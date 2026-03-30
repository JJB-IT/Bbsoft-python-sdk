from enum import Enum


class ProductType(str, Enum):
    DIESEL_10PPM = "Diesel10PPM"
    DIESEL_50PPM = "Diesel50PPM"
    DIESEL_500PPM = "Diesel500PPM"
    UNLEADED_93 = "Unleaded93"
    UNLEADED_95 = "Unleaded95"
    LEAD_REPLACEMENT_93 = "LeadReplacement93"
    LEAD_REPLACEMENT_95 = "LeadReplacement95"
    SUPER = "Super"
    PARAFFIN = "Paraffin"
    OIL = "Oil"
    CARWASH = "Carwash"


class TransactionStatus(str, Enum):
    AUTHORIZED = "AUTHORIZED"
    BUSY = "BUSY"
    FINISHED = "FINISHED"
    PROCESSED = "PROCESSED"
    COMPLETED = "COMPLETED"
    IQ_COMPLETED = "IQCOMPLETED"
    PROCESSED_SPEEDPOINT = "PROCESSEDSPEEDPOINT"


class PaymentType(str, Enum):
    ACCOUNT = "ACCOUNT"
    CASH = "CASH"
    CARD = "CARD"
    EFT = "EFT"


class MIF(str, Enum):
    NONE = "None"
    LEAD_REPLACEMENT_93_ALL = "LeadReplacement93All"
    LEAD_REPLACEMENT_95_ALL = "LeadReplacement95All"
    DIESEL_500PPM_ALL = "Diesel500PPMAll"
    UNLEADED_93_ALL = "Unleaded93All"
    UNLEADED_95_ALL = "Unleaded95All"
    DIESEL_50PPM_ALL = "Diesel50PPMAll"
    SHELL_VPOWER_DIESEL_50PPM_PAYAT = "ShellVPowerDiesel50PPMPayat"
    LPG_ALL = "LPGAll"
    AVGAS_POSAPI_PAYAT = "AVGASPosapiPayat"
    SHELL_VPOWER_UNLEADED_95_INLAND_IFSF = "ShellVPowerUnleaded95InlandIFSF"
    PARAFFIN_ALL = "ParaffinAll"
    SHELL_ULTRA_LR95_IFSF = "ShellUltraLeadReplacement95IFSF"
    SHELL_ULTRA_LR93_IFSF = "ShellUltraLeadReplacement93IFSF"
    SHELL_DIESEL_EXTRA_500PPM_POSAPI_PAYAT = "ShellDieselExtra500PPMPOSAPIPayat"
    SHELL_ULTRA_LR93_POSAPI_PAYAT = "ShellUltraLeadReplacement93POSAPIPayat"
    SHELL_ULTRA_LR95_POSAPI_PAYAT = "ShellUltraLeadReplacement95POSAPIPayat"
    SHELL_UNLEADED_EXTRA_93_POSAPI_PAYAT = "ShellUnleadedExtra93POSAPIPayat"
    SHELL_VPOWER_DIESEL_50PPM_IFSF_POSAPI = "ShellVPowerDiesel50PPMIFSFPosapi"
    SHELL_VPOWER_UNLEADED_95_COASTAL_POSAPI_PAYAT = "ShellVPowerUnleaded95CoastalPOSAPIPayat"
    SHELL_DIESEL_EXTRA_500PPM_IFSF = "ShellDieselExtra500PPMIFSF"
    SHELL_VPOWER_UNLEADED_95_INLAND_POSAPI_PAYAT = "ShellVPowerUnleaded95InlandPOSAPIPayat"
    DIESEL_10PPM_ALL = "Diesel10PPMAll"
    SHELL_DIESEL_EXTRA_50PPM_POSAPI_PAYAT = "ShellDieselExtra50PPMPOSAPIPayat"
    AVGAS_IFSF = "AVGASIFSF"
    OIL_PAYAT = "OilPayat"
    CARWASH_PAYAT = "CarWashPayat"
    PARKING_PAYAT = "ParkingPayat"
    TIP_PAYAT = "TipPayat"
    SHELL_UNLEADED_EXTRA_93_IFSF = "ShellUnleadedExtra93IFSF"
    SHELL_VPOWER_UNLEADED_95_COASTAL_IFSF = "ShellVPowerUnleaded95CoastalIFSF"
    SHELL_DIESEL_EXTRA_50PPM_IFSF = "ShellDieselExtra50PPMIFSF"
