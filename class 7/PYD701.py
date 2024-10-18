# TODO

nums = []

while True:
    n = eval(input())
    if n == -9999:
        break
    else:
        nums.append(n)

tnums = tuple(nums)
print(tnums)
print(f"Length: {len(tnums)}")
print(f"Max: {max(tnums)}")
print(f"Min: {min(tnums)}")
print(f"Sum: {sum(tnums)}")


"""
Length: _
Max: _
Min: _
Sum: _
"""