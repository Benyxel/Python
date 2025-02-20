

newlist=["Bernard", "Kamau", "Mwangi", "Kiplangat", "Kipkoech"]

def add():
    userInput=input("Enter elements you want to add to the list: ")
    if  userInput:
        newlist.append(userInput)
        print(f"{userInput} has been added to the list")
    else:
        print("enter something")
    



def delete():
    userInput=input("Enter the element you want to delete from the list: ")
    if userInput == "":
        print("Enter something")
    elif userInput not in newlist:
        print("Item not found")
    else:
        newlist.remove(userInput)
        print(f"{userInput} has been removed from the list")


def update():
    userInput=input("Enter the element you want to update: ")
    
    if userInput == "":
        print("Enter something")
    elif userInput not in newlist:
        print("Item not found")
    else:
        userInput2=input("Enter the new element: ")
        newlist[newlist.index(userInput)]=userInput2
        print(f"{userInput} has been updated to {userInput2}")


def main():
        print("Please select an option: ")
        print("1 to add, ")
        print("2 to delete,")
        print("3 to update")
        
        userInput=int(input("Enter your choice: "))
        
        if userInput==1:
            add()
        elif userInput==2:
            delete()
        elif userInput==3:
            update()
        else:
            print("Invalid choice")
            

main()
