# try:
#     exec("(print(noremmm)")
# except SyntaxError:
#     print("syntax occured")
# except NameError:
#     print("An error occured")
# except:
#     print("An error occured")
# else:
#     print("An error occured")

def data():
    name = input("enter your name: ")
    age = int(input("enter your age: "))
    print("\n")
    print(name)
    print(age)


while True:
    try:
        data()
        # print(x)
    except ValueError as err:
        print(f"Error: {err}. Please enter the right numeric data as age and not text.")
    except: 
        print("an error occured")
    else:
        break