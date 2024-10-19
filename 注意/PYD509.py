import math

def compute(p,q):
    return math.gcd(p,q)

# TODO
x,y = eval(input())
m,n = eval(input())

p = x*n + m*y
q = y*n
gcd = compute(p,q)
print(f"{x}/{y} + {m}/{n} = {int(p/gcd)}/{int(q/gcd)}")