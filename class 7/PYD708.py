#TODO
x = {}

print("Create dict1:")
while True:
    key = input("Key: ")
    if key=="end":  break
    x[key] = input("Value: ")
    
y = {}
print("Create dict2:")
while True:
    key = input("Key: ")
    if key=="end":  break
    y[key] = input("Value: ")

x.update(y)
for i in sorted(x.keys()):
    print(f'{i}: {x[i]}')