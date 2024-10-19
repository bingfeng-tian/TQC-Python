f_name = "read.dat"
m=f=0
# TODO
fp = open(f_name, "r", encoding="utf-8")
w = fp.readlines()
for i in w:
    print(i)
    sp = i.split()
    if sp[2]=="1":
        m+=1
    elif sp[2]=="0":
        f+=1

print(f'Number of males: {m}')
print(f'Number of females: {f}')

fp.close()
