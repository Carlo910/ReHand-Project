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
int32 value_digit1;
int32 value_read1;
int32 value_read[4];
int32 threshold[4] = {7000, 100, 6000, 7000};
int8 codifica[4];
int32 count=0;
/*
int32 value_mv[2];
int32 valuekR[2];
int32 valuemI[2];
*/
int8 i=0, j=0, k=0;
CY_ISR(Custom_ISR_ADC)
{
    count++;
    //Read timer status register to bring interrupt line low
    Timer_ReadStatusRegister();
    
    if(count<100){
      for(j=0; j<10; j++){
        for(i=0; i<4; i++){
        AMux_Select(i);
        value_digit = ADC_DelSig_Read32();
        if (value_digit < 0)  value_digit = 0;
        if (value_digit > 65535) value_digit = 65535;
      
        value_read[i]= value_read[i] + value_digit;

          }
        }
        for(k=0; k<4; k++){
            value_read[k]=value_read[k]/10;
            DataBuffer[2*k+1] = value_read[k] >> 8;
            DataBuffer[2*k+2] = value_read[k] & 0xFF;
        }
        PacketReadyFlag  = 1;
    }else if(count==100){
         AMux_Select(4);
        value_digit1 = ADC_DelSig_Read32();
        if (value_digit1 < 0)  value_digit1 = 0;
        if (value_digit1 > 65535) value_digit1 = 65535;
        
        //value_read1 = (float)(value_digit1*100)/65535;
        value_read1=value_digit1;
        //DataBuffer1[1] = value_read1;
        
        DataBuffer1[1] = value_read1 >> 8;
        DataBuffer1[2] = value_read1 & 0xFF;

        PacketReadyFlag1  = 1;
        
        count=0;
        
    }


}

    
/* [] END OF FILE */
