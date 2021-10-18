output = ""
n = ""
while n != "99999":
    n = input()
    if n != "99999":
        turn = int(n[0]) + int(n[1])
        if turn % 2 == 0 and turn != 0:
            output += "right"
            previous = "right"
        elif turn % 2 == 1:
            output += "left"
            previous = "left"
        elif turn == 0:
            output += previous
        output += " "+n[2:]+"\n"
print(output)
