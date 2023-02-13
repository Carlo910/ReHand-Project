/* ========================================
 * PROGETTO 3
 * RE-HAND 
 * Codice per la creazione del dataset
 * ========================================
*/
#include "project.h"
#include "stdio.h"
#include "Interrupt_Routines.h"


int main(void)
{
    CyGlobalIntEnable; 

    /* Inizializzazione ADC, UART, TIMER e ISR */
    ADC_DelSig_Start();
    UART_Start();
    UART_BT_Start();
    Timer_Start();
    isr_ADC_StartEx(Custom_ISR_ADC);
    //Inizializzazione Flag per la gestione invio dati
    PacketReadyFlag = 0;
    //Inzio Conversione ADC e MUX
    ADC_DelSig_StartConvert();
    AMux_Start();
    
    //Header e Tail dei pacchetti dati sensori
    DataBuffer[0] = 0xA0;
    DataBuffer[TRANSMIT_BUFFER_SIZE-1] = 0xC0;
    
    for(;;)
    {
       if ( PacketReadyFlag==1){
            //Invio dati
            for(int8 i=0; i<2; i++){
             //comunicazione UART
             UART_PutArray(DataBuffer, TRANSMIT_BUFFER_SIZE );
            }
        PacketReadyFlag=0;
        } 
    }
}

/* FINE */
