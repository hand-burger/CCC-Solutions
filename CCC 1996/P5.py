import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/max.in'
outt = absolute_path + '/max.out'

fin = open(inn)
fout = open(outt, 'w')

# Get first line
firstLine = fin.readline().strip()

# Go through each sequence
for i in range(int(firstLine)):
    # Get the size of the sequence
    size = fin.readline().strip()

    # Get X and Y
    x = fin.readline().strip().replace(" ", "")
    y = fin.readline().strip().replace(" ", "")

    # Rest max distance counter
    m = 0

    # Go through each element in the sequences
    for i in range(int(size)):
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
    print('The maximum distance is', m)
    fout.write('The maximum distance is ' + str(m) + '\n')

fin.close()
fout.close()