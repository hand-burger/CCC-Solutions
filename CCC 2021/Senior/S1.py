# Get input

n = int(input())

# Put each length and width input into the array

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

area = 0

# Loop through each fence piece and get the area

for i in range(1, n + 1):
    area += (arr[i] + arr[i - 1]) * brr[i - 1] / 2

print(area)