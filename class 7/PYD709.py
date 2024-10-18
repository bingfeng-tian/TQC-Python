#TODO
dit = {}

while True:
    key = input("Key: ")
    if key == "end":    break
    dit[key] = input("Value: ")

for i in sorted(dit.keys()):
    print(f'{i}: {dit[i]}')