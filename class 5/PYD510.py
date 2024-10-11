# TODO

def compute(num):
    if num <= 1:
        return num
    else:
        return compute(num-1)+compute(num-2)



num = int(input())
for i in range(num):
    print(compute(i),end=' ')
