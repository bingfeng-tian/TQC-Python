# TODO

score = []
stdn = ['1st','2nd','3rd']
for i in range(3):
    print(f'The {stdn[i]} student:')
    score.append([])
    for j in range(5):
        score[i].append(int(input()))

id = 0
for std in score:
    sum = 0
    for i in std:
        sum+=i
    avg = sum/5
    id += 1
    print(f'Student {id}')
    print(f'#Sum {sum}')
    print(f'#Average {avg:.2f}')

        
    
"""
The _ student:
Student _
#Sum _
#Average _
"""
