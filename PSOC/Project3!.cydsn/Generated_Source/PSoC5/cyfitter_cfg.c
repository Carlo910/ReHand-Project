
/*******************************************************************************
* File Name: cyfitter_cfg.c
* 
* PSoC Creator  4.4
*
* Description:
* This file contains device initialization code.
* Except for the user defined sections in CyClockStartupError(), this file should not be modified.
* This file is automatically generated by PSoC Creator.
*
********************************************************************************
* Copyright (c) 2007-2020 Cypress Semiconductor.  All rights reserved.
* You may use this file only in accordance with the license, terms, conditions, 
* disclaimers, and limitations in the end user license agreement accompanying 
* the software package with which this file was provided.
********************************************************************************/

#include <string.h>
#include "cytypes.h"
#include "cydevice_trm.h"
#include "cyfitter.h"
#include "CyLib.h"
#include "cyfitter_cfg.h"
#include "cyapicallbacks.h"

#define CY_NEED_CYCLOCKSTARTUPERROR 1


#if defined(__GNUC__) || defined(__ARMCC_VERSION)
    #define CYPACKED 
    #define CYPACKED_ATTR __attribute__ ((packed))
    #define CYALIGNED __attribute__ ((aligned))
    #define CY_CFG_UNUSED __attribute__ ((unused))
    #ifndef CY_CFG_SECTION
        #define CY_CFG_SECTION __attribute__ ((section(".psocinit")))
    #endif
    
    #if defined(__ARMCC_VERSION)
        #define CY_CFG_MEMORY_BARRIER() __memory_changed()
    #else
        #define CY_CFG_MEMORY_BARRIER() __sync_synchronize()
    #endif
    
#elif defined(__ICCARM__)
    #include <intrinsics.h>

    #define CYPACKED __packed
    #define CYPACKED_ATTR 
    #define CYALIGNED _Pragma("data_alignment=4")
    #define CY_CFG_UNUSED _Pragma("diag_suppress=Pe177")
    #define CY_CFG_SECTION _Pragma("location=\".psocinit\"")
    
    #define CY_CFG_MEMORY_BARRIER() __DMB()
    
#else
    #error Unsupported toolchain
#endif

#ifndef CYCODE
    #define CYCODE
#endif
#ifndef CYDATA
    #define CYDATA
#endif
#ifndef CYFAR
    #define CYFAR
#endif
#ifndef CYXDATA
    #define CYXDATA
#endif


CY_CFG_UNUSED
static void CYMEMZERO(void *s, size_t n);
CY_CFG_UNUSED
static void CYMEMZERO(void *s, size_t n)
{
	(void)memset(s, 0, n);
}
CY_CFG_UNUSED
static void CYCONFIGCPY(void *dest, const void *src, size_t n);
CY_CFG_UNUSED
static void CYCONFIGCPY(void *dest, const void *src, size_t n)
{
	(void)memcpy(dest, src, n);
}
CY_CFG_UNUSED
static void CYCONFIGCPYCODE(void *dest, const void *src, size_t n);
CY_CFG_UNUSED
static void CYCONFIGCPYCODE(void *dest, const void *src, size_t n)
{
	(void)memcpy(dest, src, n);
}




/* Clock startup error codes                                                   */
#define CYCLOCKSTART_NO_ERROR    0u
#define CYCLOCKSTART_XTAL_ERROR  1u
#define CYCLOCKSTART_32KHZ_ERROR 2u
#define CYCLOCKSTART_PLL_ERROR   3u
#define CYCLOCKSTART_FLL_ERROR   4u
#define CYCLOCKSTART_WCO_ERROR   5u


