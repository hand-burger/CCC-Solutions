#include <iostream>
#include <algorithm>
#include  <iomanip> // setprecision

using namespace std;

int main()
{
    // Get user input

    int numberOfVillages = 0;
    cin >> numberOfVillages;

    int villagePositions[numberOfVillages];

    for (int i = 0; i < numberOfVillages; i++)
    {
        cin >> villagePositions[i];
    }

    double answer = 2e9;

    // Sort the village positions
    sort(villagePositions, villagePositions + numberOfVillages);

    // Find the smallest size of neighborhood
    for (int i = 1; i < numberOfVillages - 1; i++)
    {
        answer = min(answer, (double)(villagePositions[i + 1] - villagePositions[i - 1]) / 2.0);
    }
    
    // Print the answer with precision of 1 decimal place
    cout << fixed << setprecision(1) << answer << endl;

    return 0;
}