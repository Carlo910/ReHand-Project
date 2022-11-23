/*******************************************************************************
* File Name: R_Pin.h  
* Version 2.20
*
* Description:
*  This file contains Pin function prototypes and register defines
*
* Note:
*
********************************************************************************
* Copyright 2008-2015, Cypress Semiconductor Corporation.  All rights reserved.
* You may use this file only in accordance with the license, terms, conditions, 
* disclaimers, and limitations in the end user license agreement accompanying 
* the software package with which this file was provided.
*******************************************************************************/

#if !defined(CY_PINS_R_Pin_H) /* Pins R_Pin_H */
#define CY_PINS_R_Pin_H

#include "cytypes.h"
#include "cyfitter.h"
#include "cypins.h"
#include "R_Pin_aliases.h"

/* APIs are not generated for P15[7:6] */
#if !(CY_PSOC5A &&\
	 R_Pin__PORT == 15 && ((R_Pin__MASK & 0xC0) != 0))


/***************************************
*        Function Prototypes             
***************************************/    

/**
* \addtogroup group_general
* @{
*/
void    R_Pin_Write(uint8 value);
void    R_Pin_SetDriveMode(uint8 mode);
uint8   R_Pin_ReadDataReg(void);
uint8   R_Pin_Read(void);
void    R_Pin_SetInterruptMode(uint16 position, uint16 mode);
uint8   R_Pin_ClearInterrupt(void);
/** @} general */

/***************************************
*           API Constants        
***************************************/
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup driveMode Drive mode constants
     * \brief Constants to be passed as "mode" parameter in the R_Pin_SetDriveMode() function.
     *  @{
     */
        #define R_Pin_DM_ALG_HIZ         PIN_DM_ALG_HIZ
        #define R_Pin_DM_DIG_HIZ         PIN_DM_DIG_HIZ
        #define R_Pin_DM_RES_UP          PIN_DM_RES_UP
        #define R_Pin_DM_RES_DWN         PIN_DM_RES_DWN
        #define R_Pin_DM_OD_LO           PIN_DM_OD_LO
        #define R_Pin_DM_OD_HI           PIN_DM_OD_HI
        #define R_Pin_DM_STRONG          PIN_DM_STRONG
        #define R_Pin_DM_RES_UPDWN       PIN_DM_RES_UPDWN
    /** @} driveMode */
/** @} group_constants */
    
/* Digital Port Constants */
#define R_Pin_MASK               R_Pin__MASK
#define R_Pin_SHIFT              R_Pin__SHIFT
#define R_Pin_WIDTH              1u

/* Interrupt constants */
#if defined(R_Pin__INTSTAT)
/**
* \addtogroup group_constants
* @{
*/
    /** \addtogroup intrMode Interrupt constants
     * \brief Constants to be passed as "mode" parameter in R_Pin_SetInterruptMode() function.
     *  @{
     */
        #define R_Pin_INTR_NONE      (uint16)(0x0000u)
        #define R_Pin_INTR_RISING    (uint16)(0x0001u)
        #define R_Pin_INTR_FALLING   (uint16)(0x0002u)
        #define R_Pin_INTR_BOTH      (uint16)(0x0003u) 
    /** @} intrMode */
/** @} group_constants */

    #define R_Pin_INTR_MASK      (0x01u) 
#endif /* (R_Pin__INTSTAT) */


/***************************************
*             Registers        
***************************************/

/* Main Port Registers */
/* Pin State */
#define R_Pin_PS                     (* (reg8 *) R_Pin__PS)
/* Data Register */
#define R_Pin_DR                     (* (reg8 *) R_Pin__DR)
/* Port Number */
#define R_Pin_PRT_NUM                (* (reg8 *) R_Pin__PRT) 
/* Connect to Analog Globals */                                                  
#define R_Pin_AG                     (* (reg8 *) R_Pin__AG)                       
/* Analog MUX bux enable */
#define R_Pin_AMUX                   (* (reg8 *) R_Pin__AMUX) 
/* Bidirectional Enable */                                                        
#define R_Pin_BIE                    (* (reg8 *) R_Pin__BIE)
/* Bit-mask for Aliased Register Access */
#define R_Pin_BIT_MASK               (* (reg8 *) R_Pin__BIT_MASK)
/* Bypass Enable */
#define R_Pin_BYP                    (* (reg8 *) R_Pin__BYP)
/* Port wide control signals */                                                   
#define R_Pin_CTL                    (* (reg8 *) R_Pin__CTL)
/* Drive Modes */
#define R_Pin_DM0                    (* (reg8 *) R_Pin__DM0) 
#define R_Pin_DM1                    (* (reg8 *) R_Pin__DM1)
#define R_Pin_DM2                    (* (reg8 *) R_Pin__DM2) 
/* Input Buffer Disable Override */
#define R_Pin_INP_DIS                (* (reg8 *) R_Pin__INP_DIS)
/* LCD Common or Segment Drive */
#define R_Pin_LCD_COM_SEG            (* (reg8 *) R_Pin__LCD_COM_SEG)
/* Enable Segment LCD */
#define R_Pin_LCD_EN                 (* (reg8 *) R_Pin__LCD_EN)
/* Slew Rate Control */
#define R_Pin_SLW                    (* (reg8 *) R_Pin__SLW)

/* DSI Port Registers */
/* Global DSI Select Register */
#define R_Pin_PRTDSI__CAPS_SEL       (* (reg8 *) R_Pin__PRTDSI__CAPS_SEL) 
/* Double Sync Enable */
#define R_Pin_PRTDSI__DBL_SYNC_IN    (* (reg8 *) R_Pin__PRTDSI__DBL_SYNC_IN) 
/* Output Enable Select Drive Strength */
#define R_Pin_PRTDSI__OE_SEL0        (* (reg8 *) R_Pin__PRTDSI__OE_SEL0) 
#define R_Pin_PRTDSI__OE_SEL1        (* (reg8 *) R_Pin__PRTDSI__OE_SEL1) 
/* Port Pin Output Select Registers */
#define R_Pin_PRTDSI__OUT_SEL0       (* (reg8 *) R_Pin__PRTDSI__OUT_SEL0) 
#define R_Pin_PRTDSI__OUT_SEL1       (* (reg8 *) R_Pin__PRTDSI__OUT_SEL1) 
/* Sync Output Enable Registers */
#define R_Pin_PRTDSI__SYNC_OUT       (* (reg8 *) R_Pin__PRTDSI__SYNC_OUT) 

/* SIO registers */
#if defined(R_Pin__SIO_CFG)
    #define R_Pin_SIO_HYST_EN        (* (reg8 *) R_Pin__SIO_HYST_EN)
    #define R_Pin_SIO_REG_HIFREQ     (* (reg8 *) R_Pin__SIO_REG_HIFREQ)
    #define R_Pin_SIO_CFG            (* (reg8 *) R_Pin__SIO_CFG)
    #define R_Pin_SIO_DIFF           (* (reg8 *) R_Pin__SIO_DIFF)
#endif /* (R_Pin__SIO_CFG) */

/* Interrupt Registers */
#if defined(R_Pin__INTSTAT)
    #define R_Pin_INTSTAT            (* (reg8 *) R_Pin__INTSTAT)
    #define R_Pin_SNAP               (* (reg8 *) R_Pin__SNAP)
    
	#define R_Pin_0_INTTYPE_REG 		(* (reg8 *) R_Pin__0__INTTYPE)
#endif /* (R_Pin__INTSTAT) */

#endif /* CY_PSOC5A... */

#endif /*  CY_PINS_R_Pin_H */


/* [] END OF FILE */