#ifdef CY_NEED_CYCLOCKSTARTUPERROR
/*******************************************************************************
* Function Name: CyClockStartupError
********************************************************************************
* Summary:
*  If an error is encountered during clock configuration (crystal startup error,
*  PLL lock error, etc.), the system will end up here.  Unless reimplemented by
*  the customer, this function will stop in an infinite loop.
*
* Parameters:
*   void
*
* Return:
*   void
*
*******************************************************************************/
CY_CFG_UNUSED
static void CyClockStartupError(uint8 errorCode);
CY_CFG_UNUSED
static void CyClockStartupError(uint8 errorCode)
{
    /* To remove the compiler warning if errorCode not used.                */
    errorCode = errorCode;

    /* If we have a clock startup error (bad MHz crystal, PLL lock, etc.),  */
    /* we will end up here to allow the customer to implement something to  */
    /* deal with the clock condition.                                       */

#ifdef CY_CFG_CLOCK_STARTUP_ERROR_CALLBACK
    CY_CFG_Clock_Startup_ErrorCallback();
#else
    /*  If not using CY_CFG_CLOCK_STARTUP_ERROR_CALLBACK, place your clock startup code here. */
    /* `#START CyClockStartupError` */



    /* `#END` */

    while(1) {}
#endif /* CY_CFG_CLOCK_STARTUP_ERROR_CALLBACK */
}
#endif

#define CY_CFG_BASE_ADDR_COUNT 23u
CYPACKED typedef struct
{
	uint8 offset;
	uint8 value;
} CYPACKED_ATTR cy_cfg_addrvalue_t;

#define cy_cfg_addr_table ((const uint32 CYFAR *)0x48000000u)
#define cy_cfg_data_table ((const cy_cfg_addrvalue_t CYFAR *)0x4800005Cu)

/* IOPORT_7 Address: CYDEV_PRTDSI_PRT12_BASE Size (bytes): 6 */
#define BS_IOPORT_7_VAL ((const uint8 CYFAR *)0x480001DCu)

/* IOPINS0_7 Address: CYREG_PRT12_DR Size (bytes): 10 */
#define BS_IOPINS0_7_VAL ((const uint8 CYFAR *)0x480001E4u)

/* IOPINS0_1 Address: CYREG_PRT1_DM0 Size (bytes): 8 */
#define BS_IOPINS0_1_VAL ((const uint8 CYFAR *)0x480001F0u)

/* IOPINS0_2 Address: CYREG_PRT2_DM0 Size (bytes): 8 */
#define BS_IOPINS0_2_VAL ((const uint8 CYFAR *)0x480001F8u)

/* CYDEV_CLKDIST_ACFG0_CFG0 Address: CYREG_CLKDIST_ACFG0_CFG0 Size (bytes): 4 */
#define BS_CYDEV_CLKDIST_ACFG0_CFG0_VAL ((const uint8 CYFAR *)0x48000200u)


/*******************************************************************************
* Function Name: cfg_write_bytes32
********************************************************************************
* Summary:
*  This function is used for setting up the chip configuration areas that
*  contain relatively sparse data.
*
* Parameters:
*   void
*
* Return:
*   void
*
*******************************************************************************/
static void cfg_write_bytes32(const uint32 addr_table[], const cy_cfg_addrvalue_t data_table[]);
static void cfg_write_bytes32(const uint32 addr_table[], const cy_cfg_addrvalue_t data_table[])
{
	/* For 32-bit little-endian architectures */
	uint32 i, j = 0u;
	for (i = 0u; i < CY_CFG_BASE_ADDR_COUNT; i++)
	{
		uint32 baseAddr = addr_table[i];
		uint8 count = (uint8)baseAddr;
		baseAddr &= 0xFFFFFF00u;
		while (count != 0u)
		{
			CY_SET_REG8((void *)(baseAddr + data_table[j].offset), data_table[j].value);
			j++;
			count--;
		}
	}
}

