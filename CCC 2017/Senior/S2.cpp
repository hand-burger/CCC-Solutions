#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    // Get user input
    int numberOfTides = 0;
    cin >> numberOfTides;

    // Holds the magnitude of the tides
    int tides[numberOfTides];

    // Loop over and get each tide
    for (int i = 0; i < numberOfTides; i++)
    {
        cin >> tides[i];
    }
    
    // Sort the tides
    sort(tides, tides + numberOfTides);

    int lowTide = 0;
    int highTide = 0;

    if (numberOfTides % 2 == 0)
    {
        lowTide = numberOfTides / 2 - 1;
        highTide = numberOfTides / 2;
    }
    if (numberOfTides % 2 == 1)
    {
        lowTide = floor(numberOfTides / 2.0);
        highTide = ceil(numberOfTides / 2.0);
    }

    for (; lowTide >= 0; lowTide--, highTide++)
    {
        cout << tides[lowTide] << " ";
        if (highTide < numberOfTides)
        {
            cout << tides[highTide] << " ";
        }
        
    }

    return 0;
}