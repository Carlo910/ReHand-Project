// ======================================================================
// Project3!_Copy_01.v generated from TopDesign.cysch
// 01/26/2023 at 16:00
// This file is auto generated. ANY EDITS YOU MAKE MAY BE LOST WHEN THIS FILE IS REGENERATED!!!
// ======================================================================

/* -- WARNING: The following section of defines are deprecated and will be removed in a future release -- */
`define CYDEV_CHIP_DIE_LEOPARD 1
`define CYDEV_CHIP_REV_LEOPARD_PRODUCTION 3
`define CYDEV_CHIP_REV_LEOPARD_ES3 3
`define CYDEV_CHIP_REV_LEOPARD_ES2 1
`define CYDEV_CHIP_REV_LEOPARD_ES1 0
`define CYDEV_CHIP_DIE_PSOC5LP 2
`define CYDEV_CHIP_REV_PSOC5LP_PRODUCTION 0
`define CYDEV_CHIP_REV_PSOC5LP_ES0 0
`define CYDEV_CHIP_DIE_PSOC5TM 3
`define CYDEV_CHIP_REV_PSOC5TM_PRODUCTION 1
`define CYDEV_CHIP_REV_PSOC5TM_ES1 1
`define CYDEV_CHIP_REV_PSOC5TM_ES0 0
`define CYDEV_CHIP_DIE_TMA4 4
`define CYDEV_CHIP_REV_TMA4_PRODUCTION 17
`define CYDEV_CHIP_REV_TMA4_ES 17
`define CYDEV_CHIP_REV_TMA4_ES2 33
`define CYDEV_CHIP_DIE_PSOC4A 5
`define CYDEV_CHIP_REV_PSOC4A_PRODUCTION 17
`define CYDEV_CHIP_REV_PSOC4A_ES0 17
`define CYDEV_CHIP_DIE_PSOC6ABLE2 6
`define CYDEV_CHIP_REV_PSOC6ABLE2_ES 17
`define CYDEV_CHIP_REV_PSOC6ABLE2_PRODUCTION 33
`define CYDEV_CHIP_REV_PSOC6ABLE2_NO_UDB 33
`define CYDEV_CHIP_DIE_VOLANS 7
`define CYDEV_CHIP_REV_VOLANS_PRODUCTION 0
`define CYDEV_CHIP_DIE_BERRYPECKER 8
`define CYDEV_CHIP_REV_BERRYPECKER_PRODUCTION 0
`define CYDEV_CHIP_DIE_CRANE 9
`define CYDEV_CHIP_REV_CRANE_PRODUCTION 0
`define CYDEV_CHIP_DIE_FM3 10
`define CYDEV_CHIP_REV_FM3_PRODUCTION 0
`define CYDEV_CHIP_DIE_FM4 11
`define CYDEV_CHIP_REV_FM4_PRODUCTION 0
`define CYDEV_CHIP_DIE_EXPECT 2
`define CYDEV_CHIP_REV_EXPECT 0
`define CYDEV_CHIP_DIE_ACTUAL 2
/* -- WARNING: The previous section of defines are deprecated and will be removed in a future release -- */
`define CYDEV_CHIP_FAMILY_PSOC3 1
`define CYDEV_CHIP_FAMILY_PSOC4 2
`define CYDEV_CHIP_FAMILY_PSOC5 3
`define CYDEV_CHIP_FAMILY_PSOC6 4
`define CYDEV_CHIP_FAMILY_FM0P 5
`define CYDEV_CHIP_FAMILY_FM3 6
`define CYDEV_CHIP_FAMILY_FM4 7
`define CYDEV_CHIP_FAMILY_UNKNOWN 0
`define CYDEV_CHIP_MEMBER_UNKNOWN 0
`define CYDEV_CHIP_MEMBER_3A 1
`define CYDEV_CHIP_REVISION_3A_PRODUCTION 3
`define CYDEV_CHIP_REVISION_3A_ES3 3
`define CYDEV_CHIP_REVISION_3A_ES2 1
`define CYDEV_CHIP_REVISION_3A_ES1 0
`define CYDEV_CHIP_MEMBER_5B 2
`define CYDEV_CHIP_REVISION_5B_PRODUCTION 0
`define CYDEV_CHIP_REVISION_5B_ES0 0
`define CYDEV_CHIP_MEMBER_5A 3
`define CYDEV_CHIP_REVISION_5A_PRODUCTION 1
`define CYDEV_CHIP_REVISION_5A_ES1 1
`define CYDEV_CHIP_REVISION_5A_ES0 0
`define CYDEV_CHIP_MEMBER_4G 4
`define CYDEV_CHIP_REVISION_4G_PRODUCTION 17
`define CYDEV_CHIP_REVISION_4G_ES 17
`define CYDEV_CHIP_REVISION_4G_ES2 33
`define CYDEV_CHIP_MEMBER_4U 5
`define CYDEV_CHIP_REVISION_4U_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4E 6
`define CYDEV_CHIP_REVISION_4E_PRODUCTION 0
`define CYDEV_CHIP_REVISION_4E_CCG2_NO_USBPD 0
`define CYDEV_CHIP_MEMBER_4X 7
`define CYDEV_CHIP_REVISION_4X_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4O 8
`define CYDEV_CHIP_REVISION_4O_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4R 9
`define CYDEV_CHIP_REVISION_4R_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4T 10
`define CYDEV_CHIP_REVISION_4T_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4N 11
`define CYDEV_CHIP_REVISION_4N_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4S 12
`define CYDEV_CHIP_REVISION_4S_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4W 13
`define CYDEV_CHIP_REVISION_4W_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4AC 14
`define CYDEV_CHIP_REVISION_4AC_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4AD 15
`define CYDEV_CHIP_REVISION_4AD_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4AE 16
`define CYDEV_CHIP_REVISION_4AE_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4Q 17
`define CYDEV_CHIP_REVISION_4Q_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4Y 18
`define CYDEV_CHIP_REVISION_4Y_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4Z 19
`define CYDEV_CHIP_REVISION_4Z_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4D 20
`define CYDEV_CHIP_REVISION_4D_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4J 21
`define CYDEV_CHIP_REVISION_4J_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4K 22
`define CYDEV_CHIP_REVISION_4K_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4V 23
`define CYDEV_CHIP_REVISION_4V_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4H 24
`define CYDEV_CHIP_REVISION_4H_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4AA 25
`define CYDEV_CHIP_REVISION_4AA_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4A 26
`define CYDEV_CHIP_REVISION_4A_PRODUCTION 17
`define CYDEV_CHIP_REVISION_4A_ES0 17
`define CYDEV_CHIP_MEMBER_4F 27
`define CYDEV_CHIP_REVISION_4F_PRODUCTION 0
`define CYDEV_CHIP_REVISION_4F_PRODUCTION_256K 0
`define CYDEV_CHIP_REVISION_4F_PRODUCTION_256DMA 0
`define CYDEV_CHIP_MEMBER_4P 28
`define CYDEV_CHIP_REVISION_4P_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4M 29
`define CYDEV_CHIP_REVISION_4M_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4AB 30
`define CYDEV_CHIP_REVISION_4AB_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4L 31
`define CYDEV_CHIP_REVISION_4L_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_4I 32
`define CYDEV_CHIP_REVISION_4I_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_6A 33
`define CYDEV_CHIP_REVISION_6A_ES 17
`define CYDEV_CHIP_REVISION_6A_PRODUCTION 33
`define CYDEV_CHIP_REVISION_6A_NO_UDB 33
`define CYDEV_CHIP_MEMBER_PDL_FM0P_TYPE1 34
`define CYDEV_CHIP_REVISION_PDL_FM0P_TYPE1_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_PDL_FM0P_TYPE2 35
`define CYDEV_CHIP_REVISION_PDL_FM0P_TYPE2_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_PDL_FM0P_TYPE3 36
`define CYDEV_CHIP_REVISION_PDL_FM0P_TYPE3_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_FM3 37
`define CYDEV_CHIP_REVISION_FM3_PRODUCTION 0
`define CYDEV_CHIP_MEMBER_FM4 38
`define CYDEV_CHIP_REVISION_FM4_PRODUCTION 0
`define CYDEV_CHIP_FAMILY_USED 3
`define CYDEV_CHIP_MEMBER_USED 2
`define CYDEV_CHIP_REVISION_USED 0
// Component: cy_virtualmux_v1_0
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_virtualmux_v1_0"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_virtualmux_v1_0\cy_virtualmux_v1_0.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_virtualmux_v1_0"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_virtualmux_v1_0\cy_virtualmux_v1_0.v"
`endif

// Component: B_UART_v2_50
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\B_UART_v2_50"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\B_UART_v2_50\B_UART_v2_50.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\B_UART_v2_50"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\B_UART_v2_50\B_UART_v2_50.v"
`endif

