# TODO

def compute(rows,cols):
    for row in range(rows):
        for col in range(cols):
            print(f'{col-row:4d}', end='')
        print()

rows = eval(input())
cols = eval(input())
compute(rows,cols)
