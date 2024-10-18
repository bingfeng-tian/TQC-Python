# TODO
t1 = []
t2 = []

print("Create tuple1:")
# TODO
num = eval(input())
while num != -9999:
    t1.append(num)
    num = eval(input())

print("Create tuple2:")
# TODO
num = eval(input())
while num != -9999:
    t2.append(num)
    num = eval(input())

com = tuple(t1+t2)
print(f"Combined tuple before sorting: {com}")

print(f"Combined list after sorting: {sorted(t1+t2)}")
