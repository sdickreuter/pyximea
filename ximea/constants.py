

###ENUM CONSTANTS
XI_BINNING  = 0
XI_SKIPPING = 1


# xiApi parameters
XI_PRM_DEVICE_NAME                     = b"device_name"             # Return device name
XI_PRM_DEVICE_TYPE                     = b"device_type"             # Return device type
XI_PRM_DEVICE_MODEL_ID                 = b"device_model_id"         # Return device model id
XI_PRM_DEVICE_SN                       = b"device_sn"               # Return device serial number
XI_PRM_DEVICE_SENS_SN                  = b"device_sens_sn"          # Return sensor serial number
XI_PRM_DEVICE_INSTANCE_PATH            = b"device_inst_path"        # Return device system instance path.
XI_PRM_DEVICE_USER_ID                  = b"device_user_id"          # Return custom ID of camera.
#
XI_PRM_EXPOSURE                        = b"exposure"                # Exposure time in microseconds
XI_PRM_GAIN                            = b"gain"                    # Gain in dB
XI_PRM_DOWNSAMPLING                    = b"downsampling"            # Change image resolution by binning or skipping.
XI_PRM_DOWNSAMPLING_TYPE               = b"downsampling_type"       # Change image downsampling type. XI_DOWNSAMPL_TYPE
XI_PRM_SHUTTER_TYPE                    = b"shutter_type"            # Change sensor shutter type(CMOS sensor). XI_SHUTTER_TYPE
XI_PRM_IMAGE_DATA_FORMAT               = b"imgdataformat"           # Output data format. XI_IMG_FORMAT
XI_PRM_TRANSPORT_PIXEL_FORMAT          = b"transport_pixel_format"  # Current format of pixels on transport layer. XI_GenTL_Image_Format_e
XI_PRM_SENSOR_TAPS                     = b"sensor_taps"             # Number of taps
XI_PRM_SENSOR_PIXEL_CLOCK_FREQ_HZ      = b"sensor_pixel_clock_freq_hz"# Sensor pixel clock frequency in Hz.
XI_PRM_SENSOR_PIXEL_CLOCK_FREQ_INDEX   = b"sensor_pixel_clock_freq_index"# Sensor pixel clock frequency. Selects frequency index for getter of XI_PRM_SENSOR_PIXEL_CLOCK_FREQ_HZ parameter.
XI_PRM_SENSOR_DATA_BIT_DEPTH           = b"sensor_bit_depth"        # Sensor output data bit depth.
XI_PRM_OUTPUT_DATA_BIT_DEPTH           = b"output_bit_depth"        # Device output data bit depth.
XI_PRM_OUTPUT_DATA_PACKING             = b"output_bit_packing"      # Device output data packing (or grouping) enabled. Packing could be enabled if output_data_bit_depth > 8 and packing is available. XI_SWITCH
XI_PRM_FRAMERATE                       = b"framerate"               # Define framerate in Hz
XI_PRM_ACQ_TIMING_MODE                 = b"acq_timing_mode"         # Type of sensor frames timing. XI_ACQ_TIM_MODE
XI_PRM_AVAILABLE_BANDWIDTH             = b"available_bandwidth"     # Calculate and return available interface bandwidth(int Megabits)
XI_PRM_LIMIT_BANDWIDTH                 = b"limit_bandwidth"         # Set/get bandwidth(datarate)(in Megabits)
XI_PRM_BUFFER_POLICY                   = b"buffer_policy"           # Data move policy XI_BP
XI_PRM_WIDTH                           = b"width"                   # Width of the Image provided by the device (in pixels).
XI_PRM_HEIGHT                          = b"height"                  # Height of the Image provided by the device (in pixels).
XI_PRM_OFFSET_X                        = b"offsetX"                 # Horizontal offset from the origin to the area of interest (in pixels).
XI_PRM_OFFSET_Y                        = b"offsetY"                 # Vertical offset from the origin to the area of interest (in pixels).
XI_PRM_LUT_EN                          = b"LUTEnable"               # Activates LUT. XI_SWITCH
XI_PRM_LUT_EX                          = b"LUTIndex"                # Control the index (offset) of the coefficient to access in the LUT.
XI_PRM_LUT_VALUE                       = b"LUTValue"                # Value at entry LUTIndex of the LUT
XI_PRM_TRG_SOURCE                      = b"trigger_source"          # Defines source of trigger. XI_TRG_SOURCE
XI_PRM_TRG_SELECTOR                    = b"trigger_selector"        # Selects the type of trigger. XI_TRG_SELECTOR
XI_PRM_TRG_SOFTWARE                    = b"trigger_software"        # Generates an internal trigger. XI_PRM_TRG_SOURCE must be set to TRG_SOFTWARE.
XI_PRM_TRG_DELAY                       = b"trigger_delay"           # Specifies the delay in microseconds (us) to apply after the trigger reception before activating it.
XI_PRM_GPI_SELECTOR                    = b"gpi_selector"            # Selects GPI
XI_PRM_GPI_MODE                        = b"gpi_mode"                # Defines GPI functionality XI_GPI_MODE
XI_PRM_GPI_LEVEL                       = b"gpi_level"               # GPI level
XI_PRM_GPO_SELECTOR                    = b"gpo_selector"            # Selects GPO
XI_PRM_GPO_MODE                        = b"gpo_mode"                # Defines GPO functionality XI_GPO_MODE
XI_PRM_LED_SELECTOR                    = b"led_selector"            # Selects LED
XI_PRM_LED_MODE                        = b"led_mode"                # Defines LED functionality XI_LED_MODE
XI_PRM_ACQ_FRAME_BURST_COUNT           = b"acq_frame_burst_count"   # Sets number of frames acquired by burst. This burst is used only if trigger is set to FrameBurstStart
#
XI_PRM_IS_DEVICE_EXIST                 = b"isexist"                 # Returns 1 if camera connected and works properly. XI_SWITCH
XI_PRM_ACQ_BUFFER_SIZE                 = b"acq_buffer_size"         # Acquisition buffer size in bytes
XI_PRM_ACQ_TRANSPORT_BUFFER_SIZE       = b"acq_transport_buffer_size"# Acquisition transport buffer size in bytes
XI_PRM_BUFFERS_QUEUE_SIZE              = b"buffers_queue_size"      # Queue of field/frame buffers
XI_PRM_RECENT_FRAME                    = b"recent_frame"            # GetImage returns most recent frame XI_SWITCH
#
XI_PRM_CMS                             = b"cms"                     # Mode of color management system. XI_CMS_MODE
XI_PRM_APPLY_CMS                       = b"apply_cms"               # Enable applying of CMS profiles to xiGetImage (see XI_PRM_UT_CMS_PROFILE, XI_PRM_UT_CMS_PROFILE). XI_SWITCH
XI_PRM_INPUT_CMS_PROFILE               = b"input_cms_profile"       # Filename for input cms profile (e.g. input.icc)
XI_PRM_OUTPUT_CMS_PROFILE              = b"output_cms_profile"      # Filename for output cms profile (e.g. input.icc)
XI_PRM_IMAGE_IS_COLOR                  = b"iscolor"                 # Returns 1 for color cameras. XI_SWITCH
XI_PRM_COLOR_FILTER_ARRAY              = b"cfa"                     # Returns color filter array type of RAW data. XI_COLOR_FILTER_ARRAY
XI_PRM_WB_KR                           = b"wb_kr"                   # White balance red coefficient
XI_PRM_WB_KG                           = b"wb_kg"                   # White balance green coefficient
XI_PRM_WB_KB                           = b"wb_kb"                   # White balance blue coefficient
XI_PRM_MANUAL_WB                       = b"manual_wb"               # Calculates White Balance(xiGetImage function must be called)
XI_PRM_AUTO_WB                         = b"auto_wb"                 # Automatic white balance XI_SWITCH
XI_PRM_GAMMAY                          = b"gammaY"                  # Luminosity gamma
XI_PRM_GAMMAC                          = b"gammaC"                  # Chromaticity gamma
XI_PRM_SHARPNESS                       = b"sharpness"               # Sharpness Strenght
XI_PRM_CC_MATRIX_00                    = b"ccMTX00"                 # Color Correction Matrix element [0][0]
XI_PRM_CC_MATRIX_01                    = b"ccMTX01"                 # Color Correction Matrix element [0][1]
XI_PRM_CC_MATRIX_02                    = b"ccMTX02"                 # Color Correction Matrix element [0][2]
XI_PRM_CC_MATRIX_03                    = b"ccMTX03"                 # Color Correction Matrix element [0][3]
XI_PRM_CC_MATRIX_10                    = b"ccMTX10"                 # Color Correction Matrix element [1][0]
XI_PRM_CC_MATRIX_11                    = b"ccMTX11"                 # Color Correction Matrix element [1][1]
XI_PRM_CC_MATRIX_12                    = b"ccMTX12"                 # Color Correction Matrix element [1][2]
XI_PRM_CC_MATRIX_13                    = b"ccMTX13"                 # Color Correction Matrix element [1][3]
XI_PRM_CC_MATRIX_20                    = b"ccMTX20"                 # Color Correction Matrix element [2][0]
XI_PRM_CC_MATRIX_21                    = b"ccMTX21"                 # Color Correction Matrix element [2][1]
XI_PRM_CC_MATRIX_22                    = b"ccMTX22"                 # Color Correction Matrix element [2][2]
XI_PRM_CC_MATRIX_23                    = b"ccMTX23"                 # Color Correction Matrix element [2][3]
XI_PRM_CC_MATRIX_30                    = b"ccMTX30"                 # Color Correction Matrix element [3][0]
XI_PRM_CC_MATRIX_31                    = b"ccMTX31"                 # Color Correction Matrix element [3][1]
XI_PRM_CC_MATRIX_32                    = b"ccMTX32"                 # Color Correction Matrix element [3][2]
XI_PRM_CC_MATRIX_33                    = b"ccMTX33"                 # Color Correction Matrix element [3][3]
XI_PRM_DEFAULT_CC_MATRIX               = b"defccMTX"                # Set default Color Correction Matrix
#
XI_PRM_AEAG                            = b"aeag"                    # Automatic exposure/gain XI_SWITCH
XI_PRM_AEAG_ROI_OFFSET_X               = b"aeag_roi_offset_x"       # Automatic exposure/gain ROI offset X
XI_PRM_AEAG_ROI_OFFSET_Y               = b"aeag_roi_offset_y"       # Automatic exposure/gain ROI offset Y
XI_PRM_AEAG_ROI_WIDTH                  = b"aeag_roi_width"          # Automatic exposure/gain ROI Width
XI_PRM_AEAG_ROI_HEIGHT                 = b"aeag_roi_height"         # Automatic exposure/gain ROI Height
XI_PRM_EXP_PRIORITY                    = b"exp_priority"            # Exposure priority (0.5 - exposure 50%, gain 50%).
XI_PRM_AE_MAX_LIMIT                    = b"ae_max_limit"            # Maximum limit of exposure in AEAG procedure
XI_PRM_AG_MAX_LIMIT                    = b"ag_max_limit"            # Maximum limit of gain in AEAG procedure
XI_PRM_AEAG_LEVEL                      = b"aeag_level"              # Average intensity of output signal AEAG should achieve(in %)
#
XI_PRM_BPC                             = b"bpc"                     # Correction of bad pixels XI_SWITCH
#
XI_PRM_DEBOUNCE_EN                     = b"dbnc_en"                 # Enable/Disable debounce to selected GPI XI_SWITCH
XI_PRM_DEBOUNCE_T0                     = b"dbnc_t0"                 # Debounce time (x * 10us)
XI_PRM_DEBOUNCE_T1                     = b"dbnc_t1"                 # Debounce time (x * 10us)
XI_PRM_DEBOUNCE_POL                    = b"dbnc_pol"                # Debounce polarity (pol = 1 t0 - falling edge, t1 - rising edge)
#
XI_PRM_IS_COOLED                       = b"iscooled"                # Returns 1 for cameras that support cooling.
XI_PRM_COOLING                         = b"cooling"                 # Start camera cooling. XI_SWITCH
XI_PRM_TARGET_TEMP                     = b"target_temp"             # Set sensor target temperature for cooling.
XI_PRM_CHIP_TEMP                       = b"chip_temp"               # Camera sensor temperature
XI_PRM_HOUS_TEMP                       = b"hous_temp"               # Camera housing tepmerature
#
XI_PRM_SENSOR_MODE                     = b"sensor_mode"             # Current sensor mode. Allows to select sensor mode by one integer. Setting of this parameter affects: image dimensions and downsampling.
XI_PRM_HDR                             = b"hdr"                     # Enable High Dynamic Range feature. XI_SWITCH
XI_PRM_HDR_KNEEPOINT_COUNT             = b"hdr_kneepoint_count"     # The number of kneepoints in the PWLR.
XI_PRM_HDR_T1                          = b"hdr_t1"                  # position of first kneepoint(in % of XI_PRM_EXPOSURE)
XI_PRM_HDR_T2                          = b"hdr_t2"                  # position of second kneepoint (in % of XI_PRM_EXPOSURE)
XI_PRM_KNEEPOINT1                      = b"hdr_kneepoint1"          # value of first kneepoint (% of sensor saturation)
XI_PRM_KNEEPOINT2                      = b"hdr_kneepoint2"          # value of second kneepoint (% of sensor saturation)
XI_PRM_IMAGE_BLACK_LEVEL               = b"image_black_level"       # Last image black level counts. Can be used for Offline processing to recall it.
#
XI_PRM_API_VERSION                     = b"api_version"             # Returns version of API.
XI_PRM_DRV_VERSION                     = b"drv_version"             # Returns version of current device driver.
XI_PRM_MCU1_VERSION                    = b"version_mcu1"            # Returns version of MCU1 firmware.
XI_PRM_MCU2_VERSION                    = b"version_mcu2"            # Returns version of MCU2 firmware.
XI_PRM_FPGA1_VERSION                   = b"version_fpga1"           # Returns version of FPGA1 firmware.
#
XI_PRM_DEBUG_LEVEL                     = b"debug_level"             # Set debug level XI_DEBUG_LEVEL
XI_PRM_AUTO_BANDWIDTH_CALCULATION      = b"auto_bandwidth_calculation"# Automatic bandwidth calculation, XI_SWITCH
#
XI_PRM_READ_FILE_FFS                   = b"read_file_ffs"           # Read file from camera flash filesystem.
XI_PRM_WRITE_FILE_FFS                  = b"write_file_ffs"          # Write file to camera flash filesystem.
XI_PRM_FFS_FILE_NAME                   = b"ffs_file_name"           # Set name of file to be written/read from camera FFS.
XI_PRM_FREE_FFS_SIZE                   = b"free_ffs_size"           # Size of free camera FFS.
XI_PRM_USED_FFS_SIZE                   = b"used_ffs_size"           # Size of used camera FFS.
#
XI_PRM_API_CONTEXT_LIST                = b"xiapi_context_list"      # List of current parameters settings context - parameters with values. Used for offline processing.





