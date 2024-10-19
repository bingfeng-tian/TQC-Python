# TODO
fname = input()
lines = words = character = 0

with open(fname, "r", encoding="utf-8") as file:
    for line in file:
        lines+=1
        words += len(line.split())
        character += sum([len(c) for c in line.split()])

print(f'{lines} line(s)')
print(f'{words} word(s)')
print(f'{character} character(s)')