yg6u6hby67
#!/usr/bin/env python
# -*- coding: utf-8 -*-



#~def main(args):
    #~return 0

#~if __name__ == '__main__':
    #~import sys
    #~sys.exit(main(sys.argv))
teraz=2016 # bieżacy rok
rok_pythona=1991  #rok powstania Pythona

imie = raw_input("Imie")
if len(imie.strip()) ==0 or not imie.isalpha():
    imie="Nieznajomy"
elif imie[0].islower():
    imie=[0].upper() + imie[1:]
wiek = raw_input("Ile masz lat?!")
if wiek.isdigit() and int(wiek) >= 18 and int(wiek) < 80:
    rok_urodzenia= teraz-int(wiek)
else:
    print "Błedny wiek!"
    wiek=0
    rok_urodzenia=teraz
wiek_pythona = teraz-rok_pythona


print "Czesc" , imie , "Jestem Python!"
print "Urodziles sie w %s roku:" % rok_urodzenia
print "Powstalem  w %s roku i mam %s lat." % (rok_pythona,wiek_pythona)

if wiek_pythona > int(wiek):
    print "Jestem starszy!"
elif wiek_pythona == int(wiek):
    print "Mamy tyle samo "
else:
    print "Jestem mlodszy!"
