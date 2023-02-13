/* ========================================
 * PROGETTO 3
 * RE-HAND 
 * 
 * ========================================
*/

#include "Interrupt_Routines.h"
#include "project.h"

// Dichiarazioni variabili
int32 value_digit;
int32 value_digit1;
int32 value_read1;
int32 value_read[4];
int32 count=0;
char received_char = 'N';
int8 i=0, j=0, k=0;

CY_ISR(Custom_ISR_ADC)
{
    count++;
    // Lettura registro Timer
    Timer_ReadStatusRegister();
    
    //Invio valore dati in due bytes per sensore
    if(count<600){
      for(j=0; j<10; j++){
        for(i=0; i<4; i++){
        AMux_Select(i);
        value_digit = ADC_DelSig_Read32();
        // Controllo dati
        if (value_digit < 0)  value_digit = 0;
        if (value_digit > 65535) value_digit = 65535;
      
        value_read[i]= value_read[i] + value_digit;

          }
        }
        // Costruzione pacchetto
        for(k=0; k<4; k++){
            value_read[k]=value_read[k]/10;
            DataBuffer[2*k+1] = value_read[k] >> 8;
            DataBuffer[2*k+2] = value_read[k] & 0xFF;
        }
        PacketReadyFlag  = 1;    
    }else if(count==600){
        // Invio valore batteria in due bytes
        AMux_Select(4);
        value_digit1 = ADC_DelSig_Read32();
        // Controllo dati
        if (value_digit1 < 0)  value_digit1 = 0;
        if (value_digit1 > 65535) value_digit1 = 65535;

        value_read1=value_digit1;
        // Costruzione pacchetto 
        DataBuffer1[1] = value_read1 >> 8;
        DataBuffer1[2] = value_read1 & 0xFF;
        for (i=0;i<6;i++){
            DataBuffer1[3+i]=0x00;
        }

        PacketReadyFlag1  = 1;
        count=0;
        
    }
    
    // Gestione connessione BT e lampeggio del led 
    received_char = UART_BT_GetChar();
    if(received_char == 'Y')
    {
        led_status = LED_ON;
    }
    else if(received_char == 'N')
    {
        led_status = LED_OFF;
    }
}

    
/* [] FINE */
