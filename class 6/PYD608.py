# TODO

n = []
for i in range(3):
    n.append([])
    for j in range(3):
        n[i].append(int(input()))

maxm = [n[0][0],0,0]
minm = [n[0][0],0,0]

for i in range(3):
    for j in range(3):
        if n[i][j]>maxm[0]:
            maxm[0] = n[i][j]
            maxm[1] = i
            maxm[2] = j
        if n[i][j]<minm[0]:
            minm[0] = n[i][j]
            minm[1] = i
            minm[2] = j
            
print(f'Index of the largest number {maxm[0]} is: ({maxm[1]}, {maxm[2]})')
print(f'Index of the smallest number {minm[0]} is: ({minm[1]}, {minm[2]})')

"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""