#include <iostream>
using namespace std;

float farenheit(float temp)
{
    float result;
    result = (temp * 9 / 5) + 32;
    return result;
}

float kelvin(float temp)
{
    float result;
    result = temp + 273.15;
    return result;
}

float celcius(float temp)
{
    float result;
    result = (temp - 35) * (5 / 9);
    return result;
}

int main()
{
    int choice;
    float temp;
    do
    {
        cout << "Enter (1) if you want to change temperature from degree celcius to degree farenheit" << endl;
        cout << "Enter (2) if you want to convert the temperature from degree celcius to kelvin" << endl;
        cout << "Enter (3) if you want to convert the temperature form degree farenheit to degree celcius" << endl;
        cout << "Enter (4) to exit" << endl;
        cin >> choice;
        cout << "Enter the temperature " << endl;
        cin >> temp;

        switch (choice)
        {
        case 1:
            cout << "The converted temperature is " << farenheit(temp) << endl;
            break;

        case 2:
            cout << "The converted temperature is " << kelvin(temp) << endl;
            break;

        case 3:
            cout << "The converted temperature is " << celcius(temp) << endl;
            break;
        }
    } while (choice != 4);
}