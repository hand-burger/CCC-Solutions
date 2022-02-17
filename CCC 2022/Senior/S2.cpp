#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int X;
    cin >> X;

    // Take in the two names into 2d vector

    vector<vector<string> > xNames;

    for (size_t i = 0; i < X; ++i)
    {
        vector<string> name;
        string firstName;
        string lastName;
        cin >> firstName;
        cin >> lastName;
        name.push_back(firstName);
        name.push_back(lastName);
        xNames.push_back(name);
    }

    // Get two names for the input

    // for (size_t i = 0; i < X; ++i)
    // {
    //     string firstName;
    //     string lastName;
    //     cin >> firstName;
    //     cin >> lastName;
    //     xNames.push_back({firstName, lastName});
    // }

    int Y;
    cin >> Y;

    vector<vector<string> > yNames;

    for (size_t i = 0; i < Y; ++i)
    {
        vector<string> name;
        string firstName;
        string lastName;
        cin >> firstName;
        cin >> lastName;
        name.push_back(firstName);
        name.push_back(lastName);
        yNames.push_back(name);
    }

    // Get two names for the input

    // for (size_t i = 0; i < Y; ++i)
    // {
    //     string firstName;
    //     string lastName;
    //     cin >> firstName;
    //     cin >> lastName;
    //     yNames.push_back({firstName, lastName});
    // }

    int G;
    cin >> G;

    vector<vector<string> > gNames;

    for (size_t i = 0; i < G; ++i)
    {
        vector<string> name;
        string firstName;
        string secondName;
        string lastName;
        cin >> firstName;
        cin >> secondName;
        cin >> lastName;
        name.push_back(firstName);
        name.push_back(secondName);
        name.push_back(lastName);
        gNames.push_back(name);
    }

    // Get three names for the input

    // for (size_t i = 0; i < G; ++i)
    // {
    //     string firstName;
    //     string secondName;
    //     string lastName;
    //     cin >> firstName;
    //     cin >> secondName;
    //     cin >> lastName;
    //     gNames.push_back({firstName, secondName, lastName});
    // }

    // xStudents must be in the same group!
    // yStudents must not be in the same group!

    // gNames contain the groups

    // So g[0][0]&[0][1]&[0][2] is the first group

    // I guess do some binary search for anything wrong??


    // Take the first set of names that must be together
    // Go to the first group, search for the first name,
    // If it exists and the other does not, ++
    // If it exists and the other one does, nothing.
    // Next group . . .

    // So you want to loop over each group as well as each name
    // So G and X

    int violations = 0;

    for (size_t i = 0; i < G; ++i)
    {
        for (size_t j = 0; j < X; ++j)
        {
            // IF YOU CAN FIND WITHIN THE GROUPS THE FIRST NAME OF THE iTH INDEX AND YOU CANT FIND THE SECOND NAME OF THE iTH INDEX
            if (binary_search(gNames[i].begin(), gNames[i].end(), xNames[j][0]) && !binary_search(gNames[i].begin(), gNames[i].end(), xNames[j][1]))
            {
                // If you can find the first name but not the second name, violation
                // Using binary search, check if the first name of the vector at index i exists
                violations++;
            }
        }
    }

    // Now do the opposite
    for (size_t i = 0; i < G; ++i)
    {
        for (size_t j = 0; j < Y; ++j)
        {
            if (binary_search(gNames[i].begin(), gNames[i].end(), yNames[j][0]) && binary_search(gNames[i].begin(), gNames[i].end(), yNames[j][1]))
            {
                // If you can find the first name and the second name, violation
                // Found the second one, no good
                violations++;
            }
        }
    }

    cout << violations << endl;

    return 0;
}