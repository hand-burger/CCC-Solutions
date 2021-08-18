depth1 = int(input())
depth2 = int(input())
depth3 = int(input())
depth4 = int(input())

if depth1 == depth2 == depth3 == depth4:
    print('Fish At Constant Depth')
elif depth1 < depth2 < depth3 < depth4:
    print('Fish Rising')
elif depth1 > depth2 > depth3 > depth4:
    print('Fish Diving')
else:
    print('No Fish')