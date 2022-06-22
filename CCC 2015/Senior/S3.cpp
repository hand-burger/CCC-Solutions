#include <iostream>
#include <vector>

using namespace std;

// Define disjoint set
struct disjointSet
{
    vector<int> rank, parent;
    int n;

public:
    disjointSet(int n) : n(n), rank(n + 1), parent(n + 1){}

    // Creates the disjoint set
    void makeSet()
    {
        for (int i = 0; i < n; i++)
        {
            parent[i] = i;
        }
        
    }

    int findSet(int x)
    {
        if (parent[x] != x)
        {
            parent[x] = findSet(parent[x]);
        }
        return parent[x];
    }

    // Finds the set of x and y and combines them
    void Union(int x, int y)
    {
        int xRoot = findSet(x), yRoot = findSet(y);

        // If the two sets are already in the same set, do nothing
        if (xRoot == yRoot)
        {
            return;
        }

        if (xRoot < yRoot)
        {
            parent[yRoot] = xRoot;
        }
        else if (yRoot < xRoot)
        {
            parent[xRoot] = yRoot;
        }

        // Else, make the union of the two sets
        else
        {
            parent[yRoot] = xRoot;

            // Increment the rank or size of the set
            rank[xRoot]++;
        }
        
    }
};

int main()
{
    // Get user input
    int numberOfGates = 0;
    int numberOfPlanes = 0;

    cin >> numberOfGates >> numberOfPlanes;

    disjointSet ds(numberOfGates + 3);
    ds.makeSet();

    int count = 0;

    // Get each plane
    for (int i = 0; i < numberOfPlanes; i++)
    {
        // Get the gate number, plane must land at a gate from 1 to numberOfGates inclusive so add 1 to the gate number
        int gateNumber;
        cin >> gateNumber;
        gateNumber++;

        int a = ds.findSet(gateNumber);

        if (a > 1)
        {
            count++;
        }
        else
        {
            break;
        }

        // Find the set of the gate number
        int b = ds.findSet(a - 1);
        ds.Union(a, b);
        
    }

    // Print the number of planes that can land
    cout << count << endl;

    return 0;
}