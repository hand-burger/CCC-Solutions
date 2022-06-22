#include <iostream>
#include <string>

using namespace std;

// Convert roman numerals to decimal
int eval(char ch)
{
    if(ch == 'I') return 1;
    else if(ch == 'V') return 5;
    else if(ch == 'X') return 10;
    else if(ch == 'L') return 50;
    else if(ch == 'C') return 100;
    else if(ch == 'D') return 500;
    else if(ch == 'M') return 1000;
}

int main()
{
    // Get the user input
    string input;
    cin >> input;

    // Decimal value of the aromatic number
    int decimalValue = 0;

    // Use this to check if the previous character was a smaller value
    int previousDecimalValue = -1;

    // Iterate through the string
    // It checks every other character in the string because it goes by pairs
    for (int i = input.length() - 1; i >= 0; i -= 2)
    {
        // Get the current character
        int currentChar = input[i - 1] - '0';

        // Convert it to decimal
        int toDecimal = eval(input[i]);

        // If the previous character was a smaller value, subtract it from the current value
        if (toDecimal < previousDecimalValue)
        {
            decimalValue -= currentChar * toDecimal;
        }

        // Otherwise, add it to the current value
        else
        {
            decimalValue += currentChar * toDecimal;
        }

        // Store the current value to compare it to the next one
        previousDecimalValue = toDecimal;
    }
    
    // Print the result
    cout << decimalValue << endl;

    return 0;
}