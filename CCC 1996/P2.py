# Take in input number
# For algo, do n % 10 since the remainder = last number
# Store that value
# Subtract it from the number, divide by 10, and subtract it again

import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/div.in'
outt = absolute_path + '/div.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')

# Get first line for array size
firstLine = fin.readlines()

# Create array size of numbers in file
nums = [None] * int(firstLine[0])

# Load array with values
for i in range(len(nums)):
    nums[i] = int(firstLine[i + 1])

# Loop through all numbers from input
for i in range(len(nums)):
    # Hold onto the initial number for printing later
    number = nums[i]
    print(nums[i])
    fout.write(str(nums[i]) + '\n')
    # Loop through all steps of each number
    # len(str(nums[i])) - 1) because the amount of times it does the algorithm is equal to the amount of digits in the number - 1
    for j in range(len(str(nums[i])) - 1):
        # Ensure the number has more than two digits
        if nums[i] / 10 >= 10:
            # Get last digit of number
            hold = nums[i] % 10
            # Remove last number and subtract for new number
            nums[i] = int((nums[i] - hold) // 10 - hold)
            print(nums[i])
            fout.write(str(nums[i]) + '\n')
        else:
            # Checks for when it is two digits
            if nums[i] == 11:
                print('The number', number, 'is divisible by 11.')
                fout.write('The number ' + str(number) + ' is divisible by 11.\n\n')
            else:
                print('The number', number, 'is not divisible by 11')
                fout.write('The number ' + str(number) + ' is not divisible by 11\n\n')

fin.close()
fout.close()