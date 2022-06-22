#include <iostream>

using namespace std;

int main()
{
    // Get user input
    int numberOfFriends = 0;
    int numberOfRounds = 0;

    cin >> numberOfFriends >> numberOfRounds;

    int listOfFriends[numberOfFriends + 1];

    // Initialize list of friends
    for (int i = 0; i <= numberOfFriends; i++)
    {
        listOfFriends[i] = i;
    }
    
    // Perform the rounds
    for (int i = 0; i < numberOfRounds; i++)
    {
        // Get the index of friends to be removed
        int round;
        cin >> round;

        int j = 0;
        for (int i = 1; i <= numberOfFriends; i++)
        {
            if (listOfFriends[i])
            {
                j++;
            }
            // If the current friend is the round, remove it
            if (j % round == 0)
            {
                listOfFriends[i] = 0;
            }
            
        }
        
    }
    
    // Print the remaining friends
    for (int i = 1; i <= numberOfFriends; i++)
    {
        if (listOfFriends[i])
        {
            cout << i << endl;
        }
    }

    return 0;
}