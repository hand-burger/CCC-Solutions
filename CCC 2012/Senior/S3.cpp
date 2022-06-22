#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    // Get the user input
    int numberOfSensors;
    cin >> numberOfSensors;

    // Make it 1001 to avoid the offset
    int readings[1001];

    // clear the memory for the array
    // readings is used as a pointer to the array, 0 is what the memory is being filled with, and the size of readings is the size of the array in bytes
    memset(readings, 0, sizeof(readings));

    // Get the readings and store them in the array by incrementing them at the position of the reading
    for (int i = 0; i < numberOfSensors; i++)
    {
        int reading;
        cin >> reading;
        readings[reading]++;
    }
    
    int largest = 0;
    int secondLargest = 0;

    // Iterate through the array and find the largest and second largest
    for (int i = 0; i < 1001; i++)
    {
        if (readings[i] > largest)
        {
            largest = readings[i];
        }
        if (readings[i] > secondLargest && readings[i] < largest)
        {
            secondLargest = readings[i];
        }
    }

    int smallestLarge = 2000001;
    int largestLarge = 0;

    // Iterate through the array and find the smallest and largest large
    for (int i = 0; i < 1001; i++) 
    {
        if (readings[i] == largest && i < smallestLarge) {
            smallestLarge = i;
        }
        if (readings[i] == largest && i > largestLarge) {
            largestLarge = i;
        }
    }

    // Print the absolute difference
    if (smallestLarge != largestLarge)
    {
        cout << abs(largestLarge - smallestLarge) << endl;
    }
    // If the two largest readings are the same
    else
    {
        int smallestSecondLarge = 2000001;
        int largestSecondLarge = 0;

        // Iterate through the array and find the smallest and largest large
        for (int i = 0; i < 1001; i++) 
        {
            if (readings[i] == secondLargest and i < smallestSecondLarge) 
            {
                smallestSecondLarge = i;
            }
            if (readings[i] == secondLargest and i > largestSecondLarge) 
            {
                largestSecondLarge = i;
            }
        }

        // Print the absolute difference
        if (abs(largestLarge - largestSecondLarge) > abs(largestLarge - smallestSecondLarge)) 
        {
            cout <<abs(largestLarge - largestSecondLarge) << endl;
        }
        else 
        {
            cout <<abs(largestLarge - smallestSecondLarge) << endl;
        }
    }

    return 0;
}