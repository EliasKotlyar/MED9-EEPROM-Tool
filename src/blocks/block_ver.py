from src.blocks.abstract_block import AbstractBlock


class BlockVER(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
    uint16_t eepVersion;               // Element eepVersion
    uint16_t tbdbkvp_w;             // tbdbkvp_w
    uint16_t upwkd_w;             // upwkd_w
    uint8_t bblkderf;             // bblkderf
    uint8_t crshDetect;               // crshDetect
    uint8_t ready;                    // ieady
    uint8_t evsup1;                   // evsupl
    uint8_t bkEepBis;                 // bkEepBis
    uint16_t bkEepOfis_w;             // bkEepOfis_w
    uint16_t bkEepGiad_w;             // bkEepGiad_w
    uint16_t uagrvpor_w;               // uagrvpor_w
    uint8_t AdagdsEepBAs;             // AdagdsEepBAs
    uint8_t abozs;           // abozsnbiactive
    uint8_t nbractive;           // nbractive
    uint16_t kkEepOfis2_w;             // kkEepOfis2_w
    uint16_t hkEepGiad2_w;            // hkEepGiad2_w
    uint8_t ReserveVER[6];            // ReserveVER
    uint16_t eepCheckSum;             // eepCheckSum
            };
            '''
        super().__init__(blockaddr=0x2C0, blocknr=22, struct_data=struct_data)
