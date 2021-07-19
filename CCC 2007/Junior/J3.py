#Get input, set the respective elements of money to zero, get average and compare to the offer

import numpy as np
choices = []
money = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

cases = int(input())

for i in range(0, cases):
    ele = int(input())
    choices.append(ele)

offer = int(input())

for i in range(0, len(choices)):
    money[choices[i] - 1] = 0

if offer < np.average(money):
    print('no deal')
else:
    print('deal')