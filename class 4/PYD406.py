# TODO

while True:
    height = eval(input())
    if height==-9999:
        break
    weight = eval(input())
    if weight==-9999:
        break
    bmi = weight / ((height/100.0) ** 2)
    state = ""
    if bmi < 18.5:
        state = "under weight"
    elif bmi < 25 and bmi >= 18.5:
        state = "normal"
    elif bmi < 30 and bmi >= 25.0:
        state = "over weight"
    elif bmi >= 30:
        state = "fat"
        
    print(f"BMI: {bmi:.2f}\nState: {state}")


"""
fat
over weight
normal
under weight
BMI: _
State: _
"""