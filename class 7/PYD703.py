# TODO

data = []
s = input()
while s != "end":
    data.append(s)
    s = input()    

t = tuple(data)
print(t)
print(t[0:3])
print(t[-3:])