x_value = int(input())
y_value = int(input())

if x_value > 0 and y_value > 0:
    print(1)
elif x_value < 0 and y_value > 0:
    print(2)
elif x_value < 0 and y_value < 0:
    print(3)
else:
    print(4)
