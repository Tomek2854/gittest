/*
 * cos.cxx
 * 

 * 
 */


#include <iostream>



using namespace std;

int parzyste(int n) 
    
{
    int i;
    for (i=0 ; i<=n ; i+=2) 
  
    cout << i << ""  ;
    
    return i/2;
}
int main(int argc, char **argv)
{
    int n ;
    char imie[100] ;
    int wiek=0;
    cout << "Podaj imie" << endl ;
    cin >> imie;
    cout << "Podaj wiek" << endl ;
    cin >> wiek;
    cout << "Witaj " << imie  << " urodziles/as sie w " << 2017-wiek << " roku" <<  endl ;
    if (wiek < 34 ) 
    {
    cout << "Jestem starszy" << endl ;
}
    else if (wiek > 34 ) 
    {
    cout << "Jestem mlodszy" << endl ;
}
    else if ( wiek == 34) 
    {
    cout << "Mamy syle samo lat" << endl ;
}
    cout << "podaj liczbe " << endl;
    cin >> n ;
    cout << "parzystych " << parzyste(n) << endl;
    

	
	
	return 0;
}

