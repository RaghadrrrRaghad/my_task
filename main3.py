names = ["Tarteel", "Asmaa", "Ahmed"]
print(names)
names.insert(0, "Sabrin")
print(names)
names.pop()
print(names)
names.append("Hamda")
print(names)
del names[2]
print(names)

friends = ["Adel", "Ahmed"]
employees = ["Samah", "Amjad"]
School = ["Ali", "Basma"]

friends.extend(employees + School)
print(friends)