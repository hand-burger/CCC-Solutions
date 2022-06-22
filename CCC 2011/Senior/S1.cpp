#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Read the number of lines
    int numberOfLines;

    // Current character
    char character;

    // Stores the number of t's and s's
    int t = 0, s = 0;

    // Read the number of lines
    for (cin >> numberOfLines; numberOfLines >= 0; numberOfLines--)
    {
        // Read the line
        while ((character = getchar()) != '\n' && character != EOF)
        {
            // Increment the number of t's and s's
            if (character == 't' || character == 'T')
            {
                t++;
            }
            else if (character == 's' || character == 'S')
            {
                s++;
            }
            
        }
        
    }

    // Determine the language and print it.
    string language;
    language =  (s >= t) ? "French" : "English";
    cout << language << endl;

    return 0;
}