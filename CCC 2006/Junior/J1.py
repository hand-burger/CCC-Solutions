burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

calorie_count = 0

if burger == 1:
    calorie_count += 461
elif burger == 2:
    calorie_count += 431
elif burger == 3:
    calorie_count += 420

if side == 1:
    calorie_count += 100
elif side == 2:
    calorie_count += 57
elif side == 3:
    calorie_count += 70

if drink == 1:
    calorie_count += 130
elif drink == 2:
    calorie_count += 160
elif drink == 3:
    calorie_count += 118

if dessert == 1:
    calorie_count += 167
elif dessert == 2:
    calorie_count += 266
elif dessert == 3:
    calorie_count += 75

print('Your total Calorie count is ' + str(calorie_count) + ".")
