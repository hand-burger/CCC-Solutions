def rotatable(i):
    input_number = str(i)
    counter = 1
    rotatable = False

    # Just loop through each digit of the number and check if the respective digits are the same or follow the 6/9 rule
    for counter in range(len(input_number)):
        if input_number[counter - 1] == '8' and input_number[-counter] == '8' or input_number[counter - 1] == '0' and input_number[-counter] == '0' or input_number[counter - 1] == '1' and input_number[-counter] == '1' or input_number[counter - 1] == '6' and input_number[-counter] == '9' or input_number[counter - 1] == '9' and input_number[-counter] == '6':
            rotatable = True
        else:
            rotatable = False
            break     
    return rotatable

m = input('Enter the lower bound of the interval: ')
n = input('Enter the upper bound of the interval: ')
count = 0
print('The number of rotatable numbers is: ', end='')
for i in range(int(m), int(n) + 1):
    if rotatable(i):
        count += 1
print(count)