import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/censor.in'
outt = absolute_path + '/censor.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')

n = fin.readline()

# Looping through the number of lines
for i in range(int(n)):
    # Get the current line
    line = fin.readline().strip()
    # Only after the first loop, print an end line which seperates each line
    if i > 0:
        print()
        fout.write('\n')
    # Loop through each word, if 4 letters, replace with ****
    for i in line.split():
        if len(i) == 4:
            i = '****'
        print(i, end=' ')
        fout.write(i + ' ')

fin.close()
fout.close()