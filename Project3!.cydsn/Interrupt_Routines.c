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
int32 value_digit[2];
int32 value_mv[2];
int32 valuekR[2];
int32 valuemI[2];
int8 i=0, j=0;
CY_ISR(Custom_ISR_ADC)
{
    //Read timer status register to bring interrupt line low
    Timer_ReadStatusRegister();
    
    for(i=0; i<2; i++){
    AMux_Select(i);
    value_digit[i] = ADC_DelSig_Read32();
    if (value_digit[i] < 0)  value_digit[i] = 0;
    if (value_digit[i] > 65535) value_digit[i] = 65535;
    value_mv[i] = ADC_DelSig_CountsTo_mVolts(value_digit[i]);
    valuemI[i] = (int32) (value_mv[i]/2);
    valuekR[i] = (int32)((5000-value_mv[i])/valuemI[i]);
    sprintf(DataBuffer[i], "Sample %d: %ld kOhm\r\n\n ", i+1, valuekR[i]);
    }
    // format ADC result for transmission

    PacketReadyFlag  = 1;
}
    
/* [] END OF FILE */
