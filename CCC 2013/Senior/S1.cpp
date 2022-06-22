#include <iostream>
#include <string>

using namespace std;

bool distinct(int year)
{
    string yearToString = to_string(year);
    
    // Check if the year is distinct
    for (size_t i = 0; i < yearToString.length(); i++)
    {
        for (size_t j = i + 1; j < yearToString.length(); j++)
        {
            // If the digits are the same, return false
            if (yearToString[i] == yearToString[j])
            {
                return false;
            }
        }
    }

    // If it reaches the end of the loop, it is distinct
    return true;
}

int main()
{
    // Get the user input
    int year;
    cin >> year;
    
    // While the year is not distinct, keep checking the next year until it is
    while (!distinct(++year)){}
    
    cout << year << endl;

    return 0;
}