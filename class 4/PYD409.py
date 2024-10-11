# TODO
N = C = Nu = 0
for i in range(5):
    v = int(input())
    if v==1:
        N+=1
    elif v==2:
        C+=1
    else:
        Nu+=1
    print(f"Total votes of No.1: Nami =  {N}")
    print(f"Total votes of No.2: Chopper =  {C}")
    print(f"Total null votes =  {Nu}")

if N>C:
    print("=> No.1 Nami won the election.")
elif C>N:
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")

"""
Total votes of No.1: Nami = _
Total votes of No.2: Chopper = _
Total null votes = _

=> No.1 Nami won the election.
=> No.2 Chopper won the election.
=> No one won the election.
"""
