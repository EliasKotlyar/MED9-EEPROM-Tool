from src.blocks.abstract_block import AbstractBlock


class EmptyBlock(AbstractBlock):
    def __init__(self, blockaddr: int, blocknr: int):
        struct_data = '''
            struct block {
        uint16_t eepVersion;               // Element eepVersion
        uint8_t data[28]; 
        uint16_t eepCheckSum;              // Element eepCheckSum - Checksumme
            };
            '''
        super().__init__(blockaddr=blockaddr, blocknr=blocknr, struct_data=struct_data)


class Block13(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x2E0, blocknr=23)


class Block14(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x300, blocknr=24)


class Block15(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x320, blocknr=25)


class Block16(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x340, blocknr=26)


class Block17(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x360, blocknr=27)


class Block18(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x380, blocknr=28)


class Block19(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x03A0, blocknr=29)


class Block20(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x03C0, blocknr=30)


class Block21(EmptyBlock):
    def __init__(self):
        super().__init__(blockaddr=0x3E0, blocknr=31)
