height = []
weight = []

maxH = maxW = 0
Hname = Wname = ""

file = open("read.txt","r")
w = file.readlines()

for x in w:
    print(x)
    data = x.split()
    
    h = eval(data[1])
    w = eval(data[2])
    height.append(h)
    weight.append(w)
    
    if h > maxH:
        maxH = h
        Hname = data[0]
    
    if w > maxW:
        maxW = w
        Wname = data[0]
        
print(f"Average height: {sum(height)/len(height):.2f}")
print(f"Average weight: {sum(weight)/len(weight):.2f}")
print(f"The tallest is {Hname} with {maxH:.2f}cm")
print(f"The heaviest is {Wname} with {maxW:.2f}kg")

file.close()
