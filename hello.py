#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#  
#  
ROK_TERAZ = 2017
ROK_CPP = 1991

def main(args):
    imie = input("Jak masz na imie  ")
    print ("Czesc" , imie)
    wiek = int( input("Ile masz lat? "))
    print ("urodziles/as sie w ", 2017- wiek,"roku" )
    if ROK_CPP  > wiek:
        print ("Jestem starszy!")
    elif ROK_CPP  == wiek:
        print ("Mamy tyle samo ")
    else:
        print ("Jestem mlodszy!")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
