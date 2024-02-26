from src.blocks.abstract_block import AbstractBlock


class BlockTESTER(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
    uint16_t eepVersion;           // Element eepVersion
    char WSC[6];                 // Werkstattcode
    uint8_t coding2[4];             // Codierung2
    uint16_t pmc_w;                // Variantencodierung
    char pme[8];                   // Variantencodierung lang
    uint16_t csvklcw_w;            // Checks, für Überw. lange
    char ReserveTESTER[5];         // ReserveTESTER
    uint8_t eepCounter;            // Plausibilisierung Doppelablage
    uint16_t eepCheckSum;          // Checksumme
            };
            '''
        super().__init__(blockaddr=0x180, blocknr=12, struct_data=struct_data)
