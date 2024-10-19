# TODO
t = int(input())

for i in range(t):
    n = eval(input().replace(' ',','))
    print(f'{max(n)-min(n):.2f}')