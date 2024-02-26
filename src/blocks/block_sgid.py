from src.blocks.abstract_block import AbstractBlock


class BlockSGID(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
uint16_t eepVersion;        // Element eepVersion
    char sgidb7[11];            // Hardwareteilenummer
    char sgidb8[3];             // Baugruppe Hardware
    char sgidb9[2];             // Sorte Hardware
    char ReserveSGID[12];       // ReserveSGID
    uint16_t eepCheckSum;       // Checksumme
            };
            '''
        super().__init__(blockaddr=0x140, blocknr=10, struct_data=struct_data)
