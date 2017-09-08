#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#  
#  
ROK_TERAZ = 2017
ROK_CPP = 1991

def parzyste(n):
    ile =list(range(0,n+1,2))
    print(ile)
    return len(ile)
    
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
        
    n =int(input("Podaj liczbę:"))   
    print("Parzystych:", parzyste (n)) 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
