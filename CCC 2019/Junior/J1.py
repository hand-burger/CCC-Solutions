three_point_apples = int(input())
two_point_apples = int(input())
one_point_apples = int(input())

three_point_bananas = int(input())
two_point_bananas = int(input())
one_point_bananas = int(input())

apple_total = (three_point_apples * 3) + \
    (two_point_apples * 2) + (one_point_apples)
banana_total = (three_point_bananas * 3) + \
    (two_point_bananas * 2) + (one_point_bananas)

if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else:
    print('T')
