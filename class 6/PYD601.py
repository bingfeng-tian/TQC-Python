# TODO

nums = []
sum = 0
for i in range(12):
    n = int(input())
    nums.append(n)
    if i%3==2:
        print(f'{n:>3d}')
    else:
        print(f'{n:>3d}',end='')
    
    if i%2==0:
        sum+=n

print(sum)