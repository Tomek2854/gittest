/*
 * struktury.cpp
 * 

 * 
 */


#include <iostream>
#include <iomanip>

using namespace std;

//~struct osoba {
    //~char imie[20];
    //~char nazwisko[20];
    //~int wiek;
    
    
    
//~};

//~struct samochod {
    //~char marka[20];
    //~char kolor[20];
    //~int rocznik;
    
    
    
//~};

void wyswietlDane(osoba o) 
{
    cout << setw(20) << "Imie: " << o.imie << endl;
    cout << setw(20) << "Nazwisko: " << o.nazwisko << endl;
    cout << setw(20) << "Wiek: " << o.wiek << endl;
    
    
}
    
//~void wyswietlDane1(samochod s) 
//~{
    //~cout << setw(20) << "Marka: " << s.marka << endl;
    //~cout << setw(20) << "Kolor: " << s.kolor << endl;
    //~cout << setw(20) << "Rocznik: " << s.rocznik << endl;
    
    
//~}
void getOsoby(osoba t[], int ile){
    for(int i=0; i < ile ; i++){
    cout << "podaj imie: " ;
    cin >> t[i].imie;
    cout << "podaj nazwisko: " ;
    cin >> t[i].nazwisko;
    cout << "podaj wiek: " ;
    cin >> t[i].wiek ;
    
    
    }
}


void drukujOsoby(osoba t[], int ile){
    for(int i=0; i < ile ; i++){
    cout << "podaj imie: " ;
    cin >> t[i].imie;
    cout << "podaj nazwisko: " ;
    cin >> t[i].nazwisko;
    cout << "podaj wiek: " ;
    cin >> t[i].wiek ;
    
    
    }
}

int main(int argc, char **argv)
{
    //osoba uczen1;
    //cout << "podaj imie: " ;
    //cin >> uczen1.imie;
    //cout << "podaj nazwisko: " ;
    //cin >> uczen1.nazwisko;
    //cout << "podaj wiek: " ;
    //cin >> uczen1.wiek ;
	//wyswietlDane(uczen1);
    
        //~samochod auto1;
    //~cout << "podaj marke: " ;
    //~cin >> auto1.marka;
    //~cout << "podaj kolor: " ;
    //~cin >> auto1.kolor;
    //~cout << "podaj rocznik: " ;
    //~cin >> auto1.rocznik ;
	//~wyswietlDane1(auto1);
   
   
   
    int ile;
    cout << "Ile osob? "; cin >> ile ;
    osoba tb[ile];
    drukujOsoby(tb,3);
	return 0;
}

