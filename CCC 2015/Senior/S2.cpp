#include <iostream>

using namespace std;

int arr[1000001];

int main()
{
    // Get user input
    int numberOfJerseys = 0;
    int numberOfAthletes = 0;

    cin >> numberOfJerseys >> numberOfAthletes;

    // Sizes
    char size;
    int sizeInt;

    // Requested jersey number
    int jerseyNumber = 0;

    // Fulfilled jerseys
    int total = 0;

    // Get each athlete
    for (int i = 0; i < numberOfJerseys; i++)
    {
        cin >> size;

        if (size == 'S')
        {
            sizeInt = 1;
        }
        else if (size == 'M')
        {
            sizeInt = 2;
        }
        else
        {
            sizeInt = 3;
        }
        
        // Get the size for each player
        arr[i + 1] = sizeInt;
    }
    
    for (int i = 0; i < numberOfAthletes; i++)
    {   
        // Get the requested jersey number and size
        cin >> size >> jerseyNumber;

        if (size == 'S')
        {
            sizeInt = 1;
        }
        else if (size == 'M')
        {
            sizeInt = 2;
        }
        else
        {
            sizeInt = 3;
        }

        // If the person with that jersey number has a size that is good or bigger than what they requested
        if (arr[jerseyNumber] >= sizeInt)
        {
            total++;
            arr[jerseyNumber] = 0;
        }
        
    }
    
    cout << total << endl;

    return 0;
}