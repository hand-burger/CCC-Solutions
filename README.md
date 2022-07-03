# Canadian Computing Contest Solutions

<img alt="c++" src="https://raw.githubusercontent.com/isocpp/logos/master/cpp_logo.png" height="40" hspace="10"> <img alt="python" src="https://www.pngall.com/wp-content/uploads/2016/05/Python-Logo-PNG-Image.png" height="40" hspace="10">

Waterloo CCC problems solutions written in C++ and/or Python 3.

# Info

Each year of problems is made up of junior and senior sections. Most junior solutions are written in Python, while senior solutions are written in C++.

Not all of the solutions are complete (currently about 1/3 complete) and probably will never be.

# Examples

## [CCC 1996 P3 - Pattern Generator](https://github.com/hand-burger/CCC-Solutions/blob/main/CCC%201996/P3.py)

In this problem you need to determine the bit patterns of a binary number, where the input is the size of the number and quantity of ones in the number.

For example: 4 2 would be a four bit number with two ones (1100, 1010, etc.)

Based on this, you need to print each pattern of bits which respects the input.

So, it might seem random but there is a pattern to these bit patterns.

For example, given 4 2, (pair of size 4 including 2 1's).

Make 4 0's and set the first 2 0's to 1's (0000 -> 1100).

Search in that number for the last 10, reverse it (10 -> 01).

And reverse the remaining parts of the string.

That gives you a new number 1100 -> 1010.

Find the last 10 and repeat, (1010 -> 1001).

Then do it until you can't do it anymore (Essentially when all the ones are on the right).

In python this looks like (this is using file I/O so it might look a little weird):

```py
# Get first line for array size
firstLine = fin.readlines()

# Create array size of numbers in file
nums = [[None] * 2] * int(firstLine[0])

# Load array with values
for i in range(len(nums)):
    nums[i] = str(firstLine[i + 1]).split()

# Convert string array to int
nums = [list(map(int, i)) for i in nums]

# Init bit patterns
bitPatterns = ""

for i in range(len(nums)):
    print('\nThe bit patterns are\n')
    fout.write('\nThe bit patterns are\n')
    n = nums[i][0]
    k = nums[i][1]
    bitPatterns = ''
    # Put 1's and 0's into the bitPatterns string
    for i in range(k):
        bitPatterns += '1'
    for i in range(n-k):
        bitPatterns += '0'

    # Initial print of the string
    print(bitPatterns)
    fout.write(bitPatterns + '\n')

    # When a trailing '10' is found in the string
    ten = bitPatterns.rfind('10')

    while ten != -1:
        # Flip the ten
        bitPatterns = bitPatterns[:ten] + '0' + bitPatterns[ten + 1:]
        bitPatterns = bitPatterns[:ten + 1] + '1' + bitPatterns[ten + 2:]
        # Now reverse the rest of the string after the flipped '10'
        reversedSegment = bitPatterns[:ten + 1:-1]
        unreversedSegment = reversedSegment[::-1]
        # If the reversed string isn't empty
        if reversedSegment != '':
            # Now insert the reversed part into the string
            # This line says bitPatterns is equal to itself until it passes the 10 it found plus the reversed string
            bitPatterns = bitPatterns[:ten + 2] + reversedSegment
        print(bitPatterns)
        fout.write(bitPatterns + '\n')
        # Repeat the 10 search
        ten = bitPatterns.rfind('10')
```

## [CCC 2015 S3 - Gates](https://github.com/hand-burger/CCC-Solutions/blob/main/CCC%202015/Senior/S3.cpp)

In this problem you need to find the number of planes that are able to dock at an airport.

You are to assign the ith plane to permanently dock at any gate 1,...,gi (1 ≤ gi ≤ G), at which no previous plane has docked. As soon as a plane cannot dock at any gate, the airport is shut down and no future planes are allowed to arrive.

And so you want to maximize the number of planes that can dock.

Along with the number of gates and planes at the airport, each plane has a gate number which they must land at or any gate less than their gate number.

So the tricky part is maximizing the number of planes that can dock while keeping in mind that some combinations work better than others.

My solution uses a disjoint set to find the maximum number of planes that can dock:

```c++
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
```

# Progress (07/03/22)

1996: COMPLETE

1997: COMPLETE

1998: 2 / 5

1999: 0 / 5

2000: 4 / 8

2001: 2 / 8

2002: 1 / 8

2003: 1 / 8

2004: 1 / 8

2005: 1 / 8

2006: 2 / 8

2007: 5 / 8

2008: 1 / 8

2009: 1 / 8

2010: 1 / 8

2011: 6 / 8

2012: 6 / 8

2013: 5 / 8

2014: 5 / 8

2015: 5 / 8

2016: 4 / 8

2017: 5 / 8

2018: 4 / 8

2019: 4 / 8

2020: 1 / 8

2021: COMPLETE

2022: 4 / 8

# Links
Past Contests are available [here](https://www.cemc.uwaterloo.ca/contests/past_contests.html#ccc)
