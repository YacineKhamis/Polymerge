import sys
import os
import binascii
import zipfile


def createZipFile(fileToArchive):
    path = fileToArchive + '.zip'
    with zipfile.ZipFile(path, mode='w') as myZip:
        myZip.write(fileToArchive, arcname=fileToArchive.split('/')[-1])


def stats(fileToAnalyze):
        return os.stat(fileToAnalyze)


def appendTo(fileCombined, fileToAppend):
    f1 = open(fileCombined, 'rb')
    fileData = f1.read()
    f1.close()

    f2 = open(fileToAppend, 'rb')
    toAppendData = f2.read()
    f2.close()

    pathToOuputFile = 'Polymerged_' + fileCombined.split('/')[-1]
    output = open(pathToOuputFile, 'wb')
    output.write(fileData)
    output.write(toAppendData)
    output.close()


def printHexa(fileToRead):
    """
    Print the content of the file passed in parameter in a user friendly flavor./
    View inspired from modern hexa editor : numbered lines each containing 16 bytes.
    """

    with open(fileToRead, 'rb') as binFile:
        binFile.seek(0, 2)
        numberBytes = binFile.tell()

        j = 0
        print('')
        print('_____________________________________________________________')
        for i in range(numberBytes):
            if i % 16 == 0:
                print('')
                j += 1
                print(format(j, '02X') + " : ", end='')
            binFile.seek(i, 0)
            data = binFile.read(1)
            text = binascii.hexlify(data)
            print(text.decode('utf-8'), end=' ')
    print('')
    print('__________________________________________________________________')


if __name__ == '__main__':
    createZipFile(sys.argv[2])
    appendTo(sys.argv[1], sys.argv[2] + '.zip')
    os.remove(sys.argv[2] + '.zip')
    print('DONE')
