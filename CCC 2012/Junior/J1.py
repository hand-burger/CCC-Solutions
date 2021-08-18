speed_limit = input('Enter the speed limit: ')
recorded_speed = input('Enter the recorded speed of the car: ')

speed_difference = int(recorded_speed) - int(speed_limit)

if speed_difference >= 1 and speed_difference <= 20:
    print('You are speeding and your fine is $100.')
elif speed_difference >= 21 and speed_difference <= 30:
    print('You are speeding and your fine is $270.')
elif speed_difference >= 31:
    print('You are speeding and your fine is $500.')
else:
    print('Congratulations, you are within the speed limit!')