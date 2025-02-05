import random

options = ['rock', 'paper', 'scissors']

user_wins = 0

while True:
    user_input = input("Enter rock, paper, scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2) 
    computer_choice = options[random_number]  
    print(f"Computer chose {computer_choice}")
    
    if user_input == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1
        break
    elif user_input == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1
        break
    elif user_input == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1
        break
    elif user_input == computer_choice:
        print("It's a tie!")
        continue
    else:
        print("You lose!")
        break