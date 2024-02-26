from dissect import cstruct


class AbstractBlock:
    def __init__(self, blockaddr: int, blocknr: int, struct_data: str = ""):
        self.blockaddr = blockaddr
        self.blocknr = blocknr
        self.cparser = cstruct.cstruct(endian='>')
        self.cparser.load(struct_data)
        self.block_len = self.cparser.typedefs["block"].size

    def parse(self, data: bytes):
        self.rawdata = data[self.blockaddr:self.blockaddr + self.block_len]
        self.parsed_data = self.cparser.block(self.rawdata)

    def __repr__(self):
        return self.__class__.__name__
