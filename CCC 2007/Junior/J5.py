# All this for the input of min and max dist aswell as additional motels

minDist = int(input())
maxDist = int(input())
n = int(input())
motels = [None] * (13 + n)

ways = 0

# Recursively gather input for motels from specified number
for i in range(0, n):
    motels[13 + i] = int(input())

# Assign motel values
motels[0] = 990
motels[1] = 1010
motels[2] = 1970
motels[3] = 2030
motels[4] = 2940
motels[5] = 3060
motels[6] = 3930
motels[7] = 4060
motels[8] = 4970
motels[9] = 5030
motels[10] = 5990
motels[11] = 6010
motels[12] = 7000

# Check if provided numbers are between
def between(a, b, c):
    return bool(a <= b and b <= c)

# Recursively determine if path is possible and how many times
def path(dist):
    # Global variable assignment
    global ways
    # First check if distance is already 7,000 before continuing
    if dist == 7000:
        # Increase counter
        ways += 1
    else:
        for i in range(0, len(motels)):
            # If the next motel - current distance (motel) is between the min and max distance aka if you can get to the next motel
            # Run the function again with that motel
            if between(minDist, motels[i] - dist, maxDist):
                path(motels[i])

path(0)

print(ways)