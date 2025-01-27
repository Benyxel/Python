cName = input("Enter customer name: ")
customerCredit = int(input("Enter credit: "))
incomePerYear = int(input("Enter income per year: "))
yearofEmployment = int(input("Enter year of employment: "))

if customerCredit >= 650 and incomePerYear >= 500000 and yearofEmployment >= 2:
   print("Dear" + " "+ cName + "You are eligible for the loan")