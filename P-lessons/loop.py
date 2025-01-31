from datetime import datetime
now = datetime.now()
nextBirthday =  datetime(datetime.now().year, 1, 30)
if now > nextBirthday:
    nextBirthday = datetime(datetime.now().year + 1, 1, 30)
print(nextBirthday)