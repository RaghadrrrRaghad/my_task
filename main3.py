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


def square_of_the_keys():
    my_dict = {}
    for i in range(1, 16):
        square = i*i
        my_dict[i] = square

    return my_dict

print(square_of_the_keys())


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 150, 'b': 200, 'd': 400}


def combine_dictionaries(dict1, dict2):
     combined_dict = dict1.copy()
     for k, v in dict2.items():
         if k in combined_dict:
             combined_dict[k] += v
         else:
             combined_dict[k] = v

     return combined_dict

d = combine_dictionaries(d1, d2)
print(d)


keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

def my_dictionary(k, v):
    my_dictionary = {}
    count = 0
    for i in k:
        my_dictionary[i] = v[count]
        count+= 1

    return my_dictionary

print(my_dictionary(keys, values))