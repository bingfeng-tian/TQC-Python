# TODO

def compute(x,y):
    gcd = 1
    for i in range(2,min(x,y)):
        if x%i==0 and y%i==0: 
            gcd = i
            break
    return gcd

(x, y) = eval(input())
print(compute(x,y))