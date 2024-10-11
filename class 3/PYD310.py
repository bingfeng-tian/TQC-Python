# TODO
n = eval(input())

sum = 0
for i in range(1,n):
    sum += 1/(pow(i,0.5)+pow(i+1,0.5))
print(f'{sum:.4f}')