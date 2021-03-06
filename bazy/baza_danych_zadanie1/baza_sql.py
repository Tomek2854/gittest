#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza_sql.py

import sqlite3
from dane import *  # import unkcji 


def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor() # utworzenie kursora
    
    # utworzenie tabel w bazie danych
    with open('pracownicy_z1.sql', 'r') as plik:
        skrypt = plik.read()
        cur.executescript(skrypt)
        
    premia =dane_z_pliku('premia.txt')
    premia = wyczysc_dane(premia, 1)
    
    dzial = dane_z_pliku('dział.txt')
    
    pracownicy = dane_z_pliku('pracownicy.txt')
    pracownicy = wyczysc_dane(pracownicy, 5)
    
    print (pracownicy[1])
    cur.executemany('INSERT INTO premia VALUES (?, ?)', premia)
    cur.executemany('INSERT INTO dzial VALUES (?, ?, ?)', dzial)
    cur.executemany('INSERT INTO pracownicy (id , nazwisko, imie, stanowisko, data_zatr , placa, id_dzial) VALUES (?, ?, ?, ?, ?, ?, ?)', pracownicy)
    
    con. commit() # zatwierdzenie opcji na bazie
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
