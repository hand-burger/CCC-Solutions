week_start = input('Enter day: ')
number_of_days = input('Enter the number of days in the month: ')
int_week_start = int(week_start)

print('Sun Mon Tue Wed Thr Fri Sat')

for i in range(int_week_start):
    print('   ', end='')

for i in range(1, int(number_of_days) + 1):
    print(i, end='   ')
    int_week_start += 1
    
    if int_week_start > 7:
        print()
        int_week_start = 1