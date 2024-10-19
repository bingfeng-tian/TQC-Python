#TODO
money = int(input())
e = float(input())
month = int(input())

#此為格式化輸出之標頭
print('%s \t  %s' % ('Month', 'Amount'))
total = money
#TODO
for i in range(month):
    total = total+total*e /1200
    print('%3d \t %.2f' % (i+1, total))