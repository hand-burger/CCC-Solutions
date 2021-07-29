inn = '/Users/jack/Documents/CCC-Solutions/CCC 1997/dkc.in'
outt = '/Users/jack/Documents/CCC-Solutions/CCC 1997/dkc.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')

# Get first line (number of numbers)
firstLine = fin.readline()

for i in range(int(firstLine)):
    # Number of teams in the competition for that test case.
    n = fin.readline()
    # One-loss, eliminated, & count vars
    oneLoss = 0
    eliminated = 0
    count = 0

# Determine the number of rounds, undefeated, one-loss & eliminated
while True:
    # Initial print of status
    print('Round:', count, ':', n, 'undefeated,', oneLoss, 'one-loss,', eliminated, 'eliminated')
    fout.write('Round: ' + str(count) + ': ' + str(n) + ' undefeated, ' + str(oneLoss) + ' one-loss, ' + str(eliminated) + ' eliminated\n')
    # When number of teams is 0 and one loss is 1, break the loop because it is the last round
    if n == 0 and oneLoss == 1:
        break
    # On the round before the last set one-line to 2 and n to 0
    if n == 1 and oneLoss == 1:
        oneLoss = 2
        n = 0
    else:
        eliminated = eliminated + oneLoss // 2
        oneLoss = oneLoss - (oneLoss // 2) + (int(n) // 2)
        n = int(n) - (int(n) // 2)
    # Once gone through all, increase the round count
    count += 1
print('There are', count, 'rounds.')
fout.write('There are ' + str(count) + ' rounds.')