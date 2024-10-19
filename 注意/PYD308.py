# TODO
time = int(input())

for _ in range(time):
    s = input()
    n = [int(i) for i in list(s)]
    print(f"Sum of all digits of {s} is {sum(n)}")