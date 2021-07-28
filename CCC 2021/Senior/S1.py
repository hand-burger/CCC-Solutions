# Get input

n = int(input())

# Put each length and width input into the array

lengths = list(map(int, input().split()))

widths = list(map(int, input().split()))

area = 0

# Loop through each fence piece and get the area

for i in range(1, n + 1):
    # Remember that the planks are not rectangles, but trapezoids, and thus use the area formula is different
    area += (lengths[i] + lengths[i - 1]) * widths[i - 1] / 2

print(area)