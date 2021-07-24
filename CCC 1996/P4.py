inn = '/Users/jack/Documents/CCC-Solutions/CCC 1996/rom.in'
outt = '/Users/jack/Documents/CCC-Solutions/CCC 1996/rom.out'

# Open input files
fin = open(inn)
fout = open(outt, 'w')

# Get first line for array size
firstLine = fin.readlines()

# Create array size of numbers in file
nums = [None] * int(firstLine[0])

# Load array with values
for i in range(0, len(nums)):
    nums[i] = str(firstLine[i + 1]).strip()

# Iterate through each equation
for i in range(0, len(nums)):
    # Reset values after each iteration of equation
    romanValue = 0
    first = 0
    second = 0
    print(nums[i], end='')
    fout.write(nums[i])
    # Iterate through each character of the equation
    for j in range(0, len(nums[i])):
        # Get sum
        romanSum = first + second
        currentChar = nums[i][j]
        # When current character is not the last, assign next character
        if currentChar != '=':
            nextChar = nums[i][j + 1]

        # While not on the last character go through each character and increment a variable based on the values of the input
        while currentChar != '=':
            if currentChar == 'M':
                romanValue += 1000
            elif currentChar == 'D':
                romanValue += 500
            elif currentChar == 'C' and nextChar == 'M':
                romanValue += 900
                j += 1
            elif currentChar == 'C' and nextChar == 'D':
                romanValue += 400
                j += 1
            elif currentChar == 'C':
                romanValue += 100
            elif currentChar == 'L':
                romanValue += 50
            elif currentChar == 'X' and nextChar == 'C':
                romanValue += 90
                j += 1
            elif currentChar == 'X' and nextChar == 'L':
                romanValue += 40
                j += 1
            elif currentChar == 'X':
                romanValue += 10
            elif currentChar == 'V':
                romanValue += 5
            elif currentChar == 'I' and nextChar == 'X':
                romanValue += 9
                j += 1
            elif currentChar == 'I' and nextChar == 'V':
                romanValue += 4
                j += 1
            elif currentChar == 'I':
                romanValue += 1
            # When the plus is reached
            else:
                # Get value for first and second part of the sum equation
                if first == 0:
                    first = romanValue
                else:
                    second = romanValue
                romanValue = 0
            j += 1
            currentChar = nums[i][j]
            if currentChar != '=':
                nextChar = nums[i][j + 1]
    # Once the sum of the equation is determined, turn it back into a roman numeral
    while romanSum > 0:
        if romanSum > 1000:
            romanSum = 0
            print('CONCORDIA CUM VERITATE', end='')
            fout.write('CONCORDIA CUM VERITATE')
        elif romanSum == 1000:
            romanSum -= 1000
            print('M', end='')
            fout.write('M')
        elif romanSum - 900 >= 0:
            romanSum -= 900
            print('CM', end='')
            fout.write('CM')
        elif romanSum - 500 >= 0:
            romanSum -= 500
            print('D', end='')
            fout.write('D')
        elif romanSum - 400 >= 0:
            romanSum -= 400
            print('CD', end='')
            fout.write('CD')
        elif romanSum - 100 >= 0:
            romanSum -= 100
            print('C', end='')
            fout.write('C')
        elif romanSum - 90 >= 0:
            romanSum -= 90
            print('XC', end='')
            fout.write('XC')
        elif romanSum - 50 >= 0:
            romanSum -= 50
            print('L', end='')
            fout.write('L')
        elif romanSum - 40 >= 0:
            romanSum -= 40
            print('XL', end='')
            fout.write('XL')
        elif romanSum - 10 >= 0:
            romanSum -= 10
            print('X', end='')
            fout.write('X')
        elif romanSum - 9 >= 0:
            romanSum -= 9
            print('IX', end='')
            fout.write('IX')
        elif romanSum - 5 >= 0:
            romanSum -= 5
            print('V', end='')
            fout.write('V')
        elif romanSum - 4 >= 0:
            romanSum -= 4
            print('IV', end='')
            fout.write('IV')
        else:
            romanSum -= 1
            print('I', end='')
            fout.write('I')
    print()
    fout.write('\n')

fin.close()
fout.close()