// UART_v2_50(Address1=0, Address2=0, BaudRate=9600, BreakBitsRX=13, BreakBitsTX=13, BreakDetect=false, CRCoutputsEn=false, Enable_RX=0, Enable_RXIntInterrupt=0, Enable_TX=1, Enable_TXIntInterrupt=0, EnableHWAddress=0, EnIntRXInterrupt=false, EnIntTXInterrupt=false, FlowControl=0, HalfDuplexEn=false, HwTXEnSignal=true, InternalClock=true, InternalClockToleranceMinus=3.93736842105263, InternalClockTolerancePlus=3.93736842105263, InternalClockUsed=1, InterruptOnAddDetect=0, InterruptOnAddressMatch=0, InterruptOnBreak=0, InterruptOnByteRcvd=0, InterruptOnOverrunError=0, InterruptOnParityError=0, InterruptOnStopError=0, InterruptOnTXComplete=false, InterruptOnTXFifoEmpty=false, InterruptOnTXFifoFull=false, InterruptOnTXFifoNotFull=false, IntOnAddressDetect=false, IntOnAddressMatch=false, IntOnBreak=false, IntOnByteRcvd=false, IntOnOverrunError=false, IntOnParityError=false, IntOnStopError=false, NumDataBits=8, NumStopBits=1, OverSamplingRate=8, ParityType=0, ParityTypeSw=false, RequiredClock=76800, RXAddressMode=0, RXBufferSize=4, RxBuffRegSizeReplacementString=uint8, RXEnable=false, TXBitClkGenDP=true, TXBufferSize=4, TxBuffRegSizeReplacementString=uint8, TXEnable=true, Use23Polling=true, CY_API_CALLBACK_HEADER_INCLUDE=#include "cyapicallbacks.h", CY_COMMENT=, CY_COMPONENT_NAME=UART_v2_50, CY_CONFIG_TITLE=UART, CY_CONST_CONFIG=true, CY_CONTROL_FILE=<:default:>, CY_DATASHEET_FILE=<:default:>, CY_FITTER_NAME=UART, CY_INSTANCE_SHORT_NAME=UART, CY_MAJOR_VERSION=2, CY_MINOR_VERSION=50, CY_PDL_DRIVER_NAME=, CY_PDL_DRIVER_REQ_VERSION=, CY_PDL_DRIVER_SUBGROUP=, CY_PDL_DRIVER_VARIANT=, CY_REMOVE=false, CY_SUPPRESS_API_GEN=false, CY_VERSION=PSoC Creator  4.4, INSTANCE_NAME=UART, )
module UART_v2_50_0 (
    clock,
    cts_n,
    reset,
    rts_n,
    rx,
    rx_clk,
    rx_data,
    rx_interrupt,
    tx,
    tx_clk,
    tx_data,
    tx_en,
    tx_interrupt);
    input       clock;
    input       cts_n;
    input       reset;
    output      rts_n;
    input       rx;
    output      rx_clk;
    output      rx_data;
    output      rx_interrupt;
    output      tx;
    output      tx_clk;
    output      tx_data;
    output      tx_en;
    output      tx_interrupt;

    parameter Address1 = 0;
    parameter Address2 = 0;
    parameter EnIntRXInterrupt = 0;
    parameter EnIntTXInterrupt = 0;
    parameter FlowControl = 0;
    parameter HalfDuplexEn = 0;
    parameter HwTXEnSignal = 1;
    parameter NumDataBits = 8;
    parameter NumStopBits = 1;
    parameter ParityType = 0;
    parameter RXEnable = 0;
    parameter TXEnable = 1;

          wire  Net_289;
          wire  Net_61;
          wire  Net_9;


	cy_clock_v1_0
		#(.id("b0162966-0060-4af5-82d1-fcb491ad7619/be0a0e37-ad17-42ca-b5a1-1a654d736358"),
		  .source_clock_id(""),
		  .divisor(0),
		  .period("13020833333.3333"),
		  .is_direct(0),
		  .is_digital(1))
		IntClock
		 (.clock_out(Net_9));


	// VirtualMux_1 (cy_virtualmux_v1_0)
	assign Net_61 = Net_9;

    B_UART_v2_50 BUART (
        .clock(Net_61),
        .cts_n(cts_n),
        .reset(reset),
        .rts_n(rts_n),
        .rx(rx),
        .rx_clk(rx_clk),
        .rx_data(rx_data),
        .rx_interrupt(rx_interrupt),
        .tx(tx),
        .tx_clk(tx_clk),
        .tx_data(tx_data),
        .tx_en(tx_en),
        .tx_interrupt(tx_interrupt));
    defparam BUART.Address1 = 0;
    defparam BUART.Address2 = 0;
    defparam BUART.BreakBitsRX = 13;
    defparam BUART.BreakBitsTX = 13;
    defparam BUART.BreakDetect = 0;
    defparam BUART.CRCoutputsEn = 0;
    defparam BUART.FlowControl = 0;
    defparam BUART.HalfDuplexEn = 0;
    defparam BUART.HwTXEnSignal = 1;
    defparam BUART.NumDataBits = 8;
    defparam BUART.NumStopBits = 1;
    defparam BUART.OverSampleCount = 8;
    defparam BUART.ParityType = 0;
    defparam BUART.ParityTypeSw = 0;
    defparam BUART.RXAddressMode = 0;
    defparam BUART.RXEnable = 0;
    defparam BUART.RXStatusIntEnable = 0;
    defparam BUART.TXBitClkGenDP = 1;
    defparam BUART.TXEnable = 1;
    defparam BUART.Use23Polling = 1;



endmodule

// Component: cy_vref_v1_70
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_vref_v1_70"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_vref_v1_70\cy_vref_v1_70.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_vref_v1_70"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_vref_v1_70\cy_vref_v1_70.v"
`endif

// Component: cy_analog_virtualmux_v1_0
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_analog_virtualmux_v1_0"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_analog_virtualmux_v1_0\cy_analog_virtualmux_v1_0.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_analog_virtualmux_v1_0"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\cy_analog_virtualmux_v1_0\cy_analog_virtualmux_v1_0.v"
`endif

// Component: AMux_v1_80
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\AMux_v1_80"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\AMux_v1_80\AMux_v1_80.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\AMux_v1_80"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyComponentLibrary\CyComponentLibrary.cylib\AMux_v1_80\AMux_v1_80.v"
`endif

// Component: ZeroTerminal
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\ZeroTerminal"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\ZeroTerminal\ZeroTerminal.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\ZeroTerminal"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\ZeroTerminal\ZeroTerminal.v"
`endif

