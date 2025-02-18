

newlist=["Bernard", "Kamau", "Mwangi", "Kiplangat", "Kipkoech"]

def add():
    userInput=input("Enter the number of elements you want to add to the list: ")
    if  userInput:
        newlist.append(userInput)
    else:
        print("enter something")
    
    print(newlist)


def delete():
    userInput=input("Enter the element you want to delete from the list: ")
    if userInput == "":
        print("Enter something")
    out = newlist.remove(userInput)
    if out not in newlist:
        print("Item not in list")
    print(newlist)


def update():
    userInput=input("Enter the element you want to update: ")
    if userInput not in newlist:
        print("Item not in list")
        if userInput == "":
            print("Enter something")
    userInput2=input("Enter the new element: ")
    uppdate = newlist[newlist.index(userInput)]=userInput2
    print(newlist)


def main():
    while True:
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
            continue

main()