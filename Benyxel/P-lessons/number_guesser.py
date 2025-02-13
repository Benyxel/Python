import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print (" Please type a number leager than 0 next time")
        quit()
else:
    print("please type a number next time")
    quit()
    

rNumber = random.randint(0 , top_of_range)

guesses = 0

while True:
    guesses += 1
    guess_input = input("Make a guess: ")
    if guess_input.isdigit():
        guess_input = int(guess_input)
    
        if guess_input == rNumber:
            print("You got it!")
            break
        elif guess_input > rNumber:
            print("You were above the number")
        else:
            print("You were below the number")
    else:
        print("Please type a number")
        
print(f"You got it in {guesses} guesses")