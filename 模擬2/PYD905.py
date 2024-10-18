f_name = input()
string = input()
# TODO

with open(f_name,"r+",encoding='utf-8') as file:
    data = file.read()

    print("=== Before the deletion")
    print(data)

    print("=== After the deletion")
    data = data.replace(string,'')
    print(data) 
    file.seek(0)
    file.write(data)