from src.blocks.abstract_block import AbstractBlock


class BlockDVE(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
    uint16_t eepVersion;           // Element eepVersion
    uint16_t bgdveEepBits;        // bgdveEepBits
    uint16_t udknlplr;            // udknlplr
    uint16_t udkplar;             // udkplar
    uint16_t udkplvor;            // udkplvor
    uint16_t udkplvvr;            // udkplvvr
    uint16_t wdknlpr;             // wdknlpr
    uint16_t udknlp2r;            // udknlp2r
    uint16_t udkp2ar;             // udkp2ar
    uint16_t udkp1aur_w;          // udkp1aur_w
    uint16_t udkp2aur_w;          // udkp2aur_w
    uint64_t ReserveDVE;          // ReserveDVE
    uint16_t eepCheckSum;         // eepCheckSum
            };
            '''
        super().__init__(blockaddr=0x160, blocknr=11, struct_data=struct_data)
