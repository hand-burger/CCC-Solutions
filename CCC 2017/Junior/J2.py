n = int(input())
shift = int(input())

sum = 0

for i in range(shift + 1):
    sum += n
    n *= 10

print(sum)
