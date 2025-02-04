cName = input("Enter customer name: ")
customerCredit = int(input("Enter credit: "))
incomePerYear = int(input("Enter income per year: "))
yearofEmployment = int(input("Enter year of employment: "))

if customerCredit >= 650 and incomePerYear >= 50000 and yearofEmployment >= 2:
   print("Dear" + " "+ cName + " " + "You are eligible for the loan")
else:
    print("Dear" + " "+ cName + " " + "You are not eligible for the loan")
    
    CN = "Kwame"
Principal = 37821
IR = 8  # Interest rate in percentage
time = 8  # Time in years

# Calculate interest
interest = Principal * (IR / 100) * time

# Calculate total amount to be paid
total_amount = Principal + interest

print(f"Client Name: {CN}")
print(f"Principal: {Principal}")
print(f"Interest Rate: {IR}%")
print(f"Time: {time} years")
print(f"Total Interest: {interest}")
print(f"Total Amount to be Paid: {total_amount}")