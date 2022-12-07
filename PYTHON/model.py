#!/usr/bin/env python3

# Import all the required packages
import socket, struct, time, os
import numpy as np
import pickle; from sklearn.preprocessing import MinMaxScaler
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf; from tensorflow import keras
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2; from tensorflow_addons.metrics import F1Score


'''
    Function definitions
'''
# Connect to a TCP socket
def connect_socket(host, port, device):
    count = 0
    s = socket.socket()
    while count < 600:
        try:
            s.connect((host, port))
            break
        except ConnectionRefusedError:
            time.sleep(1.0)
            count +=1
    if count == 20:
        print("Cannot connect to {}:{}. Please check that the {} is connected and the main app is running.".format(host, port, device))
        exit(1)
    else:
        print("Connection successful with {}:{}".format(host, port))
        return s

# Connect via TCP socket to the Xsens data acquisition program
def connect_xsens(host="127.0.0.1", port=50500):
    return connect_socket(host, port, "Xsens Master")

# Connect via TCP socket to the FES stimulator program
def connect_FES_stimulator(host="127.0.0.1", port=50400):
    return connect_socket(host, port, "FES stimulator")

# Catch the interrupt signal SIGINT (CTRL+C) and use it to stop the program
def sigint_handler(sig, f):
    global run
    run = False

def wrap_frozen_graph(graph_def, inputs, outputs, print_graph=False):
    def _imports_graph_def():
        tf.compat.v1.import_graph_def(graph_def, name="")

    wrapped_import = tf.compat.v1.wrap_function(_imports_graph_def, [])
    import_graph = wrapped_import.graph

    if print_graph == True:
        print("-" * 50)
        print("Frozen model layers: ")
        layers = [op.name for op in import_graph.get_operations()]
        # for layer in layers:
        #     print(layer)
        print("-" * 50)

    return wrapped_import.prune(
        tf.nest.map_structure(import_graph.as_graph_element, inputs),
        tf.nest.map_structure(import_graph.as_graph_element, outputs))


# Run boolean flag
run = True

# We get 6 channels * 4 sensors * 4 bytes for each packet (96 bytes)
NUM_XSENS = 4
xsens_channels = 6*NUM_XSENS
xsens_packet_size = xsens_channels*4 # [byte]

'''
    Code executed with `python model.py`
'''
if __name__ == '__main__':

    # Connect to FES stimulator
    sock_fes = connect_FES_stimulator()
    # # Connect to Xsens 
    sock_imu = connect_xsens()

    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

    # Load scaler
    with open('./tensorflow/model/task-classifier_scaler.h5', 'rb') as f_scaler:
        scaler = pickle.load(f_scaler)
    # Load model
    model = keras.models.load_model("./tensorflow/task-classifier.h5", compile=False)
    full_model = tf.function(lambda x: model(x))
    full_model = full_model.get_concrete_function(tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))
    # Get frozen ConcreteFunction
    frozen_func = convert_variables_to_constants_v2(full_model)
    frozen_func.graph.as_graph_def()
    # Test model
    X = np.ones((1,1,xsens_channels), dtype='float32')
    frozen_graph_predictions = frozen_func(x=tf.constant(X))

    valid_prediction = False
    xsens_packet = []
    pred = 12

    # Main loop: (retrieve data from Xsens), predict and send data to the FES stimulator
    while run:
        # Get data from Xsens if ready
        try:
            xsens_packet = sock_imu.recv(xsens_packet_size, socket.MSG_DONTWAIT)
        except BlockingIOError:
            pass
        # Check whether we got a packet
        if len(xsens_packet) == xsens_packet_size:
            # Unpack the data
            xsens_data = struct.unpack("f"*xsens_channels, bytes(xsens_packet))
            imu_data = np.array(xsens_data).reshape(1, xsens_channels)
            # Scale data
            imu_data = scaler.transform(imu_data)
            # Predict with TF model
            pred = frozen_func(x=tf.constant(imu_data.reshape(-1,1,xsens_channels).astype('float32')))
            pred = np.argmax(pred, axis=-1).squeeze()
            # We have a valid prediction on new Xsens data
            valid_prediction = True
        else:
            # We haven't received a new Xsens data packet
            # so we don't have a valid prediction
            valid_prediction = False
        # Pack the data for the FES stimulator:
        # send "-1" to signal invalid prediction from the AI model
        if valid_prediction :
            valid_prediction = False
            rx_buf = struct.pack("i", pred)
        else:
            rx_buf = struct.pack('i', -1)
        # Send data over TCP
        try:
            sock_fes.sendall(bytes(rx_buf))
        except BlockingIOError:
            sock_fes.close()
        # Loop at around 100 Hz
        time.sleep(0.01)