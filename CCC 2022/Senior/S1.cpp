#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int N;
    cin >> N;

    int combinations = 0;

    if (N % 4 == 0)
    {
        combinations++;
    }
    if (N % 5 == 0)
    {
        combinations++;
    }

    // Loop up to the number / 4

    for (size_t i = 1; i < N/4; ++i)
    {
        if ((N - (i*4)) % 5 == 0)
        {
            combinations++;
        }
    }
    for (size_t i = 1; i < N/5; ++i)
    {
        if (N - (i * 5) % 4 == 0)
        {
            combinations++;
        }
    }

   cout << combinations << endl;

    return 0;
}