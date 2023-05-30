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

def concatenate_dictionaries(*dicts):
    dict = {}
    for i in dicts:
        dict.update(i)
    return dict


dict1 = {'1': 10, '2': 20}
dict2 = {'3': 30, '4': 40}
dict3 = {'5': 50, '6': 60}

new_dict = concatenate_dictionaries(dict1, dict2, dict3)
print(new_dict)