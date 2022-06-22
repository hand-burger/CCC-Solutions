#include <iostream>
#include <stack>

using namespace std;

int main()
{
    // Get user input

    int tests = 0;
    cin >> tests;

    for (int i = 0; i < tests; i++)
    {
        int numberOfCars = 0;
        cin >> numberOfCars;

        int carArray[numberOfCars];

        // Initialize list of cars
        for (int j = 0; j < numberOfCars; j++)
        {
            cin >> carArray[j];
        }

        int needed = 1;
        stack<int> branch;

        for (int i = numberOfCars - 1; i >= 0; i--)
        {
            while (!branch.empty() && branch.top() == needed)
            {
                branch.pop();
                needed++;
            }
            if (carArray[i] == needed)
            {
                needed++;
            }
            else
            {
                branch.push(carArray[i]);
            }
        }
        while (!branch.empty())
        {
            if (needed == branch.top())
            {
                needed++;
                branch.pop();
            }
            else
            {
                break;
            }
        }

        // Print the output, if the recipe can be made or not
        if (needed > numberOfCars)
        {
            cout << 'Y' << endl;
        }
        else
        {
            cout << 'N' << endl;
        }
        
    }

    return 0;
}