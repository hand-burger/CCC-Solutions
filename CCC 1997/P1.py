import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/sent.in'
outt = absolute_path + '/sent.out'

# Open the files for reading and writing purposes
fin = open(inn)
fout = open(outt, 'w')

firstLine = fin.readline().strip()

# Repeat for each data set in the input file
for i in range(0, int(firstLine)):
    # Get the number of subjects, verbs and objects
    subjects = fin.readline().strip()
    verbs = fin.readline().strip()
    objects = fin.readline().strip()

    # Initialize arrays
    subs = [None] * int(subjects)
    vebs = [None] * int(verbs)
    obs = [None] * int(objects)

    # Load arrays
    for i in range(int(subjects)):
        subs[i] = fin.readline().strip()
    for i in range(int(verbs)):
        vebs[i] = fin.readline().strip()
    for i in range(int(objects)):
        obs[i] = fin.readline().strip()

    # Simple triple for loop
    for i in range(0, int(subjects)):
        for j in range(0, int(verbs)):
            for k in range(0, int(objects)):
                print(subs[i] + ' ' + vebs[j] + ' ' + obs[k] + '.')
                fout.write(subs[i] + ' ' + vebs[j] + ' ' + obs[k] + '.\n')

fin.close()
fout.close()