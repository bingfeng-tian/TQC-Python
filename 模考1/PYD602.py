# TODO
poker = ['0','A','2','3','4','5','6','7','8','9',
         '10','J','Q','K']
total = 0
for _ in range(5):
    total += poker.index(input())

print(total)