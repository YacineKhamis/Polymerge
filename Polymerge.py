#Polymerge
#
#
#AIDE
#https://github.com/jsharf/shibboleth
#PDF 101 & PDF Secrets https://www.youtube.com/watch?v=nYZ72LvphBI
#Ange albertini en Francais ! : https://www.youtube.com/watch?v=iIesDpv9F4s&index=13&list=PL2-EpKoPE60Uyi5X6NMeiROVi8hm33sW3

import getopt
import sys

def main():

    try:
        opts, args = getopt.getopt(sys.argv, "d", "debug")
    except getopt.GetoptError:
        print('Polymerge.py [-d | --debug] <file>')
        sys.exit(1)

    print ("Ouverture de " + args[1])
    with open(args[1], 'rb') as file :
        char = file.read(1)
        i = 0
        while(i < 64):
            if(i%10 == 0):
                print(' ', ' ')
            print(char, ' ', '')
            char = file.read(1)
            i += 1

if __name__ == "__main__":
  main()