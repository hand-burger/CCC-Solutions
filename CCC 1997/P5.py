inn = '/Users/jack/Documents/CCC-Solutions/CCC 1997/div.in'
outt = '/Users/jack/Documents/CCC-Solutions/CCC 1997/div.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')

# Read first line for number of numbers

firstLine = fin.readline()

# Loop through each set of dividends and divisors
for i in range(int(firstLine)):
    # Get the dividend and divisor
    dividend = fin.readline().strip()
    divisor = fin.readline().strip()

    # Get the size before they are modified in order to use it for calculations
    dividend_size = len(dividend)
    divisor_size = len(divisor)

    dividend_int = int(dividend)

    # Count variable, increases with each succesful subtraction and is used for the quotient
    count = 0

    quotient = ''

    # Repeat the subtraction until it returns a negative
    while True:
        # Essentially left align the dividend and divisor by adding trailing zeroes, which hopefully wont interfere with any math later on
        for i in range(len(dividend) - len(divisor)):
            divisor += '0'
        # Check for negative
        if dividend_int - int(divisor) >= 0:
            dividend_int -= int(divisor)
            count += 1
        else:
            break
    # Add the count of succesful subtractions to the quotient string
    quotient += str(count)
    # Now for the difference between the dividend and the divisor, which is the offset, loop through, remove the last zero to shift the number to the right and do more succesful subtractions
    for i in range(dividend_size - divisor_size):
        count = 0
        divisor = divisor[:-1]
        while True:
            if dividend_int - int(divisor) >= 0:
                dividend_int -= int(divisor)
                count += 1
            else:
                break
        # Again, add the count of succesful subtractions to the quotient
        quotient += str(count)

    print(quotient + '\n' + str(dividend_int) + '\n')
    fout.write(quotient + '\n' + str(dividend_int) + '\n\n')

fin.close()
fout.close()