from src.blocks.abstract_block import AbstractBlock


class BlockReserviert1(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
            uint16_t eepVersion;               // Element eepVersion
            uint8_t data[9];
            uint16_t sec_code;
            uint8_t sec_bytes[7];
            uint8_t data2[5];
            uint8_t immo_byte;
            uint8_t data3;
        uint8_t res[2]; 
        uint8_t eepCounter;            // Plausibilisierung Doppelablage
        uint16_t eepCheckSum;              // Element eepCheckSum - Checksumme
            };
            '''
        super().__init__(blockaddr=0x40, blocknr=1, struct_data=struct_data)
