#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spirala.py
#
import turtle

def spirala(bok,kat,przyrost,warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if kat< warunek:
        spirala(bok,kat+przyrost,przyrost,warunek)

def spirala2(bok,kat,warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if bok< warunek:
        spirala2(bok+3,kat,warunek)

def main(args):
   #spirala(120,20,106,6000)
    spirala2(21,45,3600)
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
