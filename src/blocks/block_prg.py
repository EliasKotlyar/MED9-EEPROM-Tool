from src.blocks.abstract_block import AbstractBlock


class BlockPRG(AbstractBlock):
    def __init__(self):
        struct_data = '''
                struct block {
    uint16_t eepVersion;           // Element eepVersion
    char KundenTeileNr[12];        // KundenTeileNr
    char SoftwareNr[4];            // SoftwareNr
    uint8_t COD_MS;                // COD_MS
    uint8_t dataSize;              // dataSize
    uint16_t hwkffp;               // hwkffp
    uint64_t ReservePRGID;         // ReservePRGID
    uint16_t eepCheckSum;          // eepCheckSum
                };
                '''
        super().__init__(blockaddr=0x260, blocknr=20, struct_data=struct_data)
