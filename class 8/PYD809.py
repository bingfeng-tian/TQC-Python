# TODO
s = input()
if len(s)<8:
    print("Invalid password")
else: 
    Aan = [0,0,0]
    for i in s:
        if ord(i) < ord('9') and ord(i) > ord('0'):
            Aan[2]+=1
        elif ord(i) < ord('z') and ord(i) > ord('a'):
            Aan[1]+=1
        elif ord(i) < ord('Z') and ord(i) > ord('A'):
            Aan[0]+=1

    if 0 in Aan:
        print("Invalid password")
    else:
        print("Valid password")