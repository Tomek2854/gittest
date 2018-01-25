/*




 */


#include <iostream>

using namespace std;

bool size(int sr , sp){
    return true; //jesli jest miejsce na stosie
    return false; //gdy stos jest przepelniony
    
    }

void push(int stos[],int dane, int &sp){
    if (size(sr,sp)){
        stos[sp] = dane;
        ++sp;
    }else {
        
        }
    
}

int pop(int stos[],int sp){
    sp--;
    return stos[sp];
    
    }
int main(int argc, char **argv)
{
    int *stack;  //wskaznik
    int sr; // rozmiar stosu
    int sp = 0; // wskaznik pozycji na stosie
    
    cout << "podaj rozmiar: "; cin >> sr;
    stack = new int[sr];
    
    push(stack, 4 ,sp); // sp = 1 
    push(stack, 9 ,sp);  //sp = 2
    cout  << pop(stack,sp);
    push(stack,9,sp);
    cout  << pop(stack,sp);
    push(stack,7,sp);
    cout  << pop(stack,sp);

	return 0;
}

