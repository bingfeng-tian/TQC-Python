# TODO

score = []
sum = 0
for i in range(10):
    n = int(input())
    sum += n
    score.append(n)

sum -= max(score)+min(score)

print(sum)
print(f'{sum/8:.2f}')

