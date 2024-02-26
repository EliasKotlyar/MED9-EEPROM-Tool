from src.blocks.abstract_block import AbstractBlock

class BlockCALIB(AbstractBlock):
    def __init__(self):
        struct_data = '''
struct block {
    uint16_t eepVersion;            // Element Blockversionsnummer
    uint8_t nls_ap;                 // %LRRNS
    uint8_t fba_ap;                 // %ESUK
    uint8_t fva_ap;                 // %ESUK
    uint8_t fns_ap;                 // %ESNSWL
    uint8_t fwl_ap;                 // %ESNSWL
    uint8_t flr_ap;                 // %LR
    uint8_t vvr_ap;                 // %VMAXMD
    uint8_t fst_ap;                 // %ESSTT
    uint8_t dzw_ap;                 // %ZUE
    uint8_t frk_ap;                 // %ESGRU
    uint8_t agr_ap;                 // %BBAGR
    uint8_t rix_ap;                 // %LDRLMX
    uint8_t cns_ap;                 // %LLRNS
    uint8_t mdr_ap;                 // %LLRMR
    uint8_t ReserveCALIB[13];
    uint8_t eepCounter;            // Plausibilisierung Doppelablage
    uint16_t eepCheckSum;           // Checksumme
};
            '''
        super().__init__(blockaddr=0x1C0, blocknr=14, struct_data=struct_data)