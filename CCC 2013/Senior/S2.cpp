#include <iostream>

using namespace std;

int main()
{
    // Get the user input
    int maxWeight = 0;
    int numberOfCars = 0;

    cin >> maxWeight >> numberOfCars;

    // Weights of the cars
    int weights[100000];

    // Current weight of car
    int currentCar = 0;

    // Loop through the cars
    for (int i = 0; i < numberOfCars; i++)
    {
        // Get the weight of the car
        cin >> weights[i];

        // Only four cars can be loaded at once
        if (i >= 4)
        {
            // If more than four cars have been loaded, go back
            currentCar -= weights[i - 4];
        }

        // Add the weight of the car to the current weight
        currentCar += weights[i];

        // If the current weight is greater than the max weight, we cannot bring any railway cars across the bridge
        if (currentCar > maxWeight)
        {
            cout << i << endl;
            return 0;
        }
    }

    // If we reach this point, we can bring all the cars across the bridge
    // Print the number of cars
    cout << numberOfCars << endl;

    return 0;
}