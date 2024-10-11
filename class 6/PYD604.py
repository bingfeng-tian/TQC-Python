# TODO

n = []

for i in range(10):
    n.append(int(input()))

mode = 0
mode_t = 1

for i in n:
    t = n.count(i)
    if t > mode_t:
        mode = i
        mode_t = t
    
print(mode)
print(mode_t)