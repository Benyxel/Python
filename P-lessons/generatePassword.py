from random import choice
from string import ascii_letters, digits

characters = ascii_letters + digits
length = int(input("Enter the length of the password: "))

password = ""
for i in range(length):
    character = choice(characters)
    password = password + character
print(password)