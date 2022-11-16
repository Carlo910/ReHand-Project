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

int main(void)
{
    CyGlobalIntEnable; /* Enable global interrupts. */

    /* Place your initialization/startup code here (e.g. MyInst_Start()) */
    ADC_DelSig_Start();
    UART_Start();
    Timer_Start();
    isr_ADC_StartEx(Custom_ISR_ADC);
    //Initialize send flag
    PacketReadyFlag = 0;
    //Start the ADC conversion
    ADC_DelSig_StartConvert();
    
    //Mux Start
    AMux_Start();
    
    for(;;)
    {
        /* Place your application code here. */
       if ( PacketReadyFlag==1){
        //Send data
        for(int8 i=0; i<2; i++){
        UART_PutString(DataBuffer[i]);
        }
        PacketReadyFlag=0;
      }
    }
}

/* [] END OF FILE */
