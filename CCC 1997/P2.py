inn = '/Users/jack/Documents/CCC-Solutions/CCC 1997/nasty.in'
outt = '/Users/jack/Documents/CCC-Solutions/CCC 1997/nasty.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')

# Get the first line/number of numbers
firstLine = fin.readline()

# Initialize nums array
nums = [None] * int(firstLine)

# Load the array with the input values
for i in range(int(firstLine)):
    nums[i] = int(fin.readline().strip())

# Loop through each element of nums input and check each factor
for i in nums:
    fac1 = []
    for j in range(1, i + 1):
        if i % j == 0:
            fac2 = []
            temp = i//j
            if j > temp:
                fac2.append(j)
                fac2.append(temp)
            else:
                fac2.append(temp)
                fac2.append(j)
            if fac2 not in fac1:
                fac1.append(fac2)
    nasty = False
    for x in fac1:
        difference = x[0] - x[1]
        pointer = fac1.index(x) + 1
        while pointer != fac1.index(x):
            if pointer > len(fac1) - 1:
                pointer = 0
            elif fac1[pointer][0] + fac1[pointer][1] == difference:
                pointer = fac1.index(x)
                nasty = True
            else:
                pointer += 1
    if nasty:
        print(i, 'is nasty')
        fout.write(str(i) + ' is nasty\n')
    else:
        print(i, 'is not nasty')
        fout.write(str(i) + ' is not nasty\n')

fin.close()
fout.close()