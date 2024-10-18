# TODO
def compute(p,q):
    gcd = 1
    mi = min(p,q)
    for i in range(2,mi):
        if p%i==0 and q%i==0:
            gcd = i
    return gcd

x, y = eval(input())
m, n = eval(input())
p = x*n + m*y
q = y*n

gcd = compute(p,q)
print(f'{x}/{y} + {m}/{n} = {int(p/gcd)}/{int(q/gcd)}')