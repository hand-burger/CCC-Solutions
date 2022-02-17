#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;

    // Two pieces of input for each player

    int points;
    int fouls;

    int total = 0;

    int gold = 0;

    for (size_t i = 0; i < N; ++i)
    {
        cin >> points;

        total += points * 5;

        cin >> fouls;

        total -= fouls * 3;

        if (total > 40)
        {
            gold++;
        }
    }

    if (gold == N)
    {
        cout << gold << "+" << endl;
    }
    else
    {
        cout << gold << endl;
    }

    return 0;
}