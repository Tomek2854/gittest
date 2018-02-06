/*
 * lista.cpp
 * 

 * 
 * 
 */
#include <iostream>
#include "lista.hpp"

Lista::Lista(){
    head =NULL;
    tail =NULL;
}

Lista::~Lista(){
    while(Usun()) {;};
}

void Lista::Dodaj(int wartosc){
        ELEMENT *el = new ELEMENT;
        el->wartosc = wartosc;
        el->nast = NULL;
        if(head == NULL) {
            head = el;
            tail = el;
        } else {
            tail ->nast = el;   //ustawienie wskaznika nast dotychczasowego
            // ostatniego elementu na adres nowego ostatniego elementu
            tail = el; // aktualinujemy wskaznik ogon, aby wskazywal nowy element
        }
}
void Lista::Wyswietl() {
    ELEMENT *el = head;
    while (el != NULL){
        std::cout <<el->wartosc << " ";
        el =  el->nast;
    }
    std::cout << std::endl;
}

bool Lista::Usun(){
    if (head !=NULL) {
        if(head == tail) {
            delete head;
            head = NULL;
            tail = NULL;
        } else {
            ELEMENT *el = head;
            while(el->nast !=tail){ //szukam przedostatniego elementu
                el = el->nast; //zapis adresu przedostatniego elementu
            }
            delete el->nast;
            el->nast = NULL;
            tail = el;
        }
        return true;
    }
    return false;    
}

void Lista::Wstaw(int pozycja, int wartosc) {
        ; // co dalej -musi sprawdzic miejsce gdzie chcemy cos wstawic wstaw np(5,wartosc) funkcja dodaj(wartosc)
}
