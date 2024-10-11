#TODO

m1 = [[0,0],[0,0]]
m2 = [[0,0],[0,0]]


print("Enter matrix 1:")
#TODO
for i in range(2):
        for j in range(2): 
                #置於迴圈內，依給定之格式輸出
                print("[%d, %d]: " % (i+1, j+1), end = '')
                m1[i][j] = int(input())
    

print("Enter matrix 2:")
#TODO
for i in range(2):
        for j in range(2): 
                #置於迴圈內，依給定之格式輸出
                print("[%d, %d]: " % (i+1, j+1), end = '')
                m2[i][j] = int(input())

print("Matrix 1:")
#TODO
for i in range(2):
        print(f'{m1[i][0]} {m1[i][1]} ')
print("Matrix 2:")
#TODO
for i in range(2):
        print(f'{m2[i][0]} {m2[i][1]} ')

print("Sum of 2 matrices:")
#TODO
for i in range(2):
        for j in range(2):
                print(f'{m1[i][j]+m2[i][j]} ',end='')
        print()
