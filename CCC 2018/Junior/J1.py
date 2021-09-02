digit_one = int(input())
digit_two = int(input())
digit_three = int(input())
digit_four = int(input())

if (digit_one == 8 or digit_one == 9) and (digit_four == 8 or digit_four == 9) and (digit_two == digit_three):
    print('ignore')
else:
    print('answer')
