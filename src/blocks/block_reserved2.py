from src.blocks.abstract_block import AbstractBlock


class BlockReserviert2(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
        uint16_t eepVersion;               // Element eepVersion
        uint8_t encrypted[52];
        uint8_t res[7]; 
        uint8_t eepCounter;            // Plausibilisierung Doppelablage
        uint16_t eepCheckSum;              // Element eepCheckSum - Checksumme
            };
            '''
        super().__init__(blockaddr=0x80, blocknr=4, struct_data=struct_data)
