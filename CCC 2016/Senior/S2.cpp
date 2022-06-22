#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    // Get user input
    int question = 0;
    int numberOfSpeeds = 0;

    cin >> question >> numberOfSpeeds;

    int dmoj[numberOfSpeeds];
    int peg[numberOfSpeeds];

    int maxSpeed = 0;

    for (int i = 0; i < numberOfSpeeds; i++)
    {
        cin >> dmoj[i];
    }
    
    for (int i = 0; i < numberOfSpeeds; i++)
    {
        cin >> peg[i];
    }

    // Now check which question it is

    if (question == 1)
    {
        // Question 1
        // Find the minimum speed
        sort(dmoj, dmoj + numberOfSpeeds, greater<int>());
        sort(peg, peg + numberOfSpeeds, greater<int>());

        for (int i = 0; i < numberOfSpeeds; i++)
        {
            maxSpeed += max(dmoj[i], peg[i]);
        }
        
    }
    else
    {
        // Question 2
        // Find the maximum speed
        sort(dmoj, dmoj + numberOfSpeeds);
        sort(peg, peg + numberOfSpeeds, greater<int>());

        for (int i = 0; i < numberOfSpeeds; i++)
        {
            maxSpeed += max(dmoj[i], peg[i]);
        }
    }

    // Print the result
    cout << maxSpeed << endl;

    return 0;
}