#include <iostream>
#include <cmath> // For pow()

using namespace std;

// Original image
int crystalArray[5][5] = {
    {0, 1, 1, 1, 0},
    {0, 2, 1, 2, 0},
    {0, 0, 2, 0, 0},
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0},
};

bool crystal(int magnificationLevel, int xPos, int yPos)
{

    // Grid size is 5^magnificationLevel
    int checkX, checkY;
    checkX = xPos / pow(5, magnificationLevel - 1);
    checkY = yPos / pow(5, magnificationLevel - 1);

    // Check if the crystal is in the grid
    // Base case
    if (crystalArray[checkY][checkX] != 2)
    {
        return crystalArray[checkY][checkX];
    }


    // Decrement the magnification level and check again
    return crystal(magnificationLevel - 1, xPos % (int)(pow(5, magnificationLevel - 1)), yPos % (int)(pow(5, magnificationLevel - 1)));
    
}

int main()
{
    // Get the number of test cases
    int numberOfCases;

    cin >> numberOfCases;

    // Loop over each test case
    for (int i = 0; i < numberOfCases; i++)
    {
        // Get the magnification level, x and y positions
        int magnificationLevel;
        int xPos, yPos;
        cin >> magnificationLevel >> xPos >> yPos;

        // Print the result
        if (crystal(magnificationLevel, xPos, yPos))
        {
            cout << "crystal" << endl;
        }
        else
        {
            cout << "empty" << endl;
        }
    }
    return 0;
}