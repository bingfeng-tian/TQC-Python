# TODO
time = eval(input())

for i in range(time):
    n = eval(input())
    y = n
    sum=0
    while n >0:
        d = n%10
        sum += d
        y //= 10

    print(f'Sum of all digits of {y} is {sum}')



"""
Sum of all digits of _ is _
"""