/*******************************************************************************
* Function Name: ClockSetup
********************************************************************************
*
* Summary:
*  Performs the initialization of all of the clocks in the device based on the
*  settings in the Clock tab of the DWR.  This includes enabling the requested
*  clocks and setting the necessary dividers to produce the desired frequency. 
*
* Parameters:
*  void
*
* Return:
*  void
*
*******************************************************************************/
static void ClockSetup(void);
static void ClockSetup(void)
{
	uint32 timeout;
	uint8 pllLock;


	/* Configure Digital Clocks based on settings from Clock DWR */
	CY_SET_XTND_REG16((void CYFAR *)(CYREG_CLKDIST_DCFG0_CFG0), 0x0000u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_DCFG0_CFG0 + 0x2u), 0x50u);
	CY_SET_XTND_REG16((void CYFAR *)(CYREG_CLKDIST_DCFG1_CFG0), 0x0138u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_DCFG1_CFG0 + 0x2u), 0x18u);
	CY_SET_XTND_REG16((void CYFAR *)(CYREG_CLKDIST_DCFG2_CFG0), 0x5DBFu);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_DCFG2_CFG0 + 0x2u), 0x18u);

	/* Configure Analog Clocks based on settings from Clock DWR */
	CYCONFIGCPY((void CYFAR *)(CYREG_CLKDIST_ACFG0_CFG0), (const void CYFAR *)(BS_CYDEV_CLKDIST_ACFG0_CFG0_VAL), 4u);

	/* Configure ILO based on settings from Clock DWR */
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_SLOWCLK_ILO_CR0), 0x02u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_CR), 0x08u);

	/* Configure IMO based on settings from Clock DWR */
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_FASTCLK_IMO_CR), 0x03u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_IMO_TR1), (CY_GET_XTND_REG8((void CYFAR *)CYREG_FLSHID_CUST_TABLES_IMO_3MHZ)));

	/* Configure PLL based on settings from Clock DWR */
	CY_SET_XTND_REG16((void CYFAR *)(CYREG_FASTCLK_PLL_P), 0x0008u);
	CY_SET_XTND_REG16((void CYFAR *)(CYREG_FASTCLK_PLL_CFG0), 0x1251u);
	/* Wait up to 250us for the PLL to lock */
	pllLock = 0u;
	for (timeout = 250u / 10u; (timeout > 0u) && (pllLock != 0x03u); timeout--)
	{ 
		pllLock = 0x03u & ((uint8)((uint8)pllLock << 1) | ((CY_GET_XTND_REG8((void CYFAR *)CYREG_FASTCLK_PLL_SR) & 0x01u) >> 0));
		CyDelayCycles(10u * 48u); /* Delay 10us based on 48MHz clock */
	}
	/* If we ran out of time the PLL didn't lock so go to the error function */
	if (timeout == 0u)
	{
		CyClockStartupError(CYCLOCKSTART_PLL_ERROR);
	}

	/* Configure Bus/Master Clock based on settings from Clock DWR */
	CY_SET_XTND_REG16((void CYFAR *)(CYREG_CLKDIST_MSTR0), 0x0100u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_MSTR0), 0x07u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_BCFG0), 0x00u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_BCFG2), 0x48u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_MSTR0), 0x00u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_LD), 0x02u);
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CLKDIST_DLY1), 0x04u);

	CY_SET_XTND_REG8((void CYFAR *)(CYREG_PM_ACT_CFG2), ((CY_GET_XTND_REG8((void CYFAR *)CYREG_PM_ACT_CFG2) | 0x07u)));
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_PM_ACT_CFG1), ((CY_GET_XTND_REG8((void CYFAR *)CYREG_PM_ACT_CFG1) | 0x01u)));
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_PM_ACT_CFG0), ((CY_GET_XTND_REG8((void CYFAR *)CYREG_PM_ACT_CFG0) | 0x80u)));
}


/* Analog API Functions */


