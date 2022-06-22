#include <iostream>
#include <stack>

using namespace std;

int main()
{
    // Get user input

    int numberOfInts = 0;
    cin >> numberOfInts;

    stack<int> stackOfInts;

    int sum = 0;

    // Get each int
    for (int i = 0; i < numberOfInts; i++)
    {
        int integer = 0;
        cin >> integer;

        // If the integer is not zero
        if (integer)
        {
            // Add the integer to the sum
            sum += integer;

            // Add the int to stack
            stackOfInts.push(integer);
        }
        // If the integer is zero
        else
        {
            // Subtract the last int from sum
            sum -= stackOfInts.top();

            // Remove the int from stack after using it
            stackOfInts.pop();
        }
    }
    
    // Print the sum
    cout << sum << endl;

    return 0;
}