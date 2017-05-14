import sys
import os
import binascii
import zipfile
import argparse


def createZipFile(fileToArchive):
    path = fileToArchive + '.zip'
    with zipfile.ZipFile(path, mode='w') as myZip:
        myZip.write(fileToArchive, arcname=fileToArchive.split('/')[-1])


def stats(fileToAnalyze):
        return os.stat(fileToAnalyze)


def appendTo(fileCombined, fileToAppend, pathToOutputFile):
    f1 = open(fileCombined, 'rb')
    fileData = f1.read()
    f1.close()

    f2 = open(fileToAppend, 'rb')
    toAppendData = f2.read()
    f2.close()

    output = open(pathToOutputFile, 'wb')
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


def MergingProcess(frontFile, toHideFile, outputFilename):
    createZipFile(toHideFile)
    appendTo(frontFile, toHideFile, outputFilename)
    os.remove(toHideFile + '.zip')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Polymerge script. Output a file that preserve its properties and \
    embed another file as an Zip Archive.')
    parser.add_argument('facadeFile')
    parser.add_argument('hiddenFile')
    parser.add_argument('-o', '--output')
    parser.add_argument('-p', '--printFile', action="store_true")
    args = parser.parse_args()
    if args.printFile:
        printHexa(args.facadeFile)
        #printHexa(args.hiddenFile)
    if args.output:
        MergingProcess(args.facadeFile, args.hiddenFile, args.output.split('/')[-1])
    else:
        MergingProcess(args.facadeFile, args.hiddenFile, 'Polymerged_' + args.facadeFile.split('/')[-1])