/*******************************************************************************
* Function Name: AnalogSetDefault
********************************************************************************
*
* Summary:
*  Sets up the analog portions of the chip to default values based on chip
*  configuration options from the project.
*
* Parameters:
*  void
*
* Return:
*  void
*
*******************************************************************************/
static void AnalogSetDefault(void);
static void AnalogSetDefault(void)
{
	uint8 bg_xover_inl_trim = CY_GET_XTND_REG8((void CYFAR *)(CYREG_FLSHID_MFG_CFG_BG_XOVER_INL_TRIM + 1u));
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_BG_DFT0), (bg_xover_inl_trim & 0x07u));
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_BG_DFT1), ((bg_xover_inl_trim >> 4) & 0x0Fu));
	CY_SET_XTND_REG8((void CYFAR *)CYREG_PUMP_CR0, 0x44u);
}


/*******************************************************************************
* Function Name: SetAnalogRoutingPumps
********************************************************************************
*
* Summary:
* Enables or disables the analog pumps feeding analog routing switches.
* Intended to be called at startup, based on the Vdda system configuration;
* may be called during operation when the user informs us that the Vdda voltage
* crossed the pump threshold.
*
* Parameters:
*  enabled - 1 to enable the pumps, 0 to disable the pumps
*
* Return:
*  void
*
*******************************************************************************/
void SetAnalogRoutingPumps(uint8 enabled)
{
	uint8 regValue = CY_GET_XTND_REG8((void CYFAR *)CYREG_PUMP_CR0);
	if (enabled != 0u)
	{
		regValue |= 0x22u;
	}
	else
	{
		regValue &= (uint8)~0x22u;
	}
	CY_SET_XTND_REG8((void CYFAR *)CYREG_PUMP_CR0, regValue);
}


#define CY_AMUX_UNUSED CYREG_BOOST_SR
/* This is an implementation detail of the AMux. Code that depends on it may be
   incompatible with other versions of PSoC Creator. */
uint8 CYXDATA * const CYCODE AMux__addrTable[8] = {
	(uint8 CYXDATA *)CYREG_PRT2_AG, (uint8 CYXDATA *)CYREG_DSM0_SW0, 
	(uint8 CYXDATA *)CYREG_PRT2_AG, (uint8 CYXDATA *)CYREG_DSM0_SW0, 
	(uint8 CYXDATA *)CYREG_PRT2_AG, (uint8 CYXDATA *)CYREG_DSM0_SW0, 
	(uint8 CYXDATA *)CYREG_PRT2_AG, (uint8 CYXDATA *)CYREG_DSM0_SW0, 
};

/* This is an implementation detail of the AMux. Code that depends on it may be
   incompatible with other versions of PSoC Creator. */
const uint8 CYCODE AMux__maskTable[8] = {
	0x20u, 0x02u, 
	0x10u, 0x01u, 
	0x08u, 0x08u, 
	0x40u, 0x04u, 
};

/*******************************************************************************
* Function Name: AMux_Set
********************************************************************************
* Summary:
*  This function is used to set a particular channel as active on the AMux.
*
* Parameters:  
*   channel - The mux channel input to set as active
*
* Return:
*   void
*
*******************************************************************************/
void AMux_Set(uint8 channel)
{
	if (channel < 4)
	{
		channel += channel;
		*AMux__addrTable[channel] |= AMux__maskTable[channel];
		channel++;
		*AMux__addrTable[channel] |= AMux__maskTable[channel];
	}
}

/*******************************************************************************
* Function Name: AMux_Unset
********************************************************************************
* Summary:
*  This function is used to clear a particular channel from being active on the
*  AMux.
*
* Parameters:  
*   channel - The mux channel input to mark inactive
*
* Return:
*   void
*
*******************************************************************************/
void AMux_Unset(uint8 channel)
{
	if (channel < 4)
	{
		channel += channel;
		*AMux__addrTable[channel] &= (uint8)~AMux__maskTable[channel];
		channel++;
		*AMux__addrTable[channel] &= (uint8)~AMux__maskTable[channel];
	}
}

/* This is an implementation detail of the AMux. Code that depends on it may be
   incompatible with other versions of PSoC Creator. */
