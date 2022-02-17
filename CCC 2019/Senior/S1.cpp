#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string input;
    cin >> input;

    int size = input.size();

    static const int board[4] = {1, 2, 3, 4};
    vector<int> numbers(board, board + sizeof(board) / sizeof(board[0]));

    for (size_t i = 0; i < size; ++i)
    {
        if (input[i] == 'H')
        {
            swap(numbers[0], numbers[2]);
            swap(numbers[1], numbers[3]);
        }
        else
        {
            swap(numbers[0], numbers[1]);
            swap(numbers[2], numbers[3]);
        }
    }

    for (size_t i = 0; i < 2; ++i)
    {
        cout << numbers[i] << " ";
    }

    cout << endl;
    
    for (size_t i = 0; i < 2; ++i)
    {
        cout << numbers[i+2] << " ";
    }

    cout << endl;

    return 0;
}