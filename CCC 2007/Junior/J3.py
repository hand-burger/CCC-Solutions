#Get input, set the respective elements of money to zero, get average and compare to the offer

choices = []
money = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

cases = int(input())

for i in range(0, cases):
    ele = int(input())
    choices.append(ele)

offer = int(input())

def averag(money):
    tot = 0
    money = [i for i in money if i != 0]
    for i in range(0, len(money)):
        tot += money[i]
    tot /= len(money)
    return tot

for i in range(0, len(choices)):
    money[choices[i] - 1] = 0

if offer < averag(money):
    print('no deal')
else:
    print('deal')