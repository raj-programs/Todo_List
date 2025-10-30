#include <iostream>
using namespace std;

bool leapYear(int year)
{   
    if (year % 400 == 0)
    {
        return true;
    }
    else if (year % 100 == 0)
    {
        return false;
    }
    else if (year % 4 == 0)
    {
        return true;
    }
    return false;
}

int main()
{
    int year;
    cout << "Enter the Year to check : " << endl;
    cin >> year;
    if (leapYear(year))
    {
        cout << "The " << year << " is a leap year!" << endl;
    }
    else
    {
        cout << "The " << year << "is not a leap year!" << endl;
    }
    return 0;
}