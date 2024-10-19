f_name = input()
str_old = input()
str_new = input()

file = open(f_name,"r+")

print("=== Before the replacement")
s = file.read()
print(s)

print("=== After the replacement")
s = s.replace(str_old, str_new)
print(s)
file.seek(0)
file.write(s)

file.close()
