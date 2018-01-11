/*
 * wskazniki.cpp
 * 
 * Copyright 2018  <>
 * 
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int x = 11;
    cout << x << endl; // wartosc zmiennej
    cout << &x << endl;  // 0x oznacza wartosc szestnastkowa
    cout << * &x << endl;
	return 0;
}

