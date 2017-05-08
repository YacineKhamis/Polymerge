"""Polymerge tool."""
from Test import Functions
import sys

if __name__ == '__main__':
    print(Functions.test())

    # First experiments with basic Python functions
    b01 = Functions.createBytes(2)
    Functions.printInfo(b01)

    b02 = Functions.createBytes(255)
    Functions.printInfo(b02)

    i = 16
    # Create four bytes from the integer
    four_bytes = i.to_bytes(4, byteorder='big', signed=True)
    Functions.printInfo(four_bytes)

    # Compare the difference to little endian
    Functions.printInfo(i.to_bytes(4, byteorder='little', signed=True))

    # Play around with hexadecimal data
    hexaData = Functions.b.hexlify(b'\x00\xff')
    Functions.printInfo(hexaData)

    # Trying to open a file and print its content in binary mode
    with open(sys.argv[1], 'rb') as file:
        firstFourBytes = file.read(4)

    Functions.printInfo(firstFourBytes)
