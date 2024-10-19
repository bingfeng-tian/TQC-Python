side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

#TODO
sum = side1+side2+side3
ma = max([side1,side2,side3])
if ma < sum-ma:
    print(sum)
else:
    print("Invalid")
