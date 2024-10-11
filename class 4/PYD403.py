# TODO

a=int(input())
b=int(input())

lst = []
for i in range(a,b+1):
    if i%4==0 or i%9==0:
       lst.append(i)

sum=0
c=0
for i in lst:
    print(f'{i:<4d}', end='')
    sum+=i
    c+=1
    if c%10==0 or c==lst.__len__():
        print()
print(c)
print(sum)