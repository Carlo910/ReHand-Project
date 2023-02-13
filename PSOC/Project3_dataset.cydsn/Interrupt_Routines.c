/* ========================================
 * PROGETTO 3
 * RE-HAND 
 * Codice per la creazione del dataset
 * ========================================
*/
#include "Interrupt_Routines.h"
#include "project.h"

// Dichiarazioni Variabile
int32 value_digit;
int32 value_digit1;
int32 value_read1;
int32 value_read[4];
int8 i=0, j=0, k=0;

CY_ISR(Custom_ISR_ADC)
{
    //Lettura resgistro Timer
    Timer_ReadStatusRegister();
     
      for(j=0; j<10; j++){
        for(i=0; i<4; i++){
        AMux_Select(i);
        value_digit = ADC_DelSig_Read32();
        // Controllo pacchetto
        if (value_digit < 0)  value_digit = 0;
        if (value_digit > 65535) value_digit = 65535;
      
        value_read[i]= value_read[i] + value_digit;

          }
        }
        // Costruzione pacchetti in due bytes per sensore
        for(k=0; k<4; k++){
            value_read[k]=value_read[k]/10;
            DataBuffer[2*k+1] = value_read[k] >> 8;
            DataBuffer[2*k+2] = value_read[k] & 0xFF;
        }
        PacketReadyFlag  = 1;
    }

/* FINE */
