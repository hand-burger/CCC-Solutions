w_counter = 0

for i in range(6):
    result = str(input())
    if result == 'W':
        w_counter += 1

if w_counter > 4:
    print(1)
elif w_counter <= 4 and w_counter > 2:
    print(2)
elif w_counter <= 2 and w_counter > 0:
    print(3)
else:
    print(-1)
