# import random
# min_value = 1 
# max_value = 6

# roll = random.randint(min_value, max_value)

# number = 100

# while  number > 0:
#     print(float(number))
#     number //= 2

def get_greeting(name):
    return f"Hi {name }"

message = get_greeting("Kwame")
file = open("content.txt", "w")
file.write(message)
