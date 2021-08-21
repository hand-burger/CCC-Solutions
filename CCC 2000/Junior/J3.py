# Each play costs one quarter. 
# The first machine pays 30 quarters every 35th time it is played; 
# the second machine pays 60 quarters every 100th time it is played; 
# the third pays 9 quarters every 10th time it is played.

print('How many quarters does Martha have in the jar?')
number_of_quarters = int(input())
print('How many times has the first machine been played since paying out?')
first_machine_plays = int(input())
print('How many times has the second machine been played since paying out?')
second_machine_plays = int(input())
print('How many times has the third machine been played since paying out?')
third_machine_plays = int(input())

current_turn = 0

while number_of_quarters > 0:
    number_of_quarters -= 1
    current_turn += 1
    first_machine_plays += 1
    if first_machine_plays == 35:
        first_machine_plays = 0
        number_of_quarters += 30
    if number_of_quarters == 0:
        break

    number_of_quarters -= 1
    current_turn += 1
    second_machine_plays += 1
    if second_machine_plays == 100:
        second_machine_plays = 0
        number_of_quarters += 60
    if number_of_quarters == 0:
        break
    
    number_of_quarters -= 1
    current_turn += 1
    third_machine_plays += 1
    if third_machine_plays == 10:
        third_machine_plays = 0
        number_of_quarters += 9
    if number_of_quarters == 0:
        break

print('Martha plays', current_turn, 'times before going broke.')