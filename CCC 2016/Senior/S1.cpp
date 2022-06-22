#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Get user input

    string string1, string2;
    cin >> string1 >> string2;

    
    int letters1[26] = {0};
    int letters2[26] = {0};

    // The number of asterisks in the second string
    int wild = 0;

    for (int i = 0; i < (int)string1.length(); i++)
    {
        if (string2[i] == '*')
        {
            wild++;
        }
        else
        {
            letters2[string2[i] - 'a']++;
        }

        letters1[string1[i] - 'a']++;
    }

    int count = 0;

    for (int i = 0; i < 26; i++)
    {
        count += abs(letters1[i] - letters2[i]);
    }
    
    if (count != wild)
    {
        cout << 'N' << endl;
    }
    else
    {
        cout << 'A' << endl;
    }
    

    return 0;
}