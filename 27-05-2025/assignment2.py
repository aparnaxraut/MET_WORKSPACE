numbers=(3,5,9,-2,6,-7)
for item in numbers:
    if item in (-2,-7):
        break
print("first negative number is:",item)