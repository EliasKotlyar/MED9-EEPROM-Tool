from src.blocks.abstract_block import AbstractBlock


class BlockDFPMEEP(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
    uint16_t eepVersion;        // Element eepVersion
    char frz[11];               // tT7
    uint8_t error[66];              // error
    uint8_t ReserveOFPMEEP[15];    // ReserveOFPMEEP
    uint16_t eepCheckSum;      // Checksumme

            };
            '''
        super().__init__(blockaddr=0x200, blocknr=16, struct_data=struct_data)
