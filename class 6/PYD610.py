#TODO

doC = []

for i in range(4):
    print(f"Week {i+1}:")
    for j in range(3):
        print(f'Day {j+1}:' ,end='')
        doC.append(eval(input()))

print(f"Average: {(sum(doC)/len(doC)):.2f}")
print(f"Highest: {max(doC)}")
print(f"Lowest: {min(doC)}")

"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""

"""
doC = [[23.1,24,23.5],
        [32,33,35.3],
        [29,30,26],
        [27.6,25,28.8]]
"""