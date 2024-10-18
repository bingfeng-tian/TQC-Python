file = open("write.txt",'w')

# TODO
for i in range(5):
    file.write(input()+"\n")
file.close()