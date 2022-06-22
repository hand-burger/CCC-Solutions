#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Get user input
    int numberOfStudents = 0;

    cin >> numberOfStudents;

    string firstListOfStudents[numberOfStudents];
    string secondListOfStudents[numberOfStudents];

    // Initialize lists of students
    for (int i = 0; i < numberOfStudents; i++)
    {
        cin >> firstListOfStudents[i];
    }

    for (int i = 0; i < numberOfStudents; i++)
    {
        cin >> secondListOfStudents[i];
    }
    
    // Loop over the lists of students
    for (int i = 0; i < numberOfStudents; i++)
    {
        for (int j = 0; j < numberOfStudents; j++)
        {
            // If the current partners don't agree, the lists are bad.
            if ((firstListOfStudents[i] == secondListOfStudents[j]) && (firstListOfStudents[j] != secondListOfStudents[i]))
            {
                cout << "bad" << endl;
                return 0;
            }
            if (firstListOfStudents[i] == secondListOfStudents[i])
            {
                cout << "bad" << endl;
                return 0;
            }
            
        }
        
    }
    
    // If it gets here, the lists are good
    cout << "good" << endl;
    
    return 0;
}