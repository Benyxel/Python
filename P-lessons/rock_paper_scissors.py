import random

options = ['rock', 'paper', 'scissors']

user_wins = 0
computer_wins = 0

while True:
    # this part allows the user to quit the game or continue playing
    user_input = input("Enter rock, paper, scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    # this part allows the computer to choose a random option by using the index of the options list
    random_number = random.randint(0, 2) 
    
    # this part allows the computer to choose an option from the options list
    computer_choice = options[random_number] 
    
    # this part prints the computer's choice
    print(f"Computer chose {computer_choice}")
    
    # this part compares the user's input and the computer's choice to determine the winner
    if user_input == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1
    
    # this part compares the user's input and the computer's choice to determine the winner
    elif user_input == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1
    # this part compares the user's input and the computer's choice to determine the winner
    elif user_input == "scissors" and computer_choice == "paper":
        print("You win!")
        
        user_wins += 1
        
    # this part compares the user's input and the computer's choice to determine the winner
    elif user_input == computer_choice:
        print("It's a tie!")
    
    else:
        print("You lose!")
        computer_wins += 1
        
# 
print(f"You won {user_wins} times")
print(f"The computer won {computer_wins} times")
print("Goodbye!")