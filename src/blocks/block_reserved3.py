from src.blocks.abstract_block import AbstractBlock


class BlockReserviert3(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
            uint16_t eepVersion;               // Element eepVersion
        uint8_t encrypted[8];
        uint8_t res[20]; 
        uint16_t eepCheckSum;              // Element eepCheckSum - Checksumme
            };
            '''
        super().__init__(blockaddr=0x100, blocknr=4, struct_data=struct_data)
