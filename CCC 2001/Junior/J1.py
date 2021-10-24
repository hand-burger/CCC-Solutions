# Get height
height = int(input("Enter height: "))

current = "*"
i = 1
while i < height:
    print(current + (" " * (height - len(current)) * 2 + current))
    current += "**"
    i += 2
while i > 0:
    print(current + (" " * (height - len(current)) * 2 + current))
    current = current[:-2]
    i -= 2
