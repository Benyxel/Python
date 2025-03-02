try:
    exec("(print(noremmm)")
except SyntaxError:
    print("syntax occured")
except NameError:
    print("An error occured")
except:
    print("An error occured")
else:
    print("An error occured")