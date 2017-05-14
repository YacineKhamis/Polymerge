# Polymerge

Polymerge is a python script that enables both Windows and Linux users to append
a file to another in order to hide it from casual users (not used to IT Science)
while still making the first file usable as is.

The main issue about this project was about to make the hidden file usable without
having nor Python nor this script on the target computer. We really tried to figure
out how to make both files (of any type) still valid without having third-party
software already installed on the target computer. Thanks to Ange Albertini insights,
we discovered that some file format don't use Magic Number in order to be identified
as valid file type and still usable.

Unfortunatly, we didn't achieve our purpose that was to merge two file
(myDummyPdf.pdf and mySecretPGPKey.txt for e.g) and make one file from it that you
could open with either a pdf viewer or a plain-text editor and see one file or the other
according to the choosen app. We figure out that for many files types, that specific
kind of behavior is impossible without :

 * Using a program first (and often needing installation of third-party software as Python
   might be)
 * Merging two files of the same types but making a schyzophrenic from it (based
   on the fact that two different application will parse a file as the software is
   designed for and not always compliant to file format specs)

We decided to focus on the zip file format that is one of the rare file format that is
parsed Bottom-Top which means that programs that are designed to handle zip archive
start to look for them from the end of the file enabling then the opportunity to
put a first file that will be fully valid since having correct file header, content
and trails.

## Usage :

Very basic usage, assuming your first file will be a simple image file that will
contain a file that you don't want to be found onto your computer if you forget
to lock it for example or to deliver a hidden file to someone else but easily.
Having [Python 3.6] is necessary to execute the script in the first place using :
`py polymerge.py myImageFile.jpeg secretButNotTooMuch.pdf` and then you would find
 a new file called by default `Polymerged_myImageFile.jpeg`

### Options :

 * Change output file name using the `-o or --output fileName`
 * Just print the file passed in argument in a hexadecimal editor flavor using `-p or --print fileToPrint`

## Requirements :

As mentioned before, you only need a program that can extract a zip archive from
 a file. Though, on Windows you have to use your command prompt to extract the
 hidden file.  

### Windows users

Although Windows shell context is based on file extension (which is in fact only
the few characters that end a file name after the period) you can't use your
right click and select your favorite extract method. Even changing the extension
doesn't matter in fact because zip handling Windows softwares apply hardened verification
on the file ; 7zip or WinRar in GUI mode will tell you that the file is not valid.

But Unzip which is a free software can be found [here](http://stahlworks.com/dev/?tool=zipunzip) and used in Windows command
prompt using the command : `unzip.exe OutputFile.any` and find the file in the same folder.

## Credits :

We would like to thank Ange Albertini for his work on polyglot and funky format files !
https://kyleisom.net/downloads/pocorgtfo/pocorgtfo04.pdf - Page 42

Credits to the site http://www.devdungeon.com which provided us lot of Python examples !
