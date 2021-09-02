weight = float(input())
height = float(input())

BMI = weight / (height * height)

if BMI > 25:
    print('Overweight')
elif BMI < 18.5:
    print('Underweight')
else:
    print('Normal weight')
