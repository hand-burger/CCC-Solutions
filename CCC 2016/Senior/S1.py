first = list(input())
second = str(input()).replace('*', '')

out = 'A'

# Loop through each letter in second, if it is in first then remove it until you can't or first is empty

for i in second:
    if i in first:
        first.remove(i)
    else:
        out = 'N'
        break

print(out)
