# Polymerge

Polymerge is an open source based project created in order to answer some issues in the case of merging different files into one by using steganography techniques. (OpenPuff, for instance)

This tool is designed to merge two differents files of the same type into one file readeable for the both file by choosing the right application.

This project is currently being managed by students in IT Security from France 

Choosen file formats :
* .bmp : 
  * IrFanView Gets the data via the pointer
  * UniversalViewer Gets the data right after the header
* .zip :
  * Bottom-up parsing : 7-zip, Java Zipfile, Python zipfile, Unzip 6.00, Windiws 7 Explorer, WinRAR
  * Top-bottom parsing : PHP ZipArchive, PHP zip_open
  * Scanning for all Local File Headers : binwalk
