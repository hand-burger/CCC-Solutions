import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

outt1 = absolute_path + '/perfect.out'
outt2 = absolute_path + '/cube.out'

# Open files
fout1 = open(outt1, 'w')
fout2 = open(outt2, 'w')

#Perfect Numbers
for i in range(1000, 10000):
    summ = 1
    for j in range(1, i):
        if i % j == 0 and i / j != i:
            summ += (i / j)
    if summ == i:
        print(i)
        fout1.write(str(i) + '\n')

# Cubes
for i in range(100, 1000):
    summ = 0
    n = i
    while True:
        if n == 0:
            break
        d = n % 10
        n //= 10
        # Add cube to the sum
        summ += d * d * d
    if summ == i:
        print(i)
        fout2.write(str(i) + '\n')