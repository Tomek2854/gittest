#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#  
#  
from peewee importb *

baza_plik = 'pracownicy.sqlite3'
baza = SQliteDatabase(baza_plik)

class BazaModel(Model):
    class Meta:
        datbase = baza

class Premia(BazaModel):
    id = CharField(primary_kay=True)
    premia = DecimalField()
    
class Dzial(BazaModel):
    id = IntegerField(primary_kay=True)
    nazwa = CharField()
    siedziba = CharField()
    
class Pracownik(BazaModel):
    id = CharField(primary_kay=True)
    nazwisko = CharField()
    imie = CharField()
    stanowisko = ForeigKey(Premia, related_name='pracownicy')
    dat_zatr = CharField()
    placa = DecimalField(decimal_places=2)
    premia = DecimalField(decimal_places=2, default=0)
    id_dzial = ForeignKey(Dzial, related_name='pracownicy')
    
baza.connect()
baza.create_tables([Premia,Dzial,Pracownik],True)

