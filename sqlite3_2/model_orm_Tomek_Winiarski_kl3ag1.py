# -*- coding: utf-8 -*-

from peewee import *


baza_plik = "szkola.db"
baza = SqliteDatabase(baza_plik)  # ':memory:'


class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza


class klasa(BazaModel):
    klasa = CharField(null=False)
    rok_naboru = IntegerField(null=False)
    rok_matury = IntegerField(null=False)

    def _str_(self):
        return self.nazwa

class ocena(BazaModel):
    datad = DateField(null=False)
    uczen_id = IntegerField(null=False)
    przedmiot_id = IntegerField(null=False)
    ocena = DecimalField(decimal_places=2, default=0)
    uczen_id = ForeignKeyField(uczen, related_name='id')
    przedmiot_id = ForeignKeyField(przedmiot, related_name='id')



class przedmiot(BazaModel):
    nazwa= CharField(null=False)
    imien = CharField(null=False)
    nazwiskon = CharField(null=False)
    plecn = IntegerField(null=False)



class uczen(BazaModel):
    imie = CharField()
    nazwisko = CharField()
    plec = IntegerField()
    klasa_id  = IntegerField(null=False)
    egzhum= IntegerField(null=False, default=0)
    egzmat= IntegerField(null=False, default=0)
    egzjez= IntegerField(null=False, default=0)
    klasa_id = ForeignKeyField(klasa, related_name='id')

def kwerenda_a():
    query = (uczen
            .select(uczen.imie,uczen.nazwisko,)
            )
    for obj in query:
                print(obj.imie,obj.nazwisko)



baza.connect()  # nawiązujemy połączenie z bazą
