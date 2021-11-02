found = None

for i in "hello":
    if i == "q":
        found = True
        break
else:
    found = False

print(found)
