# TODO

print("The 1st student:")
st1 = [int(input()) for i in range(5)]
print("The 2nd student:")
st2 = [int(input()) for i in range(5)]
print("The 3rd student:")
st3 = [int(input()) for i in range(5)]

print("Student 1")
print(f"#Sum {sum(st1)}")
print(f"#Average {sum(st1)/5:.2f}")
print("Student 2")
print(f"#Sum {sum(st2)}")
print(f"#Average {sum(st2)/5:.2f}")
print("Student 3")
print(f"#Sum {sum(st3)}")
print(f"#Average {sum(st3)/5:.2f}")