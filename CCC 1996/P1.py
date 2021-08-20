import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/dpa.in'
outt = absolute_path + '/dpa.out'

fin = open(inn)
fout = open(outt, 'w')

# Get first line for array size
firstLine = fin.readlines()

# Create array size of numbers in file
nums = [None] * int(firstLine[0])

summ = 1
# Load array with values
for i in range(len(nums)):
    nums[i] = int(firstLine[i + 1])

# Now get sum of n's divisors
for i in range(len(nums)):
    # Summ is reset to the default value of 1
    summ = 1
    for j in range(1, nums[i]):
        # If nums[i] / 1 cleanly divides and is not equal to nums[i]
        if nums[i] % j == 0 and nums[i] / j != nums[i]:
            summ += (nums[i] / j)
    if summ == nums[i]:
        fout.write(str(nums[i]) + ' is a perfect number.\n')
        print(nums[i], 'is a perfect number.')
    elif summ < nums[i]:
        fout.write(str(nums[i]) + ' is a deficient number.\n')
        print(nums[i], 'is a deficient number.')
    else:
        fout.write(str(nums[i]) + ' is an abundant number.\n')
        print(nums[i], 'is an abundant number.')

fin.close()
fout.close()
