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

#include "Interrupt_Routines.h"
#include "project.h"

//variable declaretion
int32 value_digit;
int32 value_read[4];
/*
int32 value_mv[2];
int32 valuekR[2];
int32 valuemI[2];
*/
int8 i=0, j=0, k=0;
CY_ISR(Custom_ISR_ADC)
{
    //Read timer status register to bring interrupt line low
    Timer_ReadStatusRegister();
  for(j=0; j<10; j++){
    for(i=0; i<4; i++){
    AMux_Select(i);
    value_digit = ADC_DelSig_Read32();
    if (value_digit < 0)  value_digit = 0;
    if (value_digit > 65535) value_digit = 65535;
  
    value_read[i]= value_read[i] + value_digit;

    PacketReadyFlag  = 1;
}
}
for(k=0; k<4; k++){
    value_read[k]=value_read[k]/10;
    DataBuffer[2*k+1] = value_read[k] >> 8;
    DataBuffer[2*k+2] = value_read[k] & 0xFF;
  }
 }
    
/* [] END OF FILE */
