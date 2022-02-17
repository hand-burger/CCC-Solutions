#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isPrime(int number)
{
    if (number < 2)
    {
        return false;
    }
    if (number == 2)
    {
        return true;
    }
    if (number % 2 == 0)
    {
        return false;
    }
    for (size_t i = 3; (i*i) <= number; ++i)
    {
        if (number % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int n;
    cin >> n;

    vector<int> input;

    for (size_t i = 0; i < n; ++i)
    {
        int num;
        cin >> num;
        input.push_back(num);
    }

    // Now with input
    // Loop over each number
    // Get number combinations of double the current number

    for (size_t i = 0; i < n; ++i)
    {
        int currentNumber = input[i] * 2;
        // Now loop up to sqrt of the number to find combinations, so j and current number - j
        for (size_t j = 0; j <= ceil(sqrt(currentNumber)); ++j)
        {
            if (isPrime(j) && isPrime(currentNumber - j))
            {
                cout << j << " " << currentNumber - j << endl;
            }
        }
    }

    return 0;
}