#-------------------------------------------------------------------------------------------------------------------
# Global definitions
SIZE_XI_IMG_V1              =  28                   # structure size default
SIZE_XI_IMG_V2              =  40                   # structure size with timestamp and GPI level information
SIZE_XI_IMG_V3              =  44                   # structure size with black level information
SIZE_XI_IMG_V4              =  48                   # structure size with horizontal buffer padding information
XI_PRM_INFO_MIN             = b":min"               # Parameter minimum
XI_PRM_INFO_MAX             = b":max"               # Parameter maximum
XI_PRM_INFO_INCREMENT       = b":inc"               # Parameter increment
XI_PRM_INFO                 = b":info"              # Parameter value
XI_PRMM_DIRECT_UPDATE       = b":direct_update"     # Parameter modifier for direct update without stopping the streaming. E.g. XI_PRM_EXPOSURE XI_PRMM_DIRECT_UPDATE can be used with this modifier
XI_MQ_LED_STATUS1           =  1                    # MQ Status 1 LED selection value.
XI_MQ_LED_STATUS2           =  2                    # MQ Status 2 LED selection value.
XI_MQ_LED_POWER             =  3                    # MQ Power LED selection value.
XI_MS_LED_STATUS1           =  1                    # CURRERA-R LED 1 selection value.
XI_MS_LED_STATUS2           =  2                    # CURRERA-R LED 2 selection value.



