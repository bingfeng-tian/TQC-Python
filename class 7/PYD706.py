# TODO
n = int(input())
for i in range(n):
    a = [0]*26
    s = input().lower()
    for i in s:
        if i!=' ':
            index = ord(i) - ord('a')
            a[index] += 1
    
    if 0 in a:
        print('False')
    else:
        print('True')