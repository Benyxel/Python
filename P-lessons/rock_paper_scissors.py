options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Enter rock, paper, scissors or  Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    