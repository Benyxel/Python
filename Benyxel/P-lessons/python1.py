import random

count = 0
chances = 7 
guesses = random.randrange(1,100)

while count < chances:
    userinput = int(input("Enter your guess: "))
    if userinput == guesses:
        print("you got it right")
        break
    elif userinput < guesses:
        print("your guess is too low")
        count += 1
        print("you have",chances - count,"chances left")
        continue
        
    elif userinput > guesses:
        print("your guess is too high")
        count += 1
        print("you have",chances - count,"chances left")
        continue
        
    elif count == chances:
        print("Game over")
        break
print("The number is",guesses)