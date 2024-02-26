from common.binary_file import read_binary_file
from src.blocks.block_calib import BlockCALIB

from src.blocks.block_cust import BlockFD_CUST
from src.blocks.block_dpfmeep import BlockDFPMEEP
from src.blocks.block_dve import BlockDVE
from src.blocks.block_fd import BlockFD
from src.blocks.block_prg import BlockPRG
from src.blocks.block_prgid import BlockPRGID
from src.blocks.block_reserved1 import BlockReserviert1
from src.blocks.block_reserved2 import BlockReserviert2
from src.blocks.block_reserved3 import BlockReserviert3
from src.blocks.block_sgid import BlockSGID
from src.blocks.block_tester import BlockTESTER
from src.blocks.block_ver import BlockVER
from src.blocks.empty_blocks import Block13, Block14, Block15, Block16, Block17, Block18, Block19, Block20, Block21
from src.crc import getChecksum

filename = "1K8907115L_0020_544417_Original_eeprom_no_vin.bin"
file = read_binary_file(filename)

# Define the classes as before...

# Create instances of each class in the order they appear in the data
blocks_array = [
    BlockFD(),
    BlockReserviert1(),
    BlockReserviert2(),
    BlockReserviert3(),
    BlockFD_CUST(),
    BlockSGID(),
    BlockDVE(),
    BlockTESTER(),
    BlockCALIB(),
    BlockDFPMEEP(),
    BlockPRGID(),
    BlockPRG(),
    BlockVER(),
    Block13(),
    Block14(),
    Block15(),
    Block16(),
    Block17(),
    Block18(),
    Block19(),
    Block20(),
    Block21()
]
# Printing out the instances
for block in blocks_array:
    # print(block.blockaddr, block.blocknr)

    print(block)
    block.parse(file)
    calc_checksum = getChecksum(block)
    block_checksum = block.parsed_data.eepCheckSum
    if calc_checksum != block_checksum:
        print(f"Checksum Blk: {hex(block_checksum)}. Checksum Calculated: {hex(calc_checksum)}")
    else:
        print("checksum ok!")
    print(block.parsed_data)