// Component: or_v1_0
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\or_v1_0"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\or_v1_0\or_v1_0.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\or_v1_0"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\or_v1_0\or_v1_0.v"
`endif

// ADC_DelSig_v3_30(ADC_Alignment=0, ADC_Alignment_Config2=0, ADC_Alignment_Config3=0, ADC_Alignment_Config4=0, ADC_Charge_Pump_Clock=true, ADC_Clock=1, ADC_CLOCK_FREQUENCY=640000, ADC_Input_Mode=1, ADC_Input_Range=2, ADC_Input_Range_Config2=0, ADC_Input_Range_Config3=0, ADC_Input_Range_Config4=0, ADC_Power=1, ADC_Reference=5, ADC_Reference_Config2=0, ADC_Reference_Config3=0, ADC_Reference_Config4=0, ADC_Resolution=16, ADC_Resolution_Config2=16, ADC_Resolution_Config3=16, ADC_Resolution_Config4=16, Clock_Frequency=64000, Comment_Config1=Default Config, Comment_Config2=Second Config, Comment_Config3=Third Config, Comment_Config4=Fourth Config, Config1_Name=CFG1, Config2_Name=CFG2, Config3_Name=CFG3, Config4_Name=CFG4, Configs=1, Conversion_Mode=2, Conversion_Mode_Config2=2, Conversion_Mode_Config3=2, Conversion_Mode_Config4=2, Enable_Vref_Vss=false, EnableModulatorInput=false, Input_Buffer_Gain=1, Input_Buffer_Gain_Config2=1, Input_Buffer_Gain_Config3=1, Input_Buffer_Gain_Config4=1, Input_Buffer_Mode=1, Input_Buffer_Mode_Config2=1, Input_Buffer_Mode_Config3=1, Input_Buffer_Mode_Config4=1, Ref_Voltage=1.25, Ref_Voltage_Config2=1.024, Ref_Voltage_Config3=1.024, Ref_Voltage_Config4=1.024, rm_int=false, Sample_Rate=10000, Sample_Rate_Config2=10000, Sample_Rate_Config3=10000, Sample_Rate_Config4=10000, Start_of_Conversion=0, Vdda_Value=3.3, CY_API_CALLBACK_HEADER_INCLUDE=#include "cyapicallbacks.h", CY_COMMENT=, CY_COMPONENT_NAME=ADC_DelSig_v3_30, CY_CONFIG_TITLE=ADC_DelSig, CY_CONST_CONFIG=true, CY_CONTROL_FILE=<:default:>, CY_DATASHEET_FILE=<:default:>, CY_FITTER_NAME=ADC_DelSig, CY_INSTANCE_SHORT_NAME=ADC_DelSig, CY_MAJOR_VERSION=3, CY_MINOR_VERSION=30, CY_PDL_DRIVER_NAME=, CY_PDL_DRIVER_REQ_VERSION=, CY_PDL_DRIVER_SUBGROUP=, CY_PDL_DRIVER_VARIANT=, CY_REMOVE=false, CY_SUPPRESS_API_GEN=false, CY_VERSION=PSoC Creator  4.4, INSTANCE_NAME=ADC_DelSig, )
module ADC_DelSig_v3_30_1 (
    aclk,
    eoc,
    mi,
    nVref,
    soc,
    vminus,
    vplus);
    input       aclk;
    output      eoc;
    input       mi;
    inout       nVref;
    electrical  nVref;
    input       soc;
    inout       vminus;
    electrical  vminus;
    inout       vplus;
    electrical  vplus;


          wire  Net_270;
          wire  Net_268;
          wire  Net_252;
          wire  Net_275;
          wire  Net_250;
    electrical  Net_249;
    electrical  Net_257;
    electrical  Net_248;
    electrical  Net_23;
          wire  Net_247;
          wire  aclock;
          wire [3:0] mod_dat;
          wire  mod_reset;
    electrical  Net_352;
          wire  Net_482;
          wire [7:0] Net_245;
          wire  Net_246;
    electrical  Net_34;
    electrical  Net_35;
    electrical  Net_244;
          wire  Net_93;
    electrical  Net_20;
    electrical  Net_690;
    electrical  Net_686;
    electrical  Net_520;
          wire  Net_481;
    electrical  Net_677;
    electrical  Net_41;
    electrical  Net_573;
    electrical  Net_109;
          wire  Net_488;


	cy_vref_v1_0
		#(.guid("15B3DB15-B7B3-4d62-A2DF-25EA392A7161"),
		  .name("Vssa (GND)"),
		  .autoenable(1))
		vRef_2
		 (.vout(Net_244));


	// cy_analog_virtualmux_6 (cy_analog_virtualmux_v1_0)
	cy_connect_v1_0 cy_analog_virtualmux_6_connect(Net_690, Net_35);
	defparam cy_analog_virtualmux_6_connect.sig_width = 1;

    cy_analog_noconnect_v1_0 cy_analog_noconnect_1 (
        .noconnect(Net_34));

	// cy_analog_virtualmux_4 (cy_analog_virtualmux_v1_0)
	cy_connect_v1_0 cy_analog_virtualmux_4_connect(Net_677, Net_34);
	defparam cy_analog_virtualmux_4_connect.sig_width = 1;

    // -- AMux AMux start -- ***
    // -- Mux A --
    
    cy_psoc3_amux_v1_0 AMux(
        .muxin({
            Net_690,
            Net_244
            }),
        .vout(Net_20)
        );
    
    defparam AMux.muxin_width = 2;
    defparam AMux.init_mux_sel = 2'h0;
    defparam AMux.one_active = 0;
    defparam AMux.connect_mode = 1;
    
    // -- AMux AMux end --

    cy_psoc3_ds_mod_v4_0 DSM (
        .aclock(Net_488),
        .clk_udb(1'b0),
        .dec_clock(aclock),
        .dout_udb(Net_245[7:0]),
        .ext_pin_1(Net_573),
        .ext_pin_2(Net_41),
        .ext_vssa(Net_109),
        .extclk_cp_udb(Net_93),
        .mod_dat(mod_dat[3:0]),
        .modbit(Net_481),
        .qtz_ref(Net_677),
        .reset_dec(mod_reset),
        .reset_udb(Net_482),
        .vminus(Net_520),
        .vplus(vplus));
    defparam DSM.resolution = 16;

    cy_analog_noconnect_v1_0 cy_analog_noconnect_5 (
        .noconnect(Net_352));

	// cy_analog_virtualmux_5 (cy_analog_virtualmux_v1_0)
	cy_connect_v1_0 cy_analog_virtualmux_5_connect(Net_109, Net_352);
	defparam cy_analog_virtualmux_5_connect.sig_width = 1;


	cy_clock_v1_0
		#(.id("ffc01197-b954-4c7b-b019-b81b7cbef90c/b7604721-db56-4477-98c2-8fae77869066"),
		  .source_clock_id("61737EF6-3B74-48f9-8B91-F7473A442AE7"),
		  .divisor(1),
		  .period("0"),
		  .is_direct(0),
		  .is_digital(1))
		Ext_CP_Clk
		 (.clock_out(Net_93));


    cy_analog_noconnect_v1_0 cy_analog_noconnect_3 (
        .noconnect(Net_257));

    cy_analog_noconnect_v1_0 cy_analog_noconnect_2 (
        .noconnect(Net_249));

	// cy_analog_virtualmux_3 (cy_analog_virtualmux_v1_0)
	cy_connect_v1_0 cy_analog_virtualmux_3_connect(Net_41, Net_257);
	defparam cy_analog_virtualmux_3_connect.sig_width = 1;

	// cy_analog_virtualmux_2 (cy_analog_virtualmux_v1_0)
	cy_connect_v1_0 cy_analog_virtualmux_2_connect(Net_573, Net_249);
	defparam cy_analog_virtualmux_2_connect.sig_width = 1;

	// cy_analog_virtualmux_1 (cy_analog_virtualmux_v1_0)
	cy_connect_v1_0 cy_analog_virtualmux_1_connect(Net_520, Net_20);
	defparam cy_analog_virtualmux_1_connect.sig_width = 1;


	cy_isr_v1_0
		#(.int_type(2'b10))
		IRQ
		 (.int_signal(eoc));


	// Clock_VirtualMux (cy_virtualmux_v1_0)
	assign Net_488 = Net_250;


	cy_clock_v1_0
		#(.id("ffc01197-b954-4c7b-b019-b81b7cbef90c/edd15f43-b66b-457b-be3a-5342345270c8"),
		  .source_clock_id("61737EF6-3B74-48f9-8B91-F7473A442AE7"),
		  .divisor(0),
		  .period("1562500000"),
		  .is_direct(0),
		  .is_digital(0))
		theACLK
		 (.clock_out(Net_250));


    ZeroTerminal ZeroTerminal_2 (
        .z(Net_482));

	// Clock_VirtualMux_1 (cy_virtualmux_v1_0)
	assign Net_481 = Net_252;

    cy_psoc3_decimator_v1_0 DEC (
        .aclock(aclock),
        .ext_start(soc),
        .interrupt(eoc),
        .mod_dat(mod_dat[3:0]),
        .mod_reset(mod_reset));

    ZeroTerminal ZeroTerminal_1 (
        .z(Net_252));


    assign Net_268 = Net_270 | Net_93;

    ZeroTerminal ZeroTerminal_3 (
        .z(Net_270));



endmodule

// Component: OneTerminal
`ifdef CY_BLK_DIR
`undef CY_BLK_DIR
`endif

