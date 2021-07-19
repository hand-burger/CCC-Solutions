inn = '/Users/jack/Documents/CCC/CCC 1996/dpa.in'
outt = '/Users/jack/Documents/CCC/CCC 1996/dpa.out'

# Open the files for reading and writing purposes
fin = open(inn)
fout = open(outt)

# Initialize as 1 because n/n = 1
summ = 1

# Get first line for array size
firstLine = fin.readlines()

# Create array size of numbers in file
nums = [None] * int(firstLine[0])

# Load array with values
for i in range(0, len(nums)):
    nums[i] = int(firstLine[i + 1])

# Now get sum of n's divisors
for i in range(0, len(nums)):
    # When it has finished with one number and found the sum of divisors summ is resest to 0
    if i == len(nums):
        summ = 0
    # Summ is then reset to the default value of 1
    summ = 1
    for j in range(1, nums[i]):
        # If nums[i] / 1 cleanly divides and is not equal to nums[i]
        if nums[i] % j == 0 and nums[i] / j != nums[i]:
            summ += (nums[i] / j)
    if summ == nums[i]:
        print(str(nums[i]) + ' is a perfect number.')
    elif summ < nums[i]:
        print(str(nums[i]) + ' is a deficient number.')
    else:
        print(str(nums[i]) + ' is an abundant number.')

fin.close()
fout.close()