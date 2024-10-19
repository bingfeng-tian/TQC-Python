f_name = input()
n = int(input())

# TODO
file = open(f_name,"r",encoding='utf-8')
w = file.read()
sp = w.split()
set1 = sorted(set(sp))
for i in set1:
    if sp.count(i)==n:
        print(i)



file.close()
