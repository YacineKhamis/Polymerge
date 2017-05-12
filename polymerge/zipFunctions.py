"""Create a zip archive from specified file."""
import zipfile


def createZipFile(fileToArchive):
    path = './tmp/' + fileToArchive + '.zip'
    with zipfile.ZipFile(path, mode='w') as myZip:
        myZip.write(fileToArchive)