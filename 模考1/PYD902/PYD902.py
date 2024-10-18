f = open("read.txt",'r')

# TODO
s = f.read()
ss = s.split(' ')
total = 0
for i in ss:
    total += eval(i)
print(total)

f.close()