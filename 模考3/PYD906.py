f_name = input()
str_old = input()
str_new = input()
fp = open(f_name, "r", encoding="utf-8")

print("=== Before the replacement")
data = fp.read() 
print(data)

print("=== After the replacement")
fp = open(f_name, "w", encoding="utf-8")
data = data.replace(str_old, str_new)
print(data)
fp.seek(0)
fp.write(data)

fp.close()