uint8 CYXDATA * const CYCODE ADC_DelSig_AMux__addrTable[2] = {
	(uint8 CYXDATA *)CYREG_DSM0_SW3, 
	(uint8 CYXDATA *)CY_AMUX_UNUSED, 
};

/* This is an implementation detail of the AMux. Code that depends on it may be
   incompatible with other versions of PSoC Creator. */
const uint8 CYCODE ADC_DelSig_AMux__maskTable[2] = {
	0x40u, 
	0x00u, 
};

/*******************************************************************************
* Function Name: ADC_DelSig_AMux_Set
********************************************************************************
* Summary:
*  This function is used to set a particular channel as active on the AMux.
*
* Parameters:  
*   channel - The mux channel input to set as active
*
* Return:
*   void
*
*******************************************************************************/
void ADC_DelSig_AMux_Set(uint8 channel)
{
	if (channel < 2)
	{
		*ADC_DelSig_AMux__addrTable[channel] |= ADC_DelSig_AMux__maskTable[channel];
	}
}

/*******************************************************************************
* Function Name: ADC_DelSig_AMux_Unset
********************************************************************************
* Summary:
*  This function is used to clear a particular channel from being active on the
*  AMux.
*
* Parameters:  
*   channel - The mux channel input to mark inactive
*
* Return:
*   void
*
*******************************************************************************/
void ADC_DelSig_AMux_Unset(uint8 channel)
{
	if (channel < 2)
	{
		*ADC_DelSig_AMux__addrTable[channel] &= (uint8)~ADC_DelSig_AMux__maskTable[channel];
	}
}



/*******************************************************************************
* Function Name: cyfitter_cfg
********************************************************************************
* Summary:
*  This function is called by the start-up code for the selected device. It
*  performs all of the necessary device configuration based on the design
*  settings.  This includes settings from the Design Wide Resources (DWR) such
*  as Clocks and Pins as well as any component configuration that is necessary.
*
* Parameters:
*   void
*
* Return:
*   void
*
*******************************************************************************/

