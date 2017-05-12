import binascii as b

def test():
    return ("Hello world !")


def createBytes(n):
    return bytes(n)


def printInfo(obj):
    print(type(obj))
    print(obj)

    # print(Functions.test())

    # # First experiments with basic Python functions
    # b01 = Functions.createBytes(2)
    # Functions.printInfo(b01)
    #
    # b02 = Functions.createBytes(255)
    # Functions.printInfo(b02)
    #
    # i = 16
    # # Create four bytes from the integer
    # four_bytes = i.to_bytes(4, byteorder='big', signed=True)
    # Functions.printInfo(four_bytes)
    #
    # # Compare the difference to little endian
    # Functions.printInfo(i.to_bytes(4, byteorder='little', signed=True))
    #
    # # Play around with hexadecimal data
    # hexaData = Functions.b.hexlify(b'\x00\xff')
    # Functions.printInfo(hexaData)
    #
    # # Trying to open a file and print its content in binary mode
    # with open(sys.argv[1], 'rb') as file:
    #     firstFourBytes = file.read(4)
    #
    # Functions.printInfo(firstFourBytes)
    # path = './tmp/' + sys.argv[1] + '.zip'
    # print('creating archive')
    # with zipfile.ZipFile(path, mode='w') as myZip:
    #     myZip.write(sys.argv[1])
    #
    # jpg_file = open(sys.argv[2], 'rb')  # Path to JPEG
    # jpg_data = jpg_file.read()
    # jpg_file.close()
    #
    # # And the zip file to embed in the jpeg
    # zip_file = open('./tmp/test.zip', 'rb')  # Path to ZIP file
    # zip_data = zip_file.read()
    # zip_file.close()
    #
    # # Combine the files
    # out_file = open('./tmp/special_image.jpg', 'wb')  # Output file
    # out_file.write(jpg_data)
    # out_file.write(zip_data)
    # out_file.close()

    # INTERESTING : The zip file seems to be invalid
