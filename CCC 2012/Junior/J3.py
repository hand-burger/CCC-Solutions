scale = int(input())

stars = ''
x = ''
spaces = ''

for i in range(scale):
    stars += '*'
    x += 'X'
    spaces += ' '
for i in range(scale):
    print(stars + x + stars)
for i in range(scale):
    print(spaces + x + x)
for i in range(scale):
    print(stars + spaces + stars)