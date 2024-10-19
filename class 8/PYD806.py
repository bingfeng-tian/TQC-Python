# TODO

def compute(s,f):
    c=0
    for i in s:
        if i==f:
            c+=1
    return c

s = input()
f = input()

print(f'{f} occurs {compute(s,f)} time(s)')