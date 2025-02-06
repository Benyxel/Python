import random

options = ["rock", "scissors", "paper"]
user_wins = 0
computer_wins = 0
tie = 0

while True:
	user_input = input("Enter rock, scissors, paper or Q to quit: ").lower()
	if user_input == "q":
		break
	elif user_input not in options:
		continue

	random_number = random.randint(0, 2)
	computer_pick = options[random_number]

	if computer_pick == "rock" and user_input == "paper":
		print("You won")
		user_wins += 1
	elif computer_pick == "scissors" and user_input == "rock":
		print("You won")
		user_wins += 1
	elif computer_pick == "paper" and user_input == "scissors":
		print("You won")
		user_wins += 1
	elif computer_pick == user_input:
		print("You tie")
		tie += 1
	else:
		print("You lost")
		computer_wins += 1

print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")
print(f"Tie {tie} times")
print("Goodbye")