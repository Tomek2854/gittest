#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#  MA 02110-1301, USA.
#  
import sqlite3
 
def kw_c(cur):
    cur.execute("""
        SELECT siedziba , sum(placa) AS pensje
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial=dzial.id
        GROUP BY siedziba
        ORDER BY pensje ASC
    """)
    wyniki=cur.fetchall() #pobierz wszystkie wiersze 
    for row in wyniki:
        print (tuple(row))


def kw_d():




def main(args):
        
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor() # utworzenie kursora
    con.row_factory =sqlite3.Row
    
    kw_c(cur)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
