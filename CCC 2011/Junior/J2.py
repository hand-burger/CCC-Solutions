# A= −6t4 + ht3 + 2t2 + t

humidity_factor = int(input())
max_hours = int(input())

altitude = 0

for current_hour in range(1, max_hours):
    altitude = -6*current_hour*current_hour*current_hour*current_hour + humidity_factor*current_hour*current_hour*current_hour + 2*current_hour*current_hour + current_hour
    if altitude <= 0:
        break

if altitude > 0:
    print ("The balloon does not touch ground in the given time.")
else:
    print ("The balloon touches ground at hour:\n" , current_hour)
