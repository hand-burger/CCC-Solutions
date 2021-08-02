# So, it might seem random but there is a pattern to these bit patterns
# For example, given 4 2, (pair of size 4 including 2 1's)
# Make 4 0's and set the first 2 0's to 1's (0000 -> 1100)
# Search in that number for the last 10, reverse it (10 -> 01)
# And reverse the remaining parts of the string
# That gives you a new number 1100 -> 1010
# Find the last 10 and repeat, (1010 -> 1001)
# Then do it until you can't do it anymore (Essentially when all the ones are on the right)

import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/pat.in'
outt = absolute_path + '/pat.out'

# Open input files
fin = open(inn)
fout = open(outt, 'w')

# Get first line for array size
firstLine = fin.readlines()

# Create array size of numbers in file
nums = [[None] * 2] * int(firstLine[0])

# Load array with values
for i in range(len(nums)):
    nums[i] = str(firstLine[i + 1]).split()

# Convert string array to int
nums = [list( map(int,i) ) for i in nums]

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

fin.close()
fout.close()