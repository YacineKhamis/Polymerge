"""Contain utility functions that help handling files."""
import os
import binascii


def stats(fileToAnalyze):
        return os.stat(fileToAnalyze)

def printHexa(fileToRead):
    """
    Print the content of the file passed in parameter in a user friendly flavor./
    View inspired from modern hexa editor : numbered lines each containing 16 bytes.
    """
    #try:
    with open(fileToRead, 'rb') as binFile:
        binFile.seek(0, 2)
        numberBytes = binFile.tell()

        j = 0
        for i in range(numberBytes):
            if i % 16 == 0:
                print('')
                j += 1
                print(format(j, '02X') + " : ", end='')
            binFile.seek(i, 0)
            data = binFile.read(1)
            text = binascii.hexlify(data)
            print(text.decode('utf-8'), end=' ')
    #except OSError as e:
    #    print(e)
