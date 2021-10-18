rows = int(float(input()))
column = int(float(input()))
k = int(input())
r = [0]*rows
c = [0]*column
for i in range(k):
    n = input()
    if n[0] == 'R':
        r[int(n[2:])-1] += 1
    else:
        c[int(n[2:])-1] += 1
for i in range(len(r)):
    if r[i] % 2 != 0:
        r[i] = 1
for i in range(len(c)):
    if c[i] % 2 != 0:
        c[i] = 1
print(r.count(1)*column+c.count(1)*rows-r.count(1)*c.count(1)*2)
