Task = []

def AddTask():
    TaskName = input('Enter Your Task: ')
    Task.append(TaskName)
    print(f"Task '{TaskName}' added!")

def ViewTasks():
    if Task:
        print("\nYour Tasks:")
        for i, task in enumerate(Task, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found!")

def DeleteTask():
    ViewTasks()
    if Task:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(Task):
                removed = Task.pop(index)
                print(f"Task '{removed}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

# Main menu
while True:
    print("\n1. Add Task")
    print("2. View Tasks") 
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        AddTask()
    elif choice == "2":
        ViewTasks()
    elif choice == "3":
        DeleteTask()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")