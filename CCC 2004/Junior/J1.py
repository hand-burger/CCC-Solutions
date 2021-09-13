value = int(input())
i = 0
while True:
    if i * i > value:
        print("The largest square has side length " + str(i-1) + ".")
        break
    else:
        i += 1
