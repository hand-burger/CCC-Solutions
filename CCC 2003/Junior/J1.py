t = int(input())
s = int(input())
h = int(input())
spaces = s * ' '

for i in range(t):
    print('*' + spaces + '*' + spaces + '*')

print((3 + 2 * s) * '*')

for i in range(h):
    print((s + 1) * ' ' + '*')
