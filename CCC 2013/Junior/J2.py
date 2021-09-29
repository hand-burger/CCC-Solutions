word = str(input())

count = 0

for i in word:
    if "I" in i:
        count += 1
    if "O" in i:
        count += 1
    if "S" in i:
        count += 1
    if "H" in i:
        count += 1
    if "Z" in i:
        count += 1
    if "X" in i:
        count += 1
    if "N" in i:
        count += 1

if count == len(word):
    print('YES')
else:
    print('NO')
