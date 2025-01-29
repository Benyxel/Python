# ex 1

# List(Array)
numbers = [1, 2, 3]
numbers2 = [4, 2, 7]
print(numbers)
print(numbers2)

strings = ["a", "b", "c"]
print(strings)
booleans = [True]

print(booleans)
print(numbers[0])
print(strings[2])

# Dictionary (Object)

name_to_hungry =  {"Jack": False, "Jane": True, "Alax": True}
print(name_to_hungry)

name_to_burgers = {"Emily": 1, "Jenny": 2, "Neel": 3}
print(name_to_burgers)

name_to_name = {"Bernard": "Gifty", "Ike": "Regie", "Eben": "Bene"}
print(name_to_name)

age_to_name = {26: "Gifty", 31: "Regie", 23: "Bene"}
print(age_to_name)

print(name_to_hungry["Jane"])

print (name_to_burgers["Neel"])

# LIST of DICTIONARIES

list_of_dicts = [{"name": "Gifty", "hungry": False}, {"name": "Regie", "hungry": True}]
print(list_of_dicts)
print(list_of_dicts[0])
print(list_of_dicts[1])
print(list_of_dicts[0]["name"])
print(list_of_dicts[1]["hungry"])