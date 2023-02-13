/* ========================================
 * PROGETTO 3
 * RE-HAND 
 * 
 * ========================================
*/
#include "project.h"
#include "stdio.h"
#include "Interrupt_Routines.h"

#define LED_ON 1
#define LED_OFF 0

char Received = 'N';

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
    PacketReadyFlag1 = 0;
    //Inzio Conversione ADC e MUX
    ADC_DelSig_StartConvert();
    AMux_Start();
    
    //Header e Tail dei pacchetti dati sensori e batteria
    DataBuffer[0] = 0xA0;
    DataBuffer[TRANSMIT_BUFFER_SIZE-1] = 0xC0;
    DataBuffer1[0] = 0xAA;
    DataBuffer1[TRANSMIT_BUFFER_SIZE-1] = 0xFF;
    led_status = LED_OFF;
    
    for(;;)
    {
        // Gestione lampeggio led se il bluetooth non è connesso
        if(led_status == LED_OFF)
        {
            Pin_LED_Write(LED_ON);
            CyDelay(500);
            Pin_LED_Write(LED_OFF);
            CyDelay(500);
        }
        else
        {
            Pin_LED_Write(LED_ON);
        }
    
        // Se il bluetooth è collegato il led è fisso e i dati vengono inviati
        if(led_status == LED_ON){
        
        if ( PacketReadyFlag==1){
            for(int8 i=0; i<2; i++){
             // Comunicazione con BT dati sensori
             UART_BT_PutArray(DataBuffer, TRANSMIT_BUFFER_SIZE );
            }
        PacketReadyFlag=0;
        } if(PacketReadyFlag1==1){
            //Comunicazione con BT dati batteria 
             UART_BT_PutArray(DataBuffer1, TRANSMIT_BUFFER_SIZE);
            PacketReadyFlag1=0;
        }
    }
  }
}

/* FINE */