###ENUM strings:
logger_levels = {
'Detail'  :0,
'Trace'   :1,
'Warning' :2,
'Error'   :3,
'Fatal'   :4,
'Disabled':100
}


###ERROR CODES:
error_codes = {
0 :  ("XI_OK","Function call succeeded"),
1 :  ("XI_INVALID_HANDLE","Invalid handle"),
2 :  ("XI_READREG","Register read error"),
3 :  ("XI_WRITEREG","Register write error"),
4 :  ("XI_FREE_RESOURCES","Freeing resiurces error"),
5 :  ("XI_FREE_CHANNEL","Freeing channel error"),
6 :  ("XI_FREE_BANDWIDTH","Freeing bandwith error"),
7 :  ("XI_READBLK","Read block error"),
8 :  ("XI_WRITEBLK","Write block error"),
9 :  ("XI_NO_IMAGE","No image"),
10 : ("XI_TIMEOUT","Timeout"),
11 : ("XI_INVALID_ARG","Invalid arguments supplied"),
12 : ("XI_NOT_SUPPORTED","Not supported"),
13 : ("XI_ISOCH_ATTACH_BUFFERS","Attach buffers error"),
14 : ("XI_GET_OVERLAPPED_RESULT","Overlapped result"),
15 : ("XI_MEMORY_ALLOCATION","Memory allocation error"),
16 : ("XI_DLLCONTEXTISNULL","DLL context is NULL"),
17 : ("XI_DLLCONTEXTISNONZERO","DLL context is non zero"),
18 : ("XI_DLLCONTEXTEXIST","DLL context exists"),
19 : ("XI_TOOMANYDEVICES","Too many devices connected"),
20 : ("XI_ERRORCAMCONTEXT","Camera context error"),
21 : ("XI_UNKNOWN_HARDWARE","Unknown hardware"),
22 : ("XI_INVALID_TM_FILE","Invalid TM file"),
23 : ("XI_INVALID_TM_TAG","Invalid TM tag"),
24 : ("XI_INCOMPLETE_TM","Incomplete TM"),
25 : ("XI_BUS_RESET_FAILED","Bus reset error"),
26 : ("XI_NOT_IMPLEMENTED","Not implemented"),
27 : ("XI_SHADING_TOOBRIGHT","Shading too bright"),
28 : ("XI_SHADING_TOODARK","Shading too dark"),
29 : ("XI_TOO_LOW_GAIN","Gain is too low"),
30 : ("XI_INVALID_BPL","Invalid bad pixel list"),
31 : ("XI_BPL_REALLOC","Bad pixel list realloc error"),
32 : ("XI_INVALID_PIXEL_LIST","Invalid pixel list"),
33 : ("XI_INVALID_FFS","Invalid Flash File System"),
34 : ("XI_INVALID_PROFILE","Invalid profile"),
35 : ("XI_INVALID_CALIBRATION","Invalid calibration"),
36 : ("XI_INVALID_BUFFER","Invalid buffer"),
38 : ("XI_INVALID_DATA","Invalid data"),
39 : ("XI_TGBUSY","Timing generator is busy"),
40 : ("XI_IO_WRONG","Wrong operation open/write/read/close"),
41 : ("XI_ACQUISITION_ALREADY_UP","Acquisition already started"),
42 : ("XI_OLD_DRIVER_VERSION","Old version of device driver installed to the system."),
43 : ("XI_GET_LAST_ERROR","To get error code please call GetLastError function."),
44 : ("XI_CANT_PROCESS","Data can't be processed"),
45 : ("XI_ACQUISITION_STOPED","Acquisition has been stopped. It should be started before GetImage."),
46 : ("XI_ACQUISITION_STOPED_WERR","Acquisition has been stoped with error."),
47 : ("XI_INVALID_INPUT_ICC_PROFILE","Input ICC profile missed or corrupted"),
48 : ("XI_INVALID_OUTPUT_ICC_PROFILE","Output ICC profile missed or corrupted"),
49 : ("XI_DEVICE_NOT_READY","Device not ready to operate"),
50 : ("XI_SHADING_TOOCONTRAST","Shading too contrast"),
51 : ("XI_ALREADY_INITIALIZED","Modile already initialized"),
52 : ("XI_NOT_ENOUGH_PRIVILEGES","Application doesn't enough privileges(one or more app"),
53 : ("XI_NOT_COMPATIBLE_DRIVER","Installed driver not compatible with current software"),
54 : ("XI_TM_INVALID_RESOURCE","TM file was not loaded successfully from resources"),
55 : ("XI_DEVICE_HAS_BEEN_RESETED","Device has been reseted, abnormal initial state"),
56 : ("XI_NO_DEVICES_FOUND","No Devices Found"),
57 : ("XI_RESOURCE_OR_FUNCTION_LOCKED","Resource(device) or function locked by mutex"),
58 : ("XI_BUFFER_SIZE_TOO_SMALL","Buffer provided by user is too small"),
100 :("XI_UNKNOWN_PARAM","Unknown parameter"),
101 :("XI_WRONG_PARAM_VALUE","Wrong parameter value"),
103 :("XI_WRONG_PARAM_TYPE","Wrong parameter type"),
104 :("XI_WRONG_PARAM_SIZE","Wrong parameter size"),
105 :("XI_BUFFER_TOO_SMALL","Input buffer too small"),
106 :("XI_NOT_SUPPORTED_PARAM","Parameter info not supported"),
107 :("XI_NOT_SUPPORTED_PARAM_INFO","Parameter info not supported"),
108 :("XI_NOT_SUPPORTED_DATA_FORMAT","Data format not supported"),
109 :("XI_READ_ONLY_PARAM","Read only parameter"),
111 :("XI_BANDWIDTH_NOT_SUPPORTED","This camera does not support currently available bandwidth"),
112 :("XI_INVALID_FFS_FILE_NAME","FFS file selector is invalid or NULL"),
113 :("XI_FFS_FILE_NOT_FOUND","FFS file not found"),
201 :("XI_PROC_OTHER_ERROR","Processing error - other"),
202 :("XI_PROC_PROCESSING_ERROR","Error while image processing."),
203 :("XI_PROC_INPUT_FORMAT_UNSUPPORTED","Input format is not supported for processing."),
204 :("XI_PROC_OUTPUT_FORMAT_UNSUPPORTED","Output format is not supported for processing.")
}
