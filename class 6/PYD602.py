# TODO

poker_no = ['A','2','3','4','5','6','7',
            '8','9','10','J','Q','K']

sum = 0
for i in range(5):
    sum += poker_no.index(input())+1

print(sum)