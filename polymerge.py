"""Polymerge tool."""
import sys
from Test import Functions
from polymerge import zipFunctions, fileFunctions

if __name__ == '__main__':
    # file = zipFunctions.createZipFile(sys.argv[1])
    # print(fileFunctions.stats('./tmp/fakePublicKey.txt.zip'))
    # fileFunctions.printHexa(sys.argv[1])
    fileFunctions.printHexa('./tmp/special_image.zip')