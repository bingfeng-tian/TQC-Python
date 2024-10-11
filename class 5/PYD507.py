# TODO

def compute(x):
    if x <= 1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True

x = int(input())
if compute(x):
    print("Prime")
else:
    print("Not Prime")

"""
Prime
Not Prime
"""