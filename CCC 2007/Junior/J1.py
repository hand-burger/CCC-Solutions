#Simply get input and compare

weight1, weight2, weight3 = input().split()

if(weight1 <= weight2 and weight1 >= weight3 or weight1 <= weight3 and weight1 >= weight2):
    print(weight1)
elif(weight2 <= weight1 and weight2 >= weight3 or weight2 <= weight3 and weight2 >= weight1):
    print(weight2)
else:
    print(weight3)