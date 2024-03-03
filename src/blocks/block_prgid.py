from src.blocks.abstract_block import AbstractBlock


class BlockPRGID(AbstractBlock):
    def __init__(self):
        struct_data = '''
                    struct block {
        uint16_t eepVersion;       // Element eepVersion
    char fpc[6];               // fpc: Flash programming code
    uint8_t state;             // Flash programming: state of programming
    uint8_t attempt;           // Flash programming: number of programming sessions
    uint8_t success;           // Flash programming: number of programming sessions with success
    uint8_t flash_info;        // Flash info
    uint16_t delayctr;         // Sperrzeit (Level1, 3)
    char not_fpc[6];           // neg. Flash programming code
    uint8_t not_state;         // neg. Flash programming: state of programming
    uint8_t not_attempt;       // neg. Flash programming: number of programming sessions
    uint8_t not_success;       // neg. Flash programming: number of programming sessions with success
    uint8_t not_flash_info;    // neg. Flash info
    uint16_t not_delayctr;     // neg. Sperrzeit (Level1, 3)
    char ReservePRG[3];        // ReservePRG
    uint8_t eepCounter;        // Plausibilisierung Doppelablage
    uint16_t eepCheckSum;      // Checksumme
                    };
                    '''

        super().__init__(blockaddr=0x280, blocknr=19, struct_data=struct_data)
