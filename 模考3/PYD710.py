#TODO
dic = {}
while True:
    key = input("Key: ")
    if key=="end":  break
    dic[key] = input("Value: ")

print(input("Search key: ") in dic.keys())