#TODO
d = {}

while True:
    key = input("Key: ")
    if key=="end":  break
    d[key] = input("Value: ")

k = input("Search key: ")
print(k in d)