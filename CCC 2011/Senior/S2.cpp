#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // Read the number of lines
    int numberOfLines;

    cin >> numberOfLines;

    // Current character
    vector<char> characters(numberOfLines);

    // Get the characters
    for (int i = 0; i < numberOfLines; i++)
    {
        cin >> characters[i];
    }

    // Stores the number of correct answers
    int correctAnswers = 0;

    // Check the answers
    for (int i = 0; i < numberOfLines; i++)
    {
        char c;
        cin >> c;
        correctAnswers += (c == characters[i]);
    }

    // Print the number of correct answers
    cout << correctAnswers << endl;

    return 0;
}