`ifdef WARP
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\OneTerminal"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\OneTerminal\OneTerminal.v"
`else
`define CY_BLK_DIR "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\OneTerminal"
`include "C:\Program Files (x86)\Cypress\PSoC Creator\4.4\PSoC Creator\psoc\content\CyPrimitives\cyprimitives.cylib\OneTerminal\OneTerminal.v"
`endif

// Timer_v2_80(CaptureAlternatingFall=false, CaptureAlternatingRise=false, CaptureCount=2, CaptureCounterEnabled=false, CaptureInputEnabled=true, CaptureMode=1, CONTROL3=1, ControlRegRemoved=0, CtlModeReplacementString=SyncCtl, CyGetRegReplacementString=CY_GET_REG16, CySetRegReplacementString=CY_SET_REG16, DeviceFamily=PSoC5, EnableMode=0, FF16=true, FF8=false, FixedFunction=true, FixedFunctionUsed=1, HWCaptureCounterEnabled=false, InterruptOnCapture=false, InterruptOnFIFOFull=false, InterruptOnTC=true, IntOnCapture=0, IntOnFIFOFull=0, IntOnTC=1, NumberOfCaptures=1, param45=1, Period=99, RegDefReplacementString=reg16, RegSizeReplacementString=uint16, Resolution=16, RstStatusReplacementString=rstSts, RunMode=0, SiliconRevision=0, SoftwareCaptureModeEnabled=false, SoftwareTriggerModeEnabled=false, TriggerInputEnabled=false, TriggerMode=0, UDB16=false, UDB24=false, UDB32=false, UDB8=false, UDBControlReg=false, UsesHWEnable=0, VerilogSectionReplacementString=sT16, CY_API_CALLBACK_HEADER_INCLUDE=#include "cyapicallbacks.h", CY_COMMENT=, CY_COMPONENT_NAME=Timer_v2_80, CY_CONFIG_TITLE=Timer, CY_CONST_CONFIG=true, CY_CONTROL_FILE=<:default:>, CY_DATASHEET_FILE=<:default:>, CY_FITTER_NAME=Timer, CY_INSTANCE_SHORT_NAME=Timer, CY_MAJOR_VERSION=2, CY_MINOR_VERSION=80, CY_PDL_DRIVER_NAME=, CY_PDL_DRIVER_REQ_VERSION=, CY_PDL_DRIVER_SUBGROUP=, CY_PDL_DRIVER_VARIANT=, CY_REMOVE=false, CY_SUPPRESS_API_GEN=false, CY_VERSION=PSoC Creator  4.4, INSTANCE_NAME=Timer, )
module Timer_v2_80_2 (
    capture,
    capture_out,
    clock,
    enable,
    interrupt,
    reset,
    tc,
    trigger);
    input       capture;
    output      capture_out;
    input       clock;
    input       enable;
    output      interrupt;
    input       reset;
    output      tc;
    input       trigger;

    parameter CaptureCount = 2;
    parameter CaptureCounterEnabled = 0;
    parameter DeviceFamily = "PSoC5";
    parameter InterruptOnCapture = 0;
    parameter InterruptOnTC = 1;
    parameter Resolution = 16;
    parameter SiliconRevision = "0";

          wire  Net_260;
          wire  Net_261;
          wire  Net_266;
          wire  Net_102;
          wire  Net_55;
          wire  Net_57;
          wire  Net_53;
          wire  Net_51;

    cy_psoc3_timer_v1_0 TimerHW (
        .capture(capture),
        .clock(clock),
        .compare(Net_261),
        .enable(Net_266),
        .interrupt(Net_57),
        .kill(Net_260),
        .tc(Net_51),
        .timer_reset(reset));

    ZeroTerminal ZeroTerminal_1 (
        .z(Net_260));

	// VirtualMux_2 (cy_virtualmux_v1_0)
	assign interrupt = Net_57;

	// VirtualMux_3 (cy_virtualmux_v1_0)
	assign tc = Net_51;

    OneTerminal OneTerminal_1 (
        .o(Net_102));

	// VirtualMux_1 (cy_virtualmux_v1_0)
	assign Net_266 = Net_102;



endmodule

// UART_v2_50(Address1=0, Address2=0, BaudRate=9600, BreakBitsRX=13, BreakBitsTX=13, BreakDetect=false, CRCoutputsEn=false, Enable_RX=1, Enable_RXIntInterrupt=0, Enable_TX=1, Enable_TXIntInterrupt=0, EnableHWAddress=0, EnIntRXInterrupt=false, EnIntTXInterrupt=false, FlowControl=0, HalfDuplexEn=false, HwTXEnSignal=true, InternalClock=true, InternalClockToleranceMinus=3.93736842105263, InternalClockTolerancePlus=3.93736842105263, InternalClockUsed=1, InterruptOnAddDetect=0, InterruptOnAddressMatch=0, InterruptOnBreak=0, InterruptOnByteRcvd=1, InterruptOnOverrunError=0, InterruptOnParityError=0, InterruptOnStopError=0, InterruptOnTXComplete=false, InterruptOnTXFifoEmpty=false, InterruptOnTXFifoFull=false, InterruptOnTXFifoNotFull=false, IntOnAddressDetect=false, IntOnAddressMatch=false, IntOnBreak=false, IntOnByteRcvd=true, IntOnOverrunError=false, IntOnParityError=false, IntOnStopError=false, NumDataBits=8, NumStopBits=1, OverSamplingRate=8, ParityType=0, ParityTypeSw=false, RequiredClock=76800, RXAddressMode=0, RXBufferSize=4, RxBuffRegSizeReplacementString=uint8, RXEnable=true, TXBitClkGenDP=true, TXBufferSize=4, TxBuffRegSizeReplacementString=uint8, TXEnable=true, Use23Polling=true, CY_API_CALLBACK_HEADER_INCLUDE=#include "cyapicallbacks.h", CY_COMMENT=, CY_COMPONENT_NAME=UART_v2_50, CY_CONFIG_TITLE=UART_BT, CY_CONST_CONFIG=true, CY_CONTROL_FILE=<:default:>, CY_DATASHEET_FILE=<:default:>, CY_FITTER_NAME=UART_BT, CY_INSTANCE_SHORT_NAME=UART_BT, CY_MAJOR_VERSION=2, CY_MINOR_VERSION=50, CY_PDL_DRIVER_NAME=, CY_PDL_DRIVER_REQ_VERSION=, CY_PDL_DRIVER_SUBGROUP=, CY_PDL_DRIVER_VARIANT=, CY_REMOVE=false, CY_SUPPRESS_API_GEN=false, CY_VERSION=PSoC Creator  4.4, INSTANCE_NAME=UART_BT, )
module UART_v2_50_3 (
    clock,
    cts_n,
    reset,
    rts_n,
    rx,
    rx_clk,
    rx_data,
    rx_interrupt,
    tx,
    tx_clk,
    tx_data,
    tx_en,
    tx_interrupt);
    input       clock;
    input       cts_n;
    input       reset;
    output      rts_n;
    input       rx;
    output      rx_clk;
    output      rx_data;
    output      rx_interrupt;
    output      tx;
    output      tx_clk;
    output      tx_data;
    output      tx_en;
    output      tx_interrupt;

    parameter Address1 = 0;
    parameter Address2 = 0;
    parameter EnIntRXInterrupt = 0;
    parameter EnIntTXInterrupt = 0;
    parameter FlowControl = 0;
    parameter HalfDuplexEn = 0;
    parameter HwTXEnSignal = 1;
    parameter NumDataBits = 8;
    parameter NumStopBits = 1;
    parameter ParityType = 0;
    parameter RXEnable = 1;
    parameter TXEnable = 1;

          wire  Net_289;
          wire  Net_61;
          wire  Net_9;


	cy_clock_v1_0
		#(.id("eca3a73d-a6e6-48a8-bb9a-47261f5db8db/be0a0e37-ad17-42ca-b5a1-1a654d736358"),
		  .source_clock_id(""),
		  .divisor(0),
		  .period("13020833333.3333"),
		  .is_direct(0),
		  .is_digital(1))
		IntClock
		 (.clock_out(Net_9));


	// VirtualMux_1 (cy_virtualmux_v1_0)
	assign Net_61 = Net_9;

    B_UART_v2_50 BUART (
        .clock(Net_61),
        .cts_n(cts_n),
        .reset(reset),
        .rts_n(rts_n),
        .rx(rx),
        .rx_clk(rx_clk),
        .rx_data(rx_data),
        .rx_interrupt(rx_interrupt),
        .tx(tx),
        .tx_clk(tx_clk),
        .tx_data(tx_data),
        .tx_en(tx_en),
        .tx_interrupt(tx_interrupt));
    defparam BUART.Address1 = 0;
    defparam BUART.Address2 = 0;
    defparam BUART.BreakBitsRX = 13;
    defparam BUART.BreakBitsTX = 13;
    defparam BUART.BreakDetect = 0;
    defparam BUART.CRCoutputsEn = 0;
    defparam BUART.FlowControl = 0;
    defparam BUART.HalfDuplexEn = 0;
    defparam BUART.HwTXEnSignal = 1;
    defparam BUART.NumDataBits = 8;
    defparam BUART.NumStopBits = 1;
    defparam BUART.OverSampleCount = 8;
    defparam BUART.ParityType = 0;
    defparam BUART.ParityTypeSw = 0;
    defparam BUART.RXAddressMode = 0;
    defparam BUART.RXEnable = 1;
    defparam BUART.RXStatusIntEnable = 1;
    defparam BUART.TXBitClkGenDP = 1;
    defparam BUART.TXEnable = 1;
    defparam BUART.Use23Polling = 1;



endmodule

// top
module top ;

    electrical  Net_623;
    electrical  Net_592;
          wire  Net_365;
          wire  Net_364;
          wire  Net_363;
          wire  Net_362;
          wire  Net_361;
          wire  Net_360;
          wire  Net_359;
          wire  Net_358;
          wire  Net_357;
          wire  Net_356;
          wire  Net_355;
          wire  Net_354;
          wire  Net_353;
    electrical  Net_299;
    electrical  Net_167;
    electrical  Net_182;
    electrical  Net_619;
    electrical  Net_618;
    electrical  Net_139;
    electrical  Net_90;
          wire  Net_88;
          wire  Net_86;
          wire  Net_85;
          wire  Net_84;
          wire  Net_83;
          wire  Net_82;
          wire  Net_134;
    electrical  Net_74;
          wire  Net_75;
    electrical  Net_78;
          wire  Net_79;
          wire  Net_76;
          wire  Net_77;
    electrical [1:0] Net_586;
    electrical  Net_585;
    electrical  Net_584;
    electrical  Net_583;
    electrical  Net_582;
    electrical  Net_581;
    electrical  Net_580;
    electrical  Net_579;
    electrical  Net_578;
    electrical  Net_577;
    electrical  Net_576;
    electrical  Net_575;
    electrical  Net_574;
    electrical  Net_573;
    electrical  Net_572;
    electrical  Net_571;
    electrical  Net_570;
    electrical  Net_569;
    electrical  Net_568;
    electrical  Net_567;
    electrical  Net_566;
    electrical  Net_565;
    electrical  Net_564;
    electrical  Net_563;
    electrical  Net_562;
    electrical  Net_561;
    electrical  Net_560;
    electrical  Net_559;
    electrical  Net_558;
    electrical  Net_557;
    electrical  Net_537;
    electrical  Net_556;
    electrical  Net_555;
    electrical  Net_554;
    electrical  Net_553;
    electrical  Net_552;
    electrical  Net_551;
    electrical  Net_550;
    electrical  Net_549;
    electrical  Net_548;
    electrical  Net_547;
    electrical  Net_546;
    electrical  Net_545;
    electrical  Net_544;
    electrical  Net_543;
    electrical  Net_542;
    electrical  Net_541;
    electrical  Net_540;
    electrical  Net_539;
    electrical  Net_538;
          wire  Net_13;
          wire  Net_12;
          wire  Net_11;
          wire  Net_10;
          wire  Net_8;
          wire  Net_7;
          wire  Net_6;
          wire  Net_72;
          wire  Net_4;
          wire  Net_3;
          wire  Net_2;
          wire  Net_1;
    electrical  Net_617;
    electrical  Net_616;
    electrical  Net_625;
    electrical  Net_620;
    electrical  Net_624;
    electrical  Net_54;
    electrical  Net_55;
    electrical  Net_302;
    electrical  Net_301;
    electrical  Net_154;
    electrical  Net_640;
    electrical  Net_293;
    electrical  Net_166;
    electrical  Net_159;
          wire  Net_80;
          wire  Net_87;
          wire  Net_9;
          wire  Net_5;

    UART_v2_50_0 UART (
        .clock(1'b0),
        .cts_n(1'b0),
        .reset(1'b0),
        .rts_n(Net_4),
        .rx(1'b0),
        .rx_clk(Net_6),
        .rx_data(Net_7),
        .rx_interrupt(Net_8),
        .tx(Net_9),
        .tx_clk(Net_10),
        .tx_data(Net_11),
        .tx_en(Net_12),
        .tx_interrupt(Net_13));
    defparam UART.Address1 = 0;
    defparam UART.Address2 = 0;
    defparam UART.EnIntRXInterrupt = 0;
    defparam UART.EnIntTXInterrupt = 0;
    defparam UART.FlowControl = 0;
    defparam UART.HalfDuplexEn = 0;
    defparam UART.HwTXEnSignal = 1;
    defparam UART.NumDataBits = 8;
    defparam UART.NumStopBits = 1;
    defparam UART.ParityType = 0;
    defparam UART.RXEnable = 0;
    defparam UART.TXEnable = 1;

	wire [0:0] tmpOE__Rx_1_net;
	wire [0:0] tmpIO_0__Rx_1_net;
	wire [0:0] tmpINTERRUPT_0__Rx_1_net;
	electrical [0:0] tmpSIOVREF__Rx_1_net;

	cy_psoc3_pins_v1_10
		#(.id("1425177d-0d0e-4468-8bcc-e638e5509a9b"),
		  .drive_mode(3'b001),
		  .ibuf_enabled(1'b1),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("I"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b0),
		  .vtrip(2'b00),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		Rx_1
		 (.oe(tmpOE__Rx_1_net),
		  .y({1'b0}),
		  .fb({Net_5}),
		  .io({tmpIO_0__Rx_1_net[0:0]}),
		  .siovref(tmpSIOVREF__Rx_1_net),
		  .interrupt({tmpINTERRUPT_0__Rx_1_net[0:0]}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__Rx_1_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

	wire [0:0] tmpOE__Tx_1_net;
	wire [0:0] tmpFB_0__Tx_1_net;
	wire [0:0] tmpIO_0__Tx_1_net;
	wire [0:0] tmpINTERRUPT_0__Tx_1_net;
	electrical [0:0] tmpSIOVREF__Tx_1_net;

	cy_psoc3_pins_v1_10
		#(.id("ed092b9b-d398-4703-be89-cebf998501f6"),
		  .drive_mode(3'b110),
		  .ibuf_enabled(1'b1),
		  .init_dr_st(1'b1),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b1),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("O"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b0),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		Tx_1
		 (.oe(tmpOE__Tx_1_net),
		  .y({Net_9}),
		  .fb({tmpFB_0__Tx_1_net[0:0]}),
		  .io({tmpIO_0__Tx_1_net[0:0]}),
		  .siovref(tmpSIOVREF__Tx_1_net),
		  .interrupt({tmpINTERRUPT_0__Tx_1_net[0:0]}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__Tx_1_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

    cy_annotation_universal_v1_0 KIT_059_1 (
        .connect({
            Net_538,
            Net_539,
            Net_540,
            Net_541,
            Net_542,
            Net_543,
            Net_544,
            Net_545,
            Net_546,
            Net_547,
            Net_548,
            Net_549,
            Net_550,
            Net_551,
            Net_552,
            Net_553,
            Net_554,
            Net_54,
            Net_55,
            Net_555,
            Net_556,
            Net_537,
            Net_557,
            Net_558,
            Net_559,
            Net_560,
            Net_561,
            Net_562,
            Net_563,
            Net_564,
            Net_565,
            Net_566,
            Net_567,
            Net_640,
            Net_293,
            Net_154,
            Net_166,
            Net_568,
            Net_569,
            Net_570,
            Net_571,
            Net_572,
            Net_573,
            Net_574,
            Net_575,
            Net_576,
            Net_577,
            Net_578,
            Net_579,
            Net_580,
            Net_581,
            Net_302,
            Net_582,
            Net_583,
            Net_584,
            Net_301,
            Net_585,
            Net_586[1:0]
        })
    );
    defparam KIT_059_1.comp_name = "KIT_059_v1_0";
    defparam KIT_059_1.port_names = "P_00, P_01, P_02, P_03, P_04, P_05, P_06, P_07, P_10, P_11, P_12, P_120, P_121, P_122, P_123, P_124, P_125, P_126, P_127, P_13, P_14, P_15, P_150, P_151, P_152, P_153, P_154, P_155, P_16, P_17, P_20, P_21, P_22, P_23, P_24, P_25, P_26, P_27, P_30, P_31, P_32, P_33, P_34, P_35, P_36, P_37, P_59, P_60, P_61, P_62, P_63, P_GND_0, P_GND_1, P_GND_3, P_RST_0, P_VDD_0, P_VDDIO, USB_1_1, USB_1_0";
    defparam KIT_059_1.width = 59;

    ADC_DelSig_v3_30_1 ADC_DelSig (
        .aclk(1'b0),
        .eoc(Net_76),
        .mi(1'b0),
        .nVref(Net_78),
        .soc(1'b1),
        .vminus(Net_74),
        .vplus(Net_159));


	cy_clock_v1_0
		#(.id("c0fb34bd-1044-4931-9788-16b01ce89812"),
		  .source_clock_id(""),
		  .divisor(0),
		  .period("2000000000000"),
		  .is_direct(0),
		  .is_digital(1))
		Clock_Timer_ADC
		 (.clock_out(Net_80));


    ZeroTerminal ZeroTerminal_1 (
        .z(Net_82));

    Timer_v2_80_2 Timer (
        .capture(1'b0),
        .capture_out(Net_84),
        .clock(Net_80),
        .enable(1'b1),
        .interrupt(Net_86),
        .reset(Net_82),
        .tc(Net_87),
        .trigger(1'b1));
    defparam Timer.CaptureCount = 2;
    defparam Timer.CaptureCounterEnabled = 0;
    defparam Timer.DeviceFamily = "PSoC5";
    defparam Timer.InterruptOnCapture = 0;
    defparam Timer.InterruptOnTC = 1;
    defparam Timer.Resolution = 16;
    defparam Timer.SiliconRevision = "0";

    cy_annotation_universal_v1_0 R_1 (
        .connect({
            Net_90,
            Net_154
        })
    );
    defparam R_1.comp_name = "Resistor_sm1_v1_0";
    defparam R_1.port_names = "T1, T2";
    defparam R_1.width = 2;

    cy_annotation_universal_v1_0 PWR_1 (
        .connect({
            Net_139
        })
    );
    defparam PWR_1.comp_name = "Power_v1_0";
    defparam PWR_1.port_names = "T1";
    defparam PWR_1.width = 1;

    cy_annotation_universal_v1_0 GND_1 (
        .connect({
            Net_90
        })
    );
    defparam GND_1.comp_name = "Gnd_v1_0";
    defparam GND_1.port_names = "T1";
    defparam GND_1.width = 1;

	wire [0:0] tmpOE__R_Pin_net;
	wire [0:0] tmpFB_0__R_Pin_net;
	wire [0:0] tmpIO_0__R_Pin_net;
	wire [0:0] tmpINTERRUPT_0__R_Pin_net;
	electrical [0:0] tmpSIOVREF__R_Pin_net;

	cy_psoc3_pins_v1_10
		#(.id("77715107-f8d5-47e5-a629-0fb83101ac6b"),
		  .drive_mode(3'b000),
		  .ibuf_enabled(1'b0),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("A"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b1),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		R_Pin
		 (.oe(tmpOE__R_Pin_net),
		  .y({1'b0}),
		  .fb({tmpFB_0__R_Pin_net[0:0]}),
		  .analog({Net_616}),
		  .io({tmpIO_0__R_Pin_net[0:0]}),
		  .siovref(tmpSIOVREF__R_Pin_net),
		  .interrupt({tmpINTERRUPT_0__R_Pin_net[0:0]}),
		  .annotation({Net_154}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__R_Pin_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};


	cy_isr_v1_0
		#(.int_type(2'b01))
		isr_ADC
		 (.int_signal(Net_87));


    cy_annotation_universal_v1_0 R_2 (
        .connect({
            Net_139,
            Net_154
        })
    );
    defparam R_2.comp_name = "TrimPot_sm1_v1_0";
    defparam R_2.port_names = "T1_1, T2_1";
    defparam R_2.width = 2;

    // -- AMux AMux start -- ***
    // -- Mux A --
    
    cy_psoc3_amux_v1_0 AMux(
        .muxin({
            Net_620,
            Net_619,
            Net_618,
            Net_617,
            Net_616
            }),
        .vout(Net_159)
        );
    
    defparam AMux.muxin_width = 5;
    defparam AMux.init_mux_sel = 5'h0;
    defparam AMux.one_active = 0;
    defparam AMux.connect_mode = 1;
    
    // -- AMux AMux end --

    cy_annotation_universal_v1_0 PWR_2 (
        .connect({
            Net_293
        })
    );
    defparam PWR_2.comp_name = "Power_v1_0";
    defparam PWR_2.port_names = "T1";
    defparam PWR_2.width = 1;

    cy_annotation_universal_v1_0 GND_2 (
        .connect({
            Net_182
        })
    );
    defparam GND_2.comp_name = "Gnd_v1_0";
    defparam GND_2.port_names = "T1";
    defparam GND_2.width = 1;

    cy_annotation_universal_v1_0 R_3 (
        .connect({
            Net_182,
            Net_293
        })
    );
    defparam R_3.comp_name = "Resistor_sm1_v1_0";
    defparam R_3.port_names = "T1, T2";
    defparam R_3.width = 2;

    cy_annotation_universal_v1_0 R_4 (
        .connect({
            Net_293,
            Net_293
        })
    );
    defparam R_4.comp_name = "TrimPot_sm1_v1_0";
    defparam R_4.port_names = "T1_1, T2_1";
    defparam R_4.width = 2;

	wire [0:0] tmpOE__R_Pin_1_net;
	wire [0:0] tmpFB_0__R_Pin_1_net;
	wire [0:0] tmpIO_0__R_Pin_1_net;
	wire [0:0] tmpINTERRUPT_0__R_Pin_1_net;
	electrical [0:0] tmpSIOVREF__R_Pin_1_net;

	cy_psoc3_pins_v1_10
		#(.id("1779090f-b136-4f02-8c0c-c3fc46643f1f"),
		  .drive_mode(3'b000),
		  .ibuf_enabled(1'b0),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("A"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b1),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		R_Pin_1
		 (.oe(tmpOE__R_Pin_1_net),
		  .y({1'b0}),
		  .fb({tmpFB_0__R_Pin_1_net[0:0]}),
		  .analog({Net_617}),
		  .io({tmpIO_0__R_Pin_1_net[0:0]}),
		  .siovref(tmpSIOVREF__R_Pin_1_net),
		  .interrupt({tmpINTERRUPT_0__R_Pin_1_net[0:0]}),
		  .annotation({Net_293}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__R_Pin_1_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

    cy_annotation_universal_v1_0 PWR_3 (
        .connect({
            Net_166
        })
    );
    defparam PWR_3.comp_name = "Power_v1_0";
    defparam PWR_3.port_names = "T1";
    defparam PWR_3.width = 1;

    cy_annotation_universal_v1_0 GND_3 (
        .connect({
            Net_167
        })
    );
    defparam GND_3.comp_name = "Gnd_v1_0";
    defparam GND_3.port_names = "T1";
    defparam GND_3.width = 1;

    cy_annotation_universal_v1_0 R_5 (
        .connect({
            Net_167,
            Net_166
        })
    );
    defparam R_5.comp_name = "Resistor_sm1_v1_0";
    defparam R_5.port_names = "T1, T2";
    defparam R_5.width = 2;

    cy_annotation_universal_v1_0 R_6 (
        .connect({
            Net_166,
            Net_166
        })
    );
    defparam R_6.comp_name = "TrimPot_sm1_v1_0";
    defparam R_6.port_names = "T1_1, T2_1";
    defparam R_6.width = 2;

    cy_annotation_universal_v1_0 PWR_4 (
        .connect({
            Net_640
        })
    );
    defparam PWR_4.comp_name = "Power_v1_0";
    defparam PWR_4.port_names = "T1";
    defparam PWR_4.width = 1;

    cy_annotation_universal_v1_0 GND_4 (
        .connect({
            Net_299
        })
    );
    defparam GND_4.comp_name = "Gnd_v1_0";
    defparam GND_4.port_names = "T1";
    defparam GND_4.width = 1;

    cy_annotation_universal_v1_0 R_7 (
        .connect({
            Net_299,
            Net_640
        })
    );
    defparam R_7.comp_name = "Resistor_sm1_v1_0";
    defparam R_7.port_names = "T1, T2";
    defparam R_7.width = 2;

    cy_annotation_universal_v1_0 R_8 (
        .connect({
            Net_640,
            Net_640
        })
    );
    defparam R_8.comp_name = "TrimPot_sm1_v1_0";
    defparam R_8.port_names = "T1_1, T2_1";
    defparam R_8.width = 2;

	wire [0:0] tmpOE__R_Pin_2_net;
	wire [0:0] tmpFB_0__R_Pin_2_net;
	wire [0:0] tmpIO_0__R_Pin_2_net;
	wire [0:0] tmpINTERRUPT_0__R_Pin_2_net;
	electrical [0:0] tmpSIOVREF__R_Pin_2_net;

	cy_psoc3_pins_v1_10
		#(.id("2674704e-2e5d-4518-ace4-8b4ea7641c00"),
		  .drive_mode(3'b000),
		  .ibuf_enabled(1'b0),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("A"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b1),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		R_Pin_2
		 (.oe(tmpOE__R_Pin_2_net),
		  .y({1'b0}),
		  .fb({tmpFB_0__R_Pin_2_net[0:0]}),
		  .analog({Net_618}),
		  .io({tmpIO_0__R_Pin_2_net[0:0]}),
		  .siovref(tmpSIOVREF__R_Pin_2_net),
		  .interrupt({tmpINTERRUPT_0__R_Pin_2_net[0:0]}),
		  .annotation({Net_640}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__R_Pin_2_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

	wire [0:0] tmpOE__R_Pin_3_net;
	wire [0:0] tmpFB_0__R_Pin_3_net;
	wire [0:0] tmpIO_0__R_Pin_3_net;
	wire [0:0] tmpINTERRUPT_0__R_Pin_3_net;
	electrical [0:0] tmpSIOVREF__R_Pin_3_net;

	cy_psoc3_pins_v1_10
		#(.id("4be21e74-552d-48ae-be0e-e55089e3973e"),
		  .drive_mode(3'b000),
		  .ibuf_enabled(1'b0),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("A"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b1),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		R_Pin_3
		 (.oe(tmpOE__R_Pin_3_net),
		  .y({1'b0}),
		  .fb({tmpFB_0__R_Pin_3_net[0:0]}),
		  .analog({Net_619}),
		  .io({tmpIO_0__R_Pin_3_net[0:0]}),
		  .siovref(tmpSIOVREF__R_Pin_3_net),
		  .interrupt({tmpINTERRUPT_0__R_Pin_3_net[0:0]}),
		  .annotation({Net_166}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__R_Pin_3_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

    cy_annotation_universal_v1_0 Bat_1 (
        .connect({
            Net_302,
            Net_301
        })
    );
    defparam Bat_1.comp_name = "Battery_v1_0";
    defparam Bat_1.port_names = "Neg, Pos";
    defparam Bat_1.width = 2;

    UART_v2_50_3 UART_BT (
        .clock(1'b0),
        .cts_n(1'b0),
        .reset(1'b0),
        .rts_n(Net_356),
        .rx(Net_357),
        .rx_clk(Net_358),
        .rx_data(Net_359),
        .rx_interrupt(Net_360),
        .tx(Net_361),
        .tx_clk(Net_362),
        .tx_data(Net_363),
        .tx_en(Net_364),
        .tx_interrupt(Net_365));
    defparam UART_BT.Address1 = 0;
    defparam UART_BT.Address2 = 0;
    defparam UART_BT.EnIntRXInterrupt = 0;
    defparam UART_BT.EnIntTXInterrupt = 0;
    defparam UART_BT.FlowControl = 0;
    defparam UART_BT.HalfDuplexEn = 0;
    defparam UART_BT.HwTXEnSignal = 1;
    defparam UART_BT.NumDataBits = 8;
    defparam UART_BT.NumStopBits = 1;
    defparam UART_BT.ParityType = 0;
    defparam UART_BT.RXEnable = 1;
    defparam UART_BT.TXEnable = 1;

	wire [0:0] tmpOE__Rx_2_net;
	wire [0:0] tmpIO_0__Rx_2_net;
	wire [0:0] tmpINTERRUPT_0__Rx_2_net;
	electrical [0:0] tmpSIOVREF__Rx_2_net;

	cy_psoc3_pins_v1_10
		#(.id("6d92eaa7-99d5-4768-8d3a-2b22ca90a4d2"),
		  .drive_mode(3'b001),
		  .ibuf_enabled(1'b1),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("I"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b0),
		  .vtrip(2'b00),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		Rx_2
		 (.oe(tmpOE__Rx_2_net),
		  .y({1'b0}),
		  .fb({Net_357}),
		  .io({tmpIO_0__Rx_2_net[0:0]}),
		  .siovref(tmpSIOVREF__Rx_2_net),
		  .interrupt({tmpINTERRUPT_0__Rx_2_net[0:0]}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__Rx_2_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

	wire [0:0] tmpOE__Tx_2_net;
	wire [0:0] tmpFB_0__Tx_2_net;
	wire [0:0] tmpIO_0__Tx_2_net;
	wire [0:0] tmpINTERRUPT_0__Tx_2_net;
	electrical [0:0] tmpSIOVREF__Tx_2_net;

	cy_psoc3_pins_v1_10
		#(.id("d74f456b-11c8-4022-ad0d-9b4464299a77"),
		  .drive_mode(3'b110),
		  .ibuf_enabled(1'b1),
		  .init_dr_st(1'b1),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b1),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("O"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b0),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		Tx_2
		 (.oe(tmpOE__Tx_2_net),
		  .y({Net_361}),
		  .fb({tmpFB_0__Tx_2_net[0:0]}),
		  .io({tmpIO_0__Tx_2_net[0:0]}),
		  .siovref(tmpSIOVREF__Tx_2_net),
		  .interrupt({tmpINTERRUPT_0__Tx_2_net[0:0]}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__Tx_2_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

	wire [0:0] tmpOE__Pin_LED_net;
	wire [0:0] tmpFB_0__Pin_LED_net;
	wire [0:0] tmpIO_0__Pin_LED_net;
	wire [0:0] tmpINTERRUPT_0__Pin_LED_net;
	electrical [0:0] tmpSIOVREF__Pin_LED_net;

	cy_psoc3_pins_v1_10
		#(.id("e851a3b9-efb8-48be-bbb8-b303b216c393"),
		  .drive_mode(3'b110),
		  .ibuf_enabled(1'b1),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("O"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b1),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		Pin_LED
		 (.oe(tmpOE__Pin_LED_net),
		  .y({1'b0}),
		  .fb({tmpFB_0__Pin_LED_net[0:0]}),
		  .io({tmpIO_0__Pin_LED_net[0:0]}),
		  .siovref(tmpSIOVREF__Pin_LED_net),
		  .interrupt({tmpINTERRUPT_0__Pin_LED_net[0:0]}),
		  .annotation({Net_592}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__Pin_LED_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

	wire [0:0] tmpOE__Pin_BATT_net;
	wire [0:0] tmpFB_0__Pin_BATT_net;
	wire [0:0] tmpIO_0__Pin_BATT_net;
	wire [0:0] tmpINTERRUPT_0__Pin_BATT_net;
	electrical [0:0] tmpSIOVREF__Pin_BATT_net;

	cy_psoc3_pins_v1_10
		#(.id("cdf8f356-4048-4b50-8dfa-e22d58af1000"),
		  .drive_mode(3'b000),
		  .ibuf_enabled(1'b0),
		  .init_dr_st(1'b0),
		  .input_clk_en(0),
		  .input_sync(1'b1),
		  .input_sync_mode(1'b0),
		  .intr_mode(2'b00),
		  .invert_in_clock(0),
		  .invert_in_clock_en(0),
		  .invert_in_reset(0),
		  .invert_out_clock(0),
		  .invert_out_clock_en(0),
		  .invert_out_reset(0),
		  .io_voltage(""),
		  .layout_mode("CONTIGUOUS"),
		  .oe_conn(1'b0),
		  .oe_reset(0),
		  .oe_sync(1'b0),
		  .output_clk_en(0),
		  .output_clock_mode(1'b0),
		  .output_conn(1'b0),
		  .output_mode(1'b0),
		  .output_reset(0),
		  .output_sync(1'b0),
		  .pa_in_clock(-1),
		  .pa_in_clock_en(-1),
		  .pa_in_reset(-1),
		  .pa_out_clock(-1),
		  .pa_out_clock_en(-1),
		  .pa_out_reset(-1),
		  .pin_aliases(""),
		  .pin_mode("A"),
		  .por_state(4),
		  .sio_group_cnt(0),
		  .sio_hyst(1'b1),
		  .sio_ibuf(""),
		  .sio_info(2'b00),
		  .sio_obuf(""),
		  .sio_refsel(""),
		  .sio_vtrip(""),
		  .sio_hifreq(""),
		  .sio_vohsel(""),
		  .slew_rate(1'b0),
		  .spanning(0),
		  .use_annotation(1'b1),
		  .vtrip(2'b10),
		  .width(1),
		  .ovt_hyst_trim(1'b0),
		  .ovt_needed(1'b0),
		  .ovt_slew_control(2'b00),
		  .input_buffer_sel(2'b00))
		Pin_BATT
		 (.oe(tmpOE__Pin_BATT_net),
		  .y({1'b0}),
		  .fb({tmpFB_0__Pin_BATT_net[0:0]}),
		  .analog({Net_620}),
		  .io({tmpIO_0__Pin_BATT_net[0:0]}),
		  .siovref(tmpSIOVREF__Pin_BATT_net),
		  .interrupt({tmpINTERRUPT_0__Pin_BATT_net[0:0]}),
		  .annotation({Net_625}),
		  .in_clock({1'b0}),
		  .in_clock_en({1'b1}),
		  .in_reset({1'b0}),
		  .out_clock({1'b0}),
		  .out_clock_en({1'b1}),
		  .out_reset({1'b0}));

	assign tmpOE__Pin_BATT_net = (`CYDEV_CHIP_MEMBER_USED == `CYDEV_CHIP_MEMBER_3A && `CYDEV_CHIP_REVISION_USED < `CYDEV_CHIP_REVISION_3A_ES3) ? ~{1'b1} : {1'b1};

    cy_annotation_universal_v1_0 R_9 (
        .connect({
            Net_625,
            Net_623
        })
    );
    defparam R_9.comp_name = "Resistor_sm1_v1_0";
    defparam R_9.port_names = "T1, T2";
    defparam R_9.width = 2;

    cy_annotation_universal_v1_0 R_10 (
        .connect({
            Net_624,
            Net_625
        })
    );
    defparam R_10.comp_name = "Resistor_sm1_v1_0";
    defparam R_10.port_names = "T1, T2";
    defparam R_10.width = 2;

    cy_annotation_universal_v1_0 GND_5 (
        .connect({
            Net_624
        })
    );
    defparam GND_5.comp_name = "Gnd_sm1_v1_0";
    defparam GND_5.port_names = "T1";
    defparam GND_5.width = 1;

    cy_annotation_universal_v1_0 PWR_5 (
        .connect({
            Net_623
        })
    );
    defparam PWR_5.comp_name = "Power_v1_0";
    defparam PWR_5.port_names = "T1";
    defparam PWR_5.width = 1;



endmodule

