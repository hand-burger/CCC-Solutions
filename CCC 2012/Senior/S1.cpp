#include <iostream>

using namespace std;

int main()
{
    // Get the jersey number
    int jerseyNumber;

    cin >> jerseyNumber;

    jerseyNumber--;

    // Literally just nCr

    // n is the number of jerseys - 1
    // r is 3

    // nCr = n! / r!(n-r)!

    cout << (jerseyNumber * (jerseyNumber - 1) * (jerseyNumber - 2) / 6) << endl;

    return 0;
}