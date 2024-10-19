# TODO
s = input()
d = s.split(' ')

total = 0
for i in d:
    total += int(i)

print(f"Total = {total}")
print(f"Average = {total/5:.1f}")