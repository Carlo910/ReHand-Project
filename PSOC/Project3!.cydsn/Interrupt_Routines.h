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
    #define  TRANSMIT_BUFFER_SIZE 1+BYTE_TO_SEND+1
    
    
    CY_ISR_PROTO(Custom_ISR_ADC);

    uint8 DataBuffer[TRANSMIT_BUFFER_SIZE]; //creo una stringa dove salvare il dato da comunicare

    volatile uint8 PacketReadyFlag; //flag per monitorare quando sono pronto ad inviare il dato con la UART
    
#endif



/* [] END OF FILE */
