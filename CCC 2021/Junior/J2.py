p = int(input())
i = 0
winner = " "
highestBid = 0

for i in range(p):
    currentName = str(input())
    currentBid = int(input())
    if currentBid > highestBid:
        highestBid = currentBid
        winner = currentName

print(winner)
