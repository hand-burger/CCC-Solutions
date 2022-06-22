#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // Get user input

    int numberOfRuns = 0;
    cin >> numberOfRuns;

    // Holds the number of runs for each team
    vector<int> team1(numberOfRuns);
    vector<int> team2(numberOfRuns);

    // Loop over and get each run
    for (int i = 0; i < numberOfRuns; i++)
    {
        int num;
        cin >> num;
        team1[i] = num;
    }

    for (int i = 0; i < numberOfRuns; i++)
    {
        int num;
        cin >> num;
        team2[i] = num;
    }


    // Now find the max score
    int maxScore = 0;
    int score1 = 0, score2 = 0;

    // Loop over each run for each day and add to the score
    for (int i = 0; i < numberOfRuns; i++)
    {
        score1 += team1[i];
        score2 += team2[i];
        
        // If the score is ever the same then we have a winner
        if (score1 == score2)
        {
            // Add 1 because offset
            maxScore = i + i;
        }
    }
    
    // Print the max score
    cout << maxScore << endl;

    return 0;
}