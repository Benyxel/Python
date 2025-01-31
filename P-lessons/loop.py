from datetime import datetime
now = datetime.now()
nextBirthday =  datetime(datetime.now().year, 1, 31)
if now > nextBirthday:
    nextBirthday = datetime(datetime.now().year + 1, 1, 31)
print(nextBirthday)

# A while loop
while datetime.now() < nextBirthday:
    print("It is your birthday")

