f = open("read.txt",'r')
# TODO
data = f.read()
sp = data.split(' ')
total = 0
for i in sp:
    total+=eval(i)
print(total)
f.close()