# TODO
x = set()
y = set()

print("Enter group X's subjects:")
s = input()
while s!='end':
    x.add(s)
    s=input()

print("Enter group Y's subjects:")
s = input()
while s!='end':
    y.add(s)
    s=input()

print(sorted(x.union(y)))
print(sorted(x.intersection(y)))
print(sorted(y-x))
print(sorted(x.union(y)-x.intersection(y)))