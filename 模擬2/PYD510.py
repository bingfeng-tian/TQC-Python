# TODO
def compute(num):
    if num == 0 or num == 1:
        return num
    else:
        return compute(num-1)+compute(num-2)
    
n = int(input())
for i in range(n):
    print(compute(i),end=' ')