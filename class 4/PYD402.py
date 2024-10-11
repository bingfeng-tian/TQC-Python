# TODO
n_list = []
while True:
    n=eval(input())
    n_list.append(n)
    if n==9999:
        break
print(min(n_list))