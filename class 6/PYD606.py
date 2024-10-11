# TODO

def compute(lst):
    for i in lst:
        for j in i:
            print(f'{j:4d}',end='')
        print()
    
rows = int(input())
cols = int(input())

lst = []
for row in range(rows):
    lst.append([])
    for col in range(cols):
        lst[row].append(col-row)

compute(lst)