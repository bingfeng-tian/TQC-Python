#TODO
money = eval(input())
r = float(input())
month = eval(input())

#此為格式化輸出之標頭
print('%s \t  %s' % ('Month', 'Amount'))
#TODO
total=money
for i in range(1,month+1):
    #此為格式化輸出之內容，需置於置於迴圈中
    total = total + total * r / 1200 
    print('%3d \t %.2f' % (i, total))