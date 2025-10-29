#include <iostream>
#include <string>
using namespace std;

int main() {
    string choice1, choice2;
    char playAgain;

    do {
        cout << "Player 1: Choose rock, paper, or scissors: ";
        cin >> choice1;

        cout << "Player 2: Choose rock, paper, or scissors: ";
        cin >> choice2;

        // Convert both inputs to lowercase for consistency
        for (auto &c : choice1) c = tolower(c);
        for (auto &c : choice2) c = tolower(c);

        // Compare choices
        if (choice1 == choice2) {
            cout << "It's a tie!" << endl;
        }
        else if ((choice1 == "rock" && choice2 == "scissors") ||
                 (choice1 == "paper" && choice2 == "rock") ||
                 (choice1 == "scissors" && choice2 == "paper")) {
            cout << "Player 1 wins!" << endl;
        }
        else if ((choice2 == "rock" && choice1 == "scissors") ||
                 (choice2 == "paper" && choice1 == "rock") ||
                 (choice2 == "scissors" && choice1 == "paper")) {
            cout << "Player 2 wins!" << endl;
        }
        else {
            cout << "Invalid input! Please choose rock, paper, or scissors." << endl;
        }

        cout << "\nDo you want to play again? (y/n): ";
        cin >> playAgain;
        cout << endl;

    } while (playAgain == 'y' || playAgain == 'Y');

    cout << "Thanks for playing! Goodbye" << endl;

    return 0;
}
