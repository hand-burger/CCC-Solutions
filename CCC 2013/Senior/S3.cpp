#include <iostream>

using namespace std;

int games[4][4][2];
int scoring[3] = {3, 1, 0};
int answer = 0;

void chances(int favoriteTeam, int gamesLeft)
{
    // If there are no games left, we have found the answer
    if (gamesLeft == 0)
    {
        int teamScores[4] = {0, 0, 0, 0};

        // Loop through the games
        for (int i = 0; i < 3; i++)
        {
            for (int j = i + 1; j < 4; j++)
            {
                // Add the score of the favorite team to the team's score
                teamScores[i] += games[i][j][0];
                teamScores[j] += games[i][j][1];
            }
        }
        bool champ = true;
        // Check if the favorite team is the champion
        for (int i = 0; i < 4; i++)
        {
            if ((favoriteTeam - 1) == i)
            {
                continue;
            }
            if (teamScores[favoriteTeam - 1] <= teamScores[i])
            {
                champ = false;
            }
        }

        // If the favorite team is the champion, add it to the answer
        if (champ)
        {
            answer++;
        }
    }
    // If there's still more games
    else
    {
        bool firstFound = false;

        // Loop through the teams
        for (int i = 0; i < 3; i++)
        {
            for (int j = i + 1; j < 4; j++)
            {
                // If the game isn't played yet, play it
                if ((games[i][j][0] == 0) && (games[i][j][1] == 0))
                {
                    // Play the game
                    for (int k = 0; k < 3; k++)
                    {
                        // Find the score
                        games[i][j][0] += scoring[k];
                        games[i][j][1] += scoring[2 - k];

                        // Decrease the number of games left
                        // and call the function again
                        chances(favoriteTeam, gamesLeft - 1);

                        // Reset the game
                        games[i][j][0] = 0;
                        games[i][j][1] = 0;
                    }
                    firstFound = true;
                    break;
                }
            }
            if (firstFound)
            {
                break;
            }
            
        }
    }
    
}

int main()
{
    // Get the user input
    int favoriteTeam = 0;
    int gamesPlayed = 0;

    cin >> favoriteTeam >> gamesPlayed;

    // Get the input for the games
    for (int i = 0; i < gamesPlayed; i++)
    {
        int teamA, teamB, scoreA, scoreB;
        cin >> teamA >> teamB >> scoreA >> scoreB;

        // If scoreA is greater than scoreB
        if (scoreA > scoreB)
        {
            games[teamA - 1][teamB - 1][0] += 3;
        }
        // If scoreA is less than scoreB
        else if (scoreA < scoreB)
        {
            games[teamA - 1][teamB - 1][1] += 3;
        }
        // If scoreA is equal to scoreB
        else
        {
            games[teamA - 1][teamB - 1][0] += 1;
            games[teamA - 1][teamB - 1][1] += 1;
        }
    }

    // Find the chances of the favorite team winning in the tournament
    chances(favoriteTeam, 6 - gamesPlayed);

    cout << answer << endl;

    return 0;
}