//Name: Nava Karine Nizard
//Email: nava.nizard12@myhunter.cuny.edu
//Date: December 4, 2024
//This program asks the user for the year until 2018 or earlier is entered.

#include <iostream>
using namespace std;

int main() {
    cout << "Enter year: ";
    int year;
    cin >> year;

    while(year > 2018) {
        cout << "Year must be 2018 or earlier.\n";
        cout << "Enter year: ";
        cin >> year;
    }

    cout << "You entered " << year;

    return 0;
}
