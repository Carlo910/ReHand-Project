/* ========================================
 *
 * Copyright YOUR COMPANY, THE YEAR
 * All Rights Reserved
 * UNPUBLISHED, LICENSED SOFTWARE.
 *
 * CONFIDENTIAL AND PROPRIETARY INFORMATION
 * WHICH IS THE PROPERTY OF your company.
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
    CyGlobalIntEnable; /* Enable global interrupts. */

    /* Place your initialization/startup code here (e.g. MyInst_Start()) */
    ADC_DelSig_Start();
    UART_Start();
    UART_BT_Start();
    Timer_Start();
    isr_ADC_StartEx(Custom_ISR_ADC);
    //Initialize send flag
    PacketReadyFlag = 0;
    PacketReadyFlag1 = 0;
    //Start the ADC conversion
    ADC_DelSig_StartConvert();
    
    //Mux Start
    AMux_Start();
    
    DataBuffer[0] = 0xA0;
    DataBuffer[TRANSMIT_BUFFER_SIZE-1] = 0xC0;
    DataBuffer1[0] = 0xAA;
    DataBuffer1[TRANSMIT_BUFFER_SIZE-1] = 0xFF;
    
    for(;;)
    {
        /* Place your application code here. */
        Received = UART_BT_GetChar();
       
        if(Received!='Y'){
            Pin_LED_Write( ~Pin_LED_Read() );
            CyDelay(500);
        }
        
        
      
       if(Received=='Y'){
       Pin_LED_Write(LED_ON);
        if ( PacketReadyFlag==1){
         //Send data
            for(int8 i=0; i<2; i++){
             //comunicazione con BT
             UART_BT_PutArray(DataBuffer, TRANSMIT_BUFFER_SIZE );
             //comunicazione UART
             //UART_PutArray(DataBuffer, TRANSMIT_BUFFER_SIZE );
            }
        PacketReadyFlag=0;
        } if(PacketReadyFlag1==1){
            //comunicazione con BT
             UART_BT_PutArray(DataBuffer1, TRANSMIT_BUFFER_SIZE);
             //comunicazione UART
             //UART_PutArray(DataBuffer1, TRANSMIT_BUFFER_SIZE1 );
            PacketReadyFlag1=0;
        }

    
    }
}
}

/* [] END OF FILE */
