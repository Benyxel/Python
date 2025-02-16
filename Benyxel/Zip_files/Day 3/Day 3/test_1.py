# dictionary: key valued pairs
# dict() contructor
# dictionary = {"key": "value"} - the keys are to the left and the values are to the right of a colon
# keys and values: it can be of any datatype
# a key can only exist once in a dictionary

data = {}

person = input("Enter your name: ")
age = input("Enter your age: ")

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(car)

# # accessing a dictionary
# print(car.get("year"))
# print(car["brand"])

# # getting the keys
# print(car.keys())

# adding items into a dictionary

# data["person"] = person
# data["age"] = age
data.update({"person": person, "age": age})
print(data)