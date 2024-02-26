from src.blocks.abstract_block import AbstractBlock


class BlockFD_CUST(AbstractBlock):
    def __init__(self):
        struct_data = '''
            struct block {
        uint8_t dProductProgress_u8[5];    // Element dProductProgress_u8 - Fertigungsfortschritt
        uint16_t dTswContVer_u16;          // Element dTswContVer - 2
        uint8_t dProdDateOne_u8[8];        // Element dProdDateOne - Fertigungsdatum1
        uint8_t dCsPdOne_u8;               // Element dCsPdOne - Checksumme Fertigungsdatum'
        uint16_t dTswContVerCp_u16;        // Element dTswContVerCp - 2
        uint8_t dProdDateTwo_u8[8];        // Element dProdDateTwo - Fertigungsdatum2
        uint8_t numSerial_u8[12];          // Element numSerial - Seriennummer
        uint8_t numDswCont_u8[10];         // Element numDswCont - SW-Containemummer
        uint8_t dHwLevel_u8;               // Element dHwLevel - HW-Stand
        uint8_t dLpLevel_u8;               // Element dLpLevel - LP-Stand
        uint8_t stFswMarker_u8[2];         // Element stFswMarker - Footprint der Fahrsoftware
        uint8_t dReserved_u8[10];
        uint16_t eepCheckSum;              // Element eepCheckSum - Checksumme
            };
            '''
        super().__init__(blockaddr=120, blocknr=9,struct_data=struct_data)