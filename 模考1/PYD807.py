# TODO

s = input()
d = s.split()
t = 0
for i in d:
    t += eval(i)

print(f'Total = {t}')
print(f'Average = {t/5:.1f}')