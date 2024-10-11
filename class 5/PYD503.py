# TODO
def compute(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    return sum

a=int(input())
b=int(input())
print(compute(a,b))