inn = '/Users/jack/Documents/CCC-Solutions/CCC 1996/max.in'
outt = '/Users/jack/Documents/CCC-Solutions/CCC 1996/max.out'

# Open input files
fin = open(inn)
fout = open(outt, 'w')

# Get first line
firstLine = fin.readline().strip()

# Go through each sequence
for i in range(0, int(firstLine)):
    # Get the size of the sequence
    size = fin.readline().strip()

    # Get X and Y
    x = fin.readline().strip().replace(" ", "")
    y = fin.readline().strip().replace(" ", "")

    # Rest max distance counter
    m = 0

    # Go through each element in the sequences
    for i in range(0, int(size)):
        # In each number of X, go through Y and find the last pos of y[j] >= x[i]
        # Then if j > i and j-i > last max, that is the new max and repeat
        j = int(size) - 1
        while True:
            if j <= i or y[j] >= x[i]:
                break
            else:
                j -= 1
        if j > i and j - i > m:
            m = j - i
    print('The maximum distance is ' + str(m))
    fout.write('The maximum distance is ' + str(m) + '\n')

fin.close()
fout.close()