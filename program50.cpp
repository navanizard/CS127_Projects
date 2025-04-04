//Name: Nava Karine Nizard
//Email: nava.nizard12@myhunter.cuny.edu
//Date: December 4, 2024
//This program prints season greetings based on user input

#include <iostream>
using namespace std; 

int main() {
    cout << "Enter month (as a number): ";
    int year;
    cin >> year;

    if(year < 3 || year > 11) {
        cout << "Happy Winter";
    } else if(year >= 3 && year < 7) {
        cout << "Happy Spring";
    } else if(year >= 7 && year < 9) {
        cout << "Happy Summer";
    } else {
        cout << "Happy Fall";
    }

    return 0;
}