void cyfitter_cfg(void)
{
#ifdef CYGlobalIntDisable
	/* Disable interrupts by default. Let user enable if/when they want. */
	CYGlobalIntDisable
#endif

	/* Enable/Disable Debug functionality based on settings from System DWR */
	CY_SET_XTND_REG8((void CYFAR *)CYREG_MLOGIC_DEBUG, (CY_GET_XTND_REG8((void CYFAR *)CYREG_MLOGIC_DEBUG) | 0x04u));

	{

		CYPACKED typedef struct {
			void CYFAR *address;
			uint16 size;
		} CYPACKED_ATTR cfg_memset_t;


		CYPACKED typedef struct {
			void CYFAR *dest;
			const void CYFAR *src;
			uint16 size;
		} CYPACKED_ATTR cfg_memcpy_t;

		static const cfg_memset_t CYCODE cfg_memset_list[] = {
			/* address, size */
			{(void CYFAR *)(CYREG_TMR0_CFG0), 12u},
			{(void CYFAR *)(CYREG_PRT0_DR), 16u},
			{(void CYFAR *)(CYREG_PRT3_DR), 64u},
			{(void CYFAR *)(CYREG_PRT15_DR), 16u},
			{(void CYFAR *)(CYDEV_UCFG_B0_P0_U0_BASE), 4096u},
			{(void CYFAR *)(CYDEV_UCFG_B1_P2_U0_BASE), 2048u},
			{(void CYFAR *)(CYDEV_UCFG_DSI0_BASE), 2560u},
			{(void CYFAR *)(CYDEV_UCFG_DSI12_BASE), 512u},
			{(void CYFAR *)(CYREG_BCTL0_MDCLK_EN), 32u},
		};

		static const cfg_memcpy_t CYCODE cfg_memcpy_list [] = {
			/* dest, src, size */
			{(void CYFAR *)(CYDEV_PRTDSI_PRT12_BASE), BS_IOPORT_7_VAL, 6u},
		};

		uint8 CYDATA i;

		/* Zero out critical memory blocks before beginning configuration */
		for (i = 0u; i < (sizeof(cfg_memset_list)/sizeof(cfg_memset_list[0])); i++)
		{
			const cfg_memset_t CYCODE * CYDATA ms = &cfg_memset_list[i];
			CYMEMZERO(ms->address, (size_t)(uint32)(ms->size));
		}

		/* Copy device configuration data into registers */
		for (i = 0u; i < (sizeof(cfg_memcpy_list)/sizeof(cfg_memcpy_list[0])); i++)
		{
			const cfg_memcpy_t CYCODE * CYDATA mc = &cfg_memcpy_list[i];
			void * CYDATA destPtr = mc->dest;
			const void * CYDATA srcPtr = mc->src;
			uint16 CYDATA numBytes = mc->size;
			CYCONFIGCPY(destPtr, srcPtr, numBytes);
		}

		cfg_write_bytes32(cy_cfg_addr_table, cy_cfg_data_table);

		/* Perform normal device configuration. Order is not critical for these items. */
		CY_SET_XTND_REG8((void CYFAR *)(CYREG_DSM0_CR3), 0x0Au);

		/* Enable digital routing */
		CY_SET_XTND_REG8((void CYFAR *)CYREG_BCTL0_BANK_CTL, CY_GET_XTND_REG8((void CYFAR *)CYREG_BCTL0_BANK_CTL) | 0x02u);
		CY_SET_XTND_REG8((void CYFAR *)CYREG_BCTL1_BANK_CTL, CY_GET_XTND_REG8((void CYFAR *)CYREG_BCTL1_BANK_CTL) | 0x02u);

		/* Enable UDB array */
		CY_SET_XTND_REG8((void CYFAR *)CYREG_PM_ACT_CFG0, CY_GET_XTND_REG8((void CYFAR *)CYREG_PM_ACT_CFG0) | 0x40u);
		CY_SET_XTND_REG8((void CYFAR *)CYREG_PM_AVAIL_CR2, CY_GET_XTND_REG8((void CYFAR *)CYREG_PM_AVAIL_CR2) | 0x10u);
	}


	/* Perform second pass device configuration. These items must be configured in specific order after the regular configuration is done. */
	CYCONFIGCPY((void CYFAR *)(CYREG_PRT12_DR), (const void CYFAR *)(BS_IOPINS0_7_VAL), 10u);
	CYCONFIGCPY((void CYFAR *)(CYREG_PRT1_DM0), (const void CYFAR *)(BS_IOPINS0_1_VAL), 8u);
	CYCONFIGCPY((void CYFAR *)(CYREG_PRT2_DM0), (const void CYFAR *)(BS_IOPINS0_2_VAL), 8u);
	/* Switch Boost to the precision bandgap reference from its internal reference */
	CY_SET_REG8((void CYXDATA *)CYREG_BOOST_CR2, (CY_GET_REG8((void CYXDATA *)CYREG_BOOST_CR2) | 0x08u));

	/* Set Flash Cycles based on max possible frequency in case a glitch occurs during ClockSetup(). */
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CACHE_CC_CTL), (((CYDEV_INSTRUCT_CACHE_ENABLED) != 0) ? 0x61u : 0x60u));
	/* Setup clocks based on selections from Clock DWR */
	ClockSetup();
	/* Set Flash Cycles based on newly configured 24.00MHz Bus Clock. */
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_CACHE_CC_CTL), (((CYDEV_INSTRUCT_CACHE_ENABLED) != 0) ? 0x81u : 0x80u));
	CY_SET_XTND_REG8((void CYFAR *)(CYREG_PANTHER_WAITPIPE), 0x01u);

	/* Perform basic analog initialization to defaults */
	AnalogSetDefault();

	/* Configure alternate active mode */
	CYCONFIGCPY((void CYFAR *)CYDEV_PM_STBY_BASE, (const void CYFAR *)CYDEV_PM_ACT_BASE, 14u);
}
