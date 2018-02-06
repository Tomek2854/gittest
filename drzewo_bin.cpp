/*
 * drzewo_bin.cpp
 
 
 * 
 */

#include <iostream>

using namespace std;

struct Wezel {
    int wartosc;
    Wezel *lewy;
    Wezel *prawy;
} *korzen = NULL;  //definicja struktury i utworzenie wskaznika korzen (zadeklarowany globalnie) korzen stanie sie wlasnoscia prywatna

Wezel* stworzWezel(int wartosc) {
    Wezel *nowyWezel = new Wezel;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy = NULL;
    
    return nowyWezel;
}

void dodajWezel(Wezel *wezel,int wartosc){
    if (korzen == NULL){
        korzen = stworzWezel(wartosc);
    } else{
        if (wartosc < wezel -> wartosc) { //wstawiamy wartosc mniejsza
           if(wezel->lewy !=NULL) {
                dodajWezel(wezel->lewy); //rekurencyjne wywolanie dodawania  do lewego poddrzewa 
            } else { //lewy potomek nie istnieje
                wezel->lewy = stworzWezel(wartosc);  //tworzymy nowy wezel
            }
        } else{ // wstawiamy wartosc wieksza
            if(wezel->prawy !=NULL) {
                dodajWezel(wezel->prawy); //rekurencyjne wywolanie dodawania  do lewego poddrzewa 
            } else { //lewy potomek nie istnieje
                wezel->prawy = stworzWezel(wartosc);  //tworzymy nowy wezel
            }
        }
    }
}

int main(int argc, char **argv)
{
	
	return 0;
}

