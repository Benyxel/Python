yourName = input("Enter your name: ")

studentGpa = float(input( yourName + " " + "Enter your GPA: "))

studentCredits = int(input( "Almost done" + " " + "Enter your credits: "))

if studentGpa >= 3.5 and studentCredits >= 120:
    print("Contragulations!" + " " + yourName + " " + "You are Eligible.")
else: 
    print( "Dear" +" " + yourName + " " +"You need 3.5 GPA atleast and 120 credits atleast to be Honored")