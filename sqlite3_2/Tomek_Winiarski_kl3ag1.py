# -*- coding: utf-8 -*-

from peewee import *


baza_plik = "szkola.db"
baza = SqliteDatabase(baza_plik)  # ':memory:'


class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza


class Klasa(BazaModel):
    id = IntegerField(primary_key=True)
    klasa = CharField(null=False)
    rok_naboru = IntegerField(null=False)
    rok_matury = IntegerField(null=False)

class Oceny(BazaModel):
    id = CharField(primary_key=True)
    Datad = DatetimeField(null=False)
    UczenID = IntegerField(null=False)
    PrzedmiotID = IntegerField(null=False)
    Ocena = DecimalField(null=False)
    UczenID = ForeignKeyField(tbUczniowie, related_name='IDUcznia')
    PrzemiotyID = ForeignKeyField(tbPrzedmioty, related_name='IDPrzedmiotu')
    


class Przedmioty(BazaModel):
    id = CharField(primary_key=True)
    Przedmiot= CharField(null=False)
    NazwiskoNaucz = CharField(null=False)
    ImieNaucz = CharField(null=False)
    PlecNaucz = IntegerField(null=False)
    
    
    
class Uczniowie(BazaModel):
    id = CharField(primary_key=True)
    imie = CharField()
    nazwisko = CharField()
    plec = IntegerField()
    KlasaID  = IntegerField(null=False)
    EgzHum= NumericField(null=False, default=0)
    EgzMat= NumericField(null=False, default=0)
    EgzJez= NumericField(null=False, default=0)
    premia = DecimalField(decimal_places=2, default=0)
    KlasaID = ForeignKeyField(tbKlasy, related_name='IDKlasy')


baza.connect()  # nawiązujemy połączenie z bazą


