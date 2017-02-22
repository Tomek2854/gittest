#!/usr/bin/env python
# -*- coding: utf-8 -*-

def silnia(liczba):
    wynik=1
    for i in range (1,liczba+1):
        wynik=wynik*i
    return wynik

def silnia_rek(n):
    if (n==0):
        return 1

    return sil_rek(n-1)* n




def main(args):
    liczba=0
    liczba=int(raw_input("Podaj liczbe: "))
    print "Silnia:" ,silnia(liczba)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
