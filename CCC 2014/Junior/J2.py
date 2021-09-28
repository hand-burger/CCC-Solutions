votes = int(input())
sequence = str(input())

countA = sequence.count('A')
countB = sequence.count('B')

if countA < countB:
    print('B')
elif countA > countB:
    print('A')
else:
    print('Tie')
