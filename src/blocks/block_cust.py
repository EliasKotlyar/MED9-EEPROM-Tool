from src.blocks.abstract_block import AbstractBlock


class BlockFD_CUST(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
    uint16_t eepVersion;        // Element eepVersion
    char HWID[4];               // Hardwarekennung für Familie, Variante, Version
    char HstWrkKz[6];           // Herstellerwerkskennzahl und Kennzeichnung
    char TgsFrtgDat[3];         // Tages-Fertigungsdatum
    char HstPrfstNr[4];         // Hersteller-Prüfst.-Nr.
    char HstLfdNr[4];           // Laufende Hersteller-Nr.
    char ReserveFDCUST[7];      // ReserveFDCUST
    uint16_t eepCheckSum;       // Checksumme
            };
            '''
        super().__init__(blockaddr=0x120, blocknr=9,struct_data=struct_data)