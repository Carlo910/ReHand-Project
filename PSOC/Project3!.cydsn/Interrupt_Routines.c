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
int32 threshold[4] = {7000, 100, 6000, 7000};
int8 codifica[4];
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

}
}
for(k=0; k<4; k++){
    value_read[k]=value_read[k]/10;
    //DataBuffer[2*k+1] = value_read[k] >> 8;
    //DataBuffer[2*k+2] = value_read[k] & 0xFF;
    if(value_read[k] > threshold[k]){
        codifica[k] = 0xFF;
    }else{
        codifica[k] = 0x00;
    }
 }

//GESTURE  
if(codifica[0]==0 && codifica[1]==0 && codifica[2]==0 && codifica[3]==0){ //MANO APERTA
    DataBuffer[1] = 0x00;
}else if (codifica[0]==1 && codifica[1]==1 && codifica[2]==1 && codifica[3]==1){  //MANO CHIUSA
    DataBuffer[1] = 0x01;  
}else if(codifica[0]==1 && codifica[1]==1 && codifica[2]==0 && codifica[3]==0){   //POLLICE-INDICE
    DataBuffer[1] = 0x02;
}


PacketReadyFlag  = 1;
}
    
/* [] END OF FILE */
