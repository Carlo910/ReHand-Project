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
#ifndef __INTERRUPT_ROUTINES_H

    #define __INTERRUPT_ROUTINES_H
    #include  "cytypes.h"
    #include  "stdio.h"
    #define  BYTE_TO_SEND 8
    #define  BYTE_BATT 8        
    #define  TRANSMIT_BUFFER_SIZE 1+BYTE_TO_SEND+1
    #define LED_ON 1
    #define LED_OFF 0
    
    CY_ISR_PROTO(Custom_ISR_ADC);

    uint8 DataBuffer[TRANSMIT_BUFFER_SIZE]; //creo una stringa dove salvare il dato da comunicare
    uint8 DataBuffer1[TRANSMIT_BUFFER_SIZE];
    volatile uint8 PacketReadyFlag; //flag per monitorare quando sono pronto ad inviare il dato con la UART
    volatile uint8 PacketReadyFlag1;
    volatile uint8_t led_status;
    
#endif



/* [] END OF FILE */
