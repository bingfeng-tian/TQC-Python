# TODO

def compute(a,b,c):
    d = b**2-4*a*c
    if d >0:
        s1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
        s2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        print(f'{s1}, {s2}')
    elif d==0:
        print(-b/(2*a))
    else:
        print("Your equation has no root.")
a = eval(input())
b = eval(input())
c = eval(input())
compute(a,b,c)

"""
Your equation has no root.
"""