f_name = "data.dat"
file = open(f_name,"w")

# TODO
for _ in range(5):
    file.write(input()+ "\n")

print("The content of \"data.dat\":")
file = open(f_name,"r")
for i in file:
    print(i)

file.close()