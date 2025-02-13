import random
name = input("Enter your name: ")
print("Welcome to the Game!",name)

words = ['rainbow', 'computer', 'science', 'programming']
word = random.choice(words)
print("Guess the Word")


guesses = ''
turns = 12 

while turns > 0:
    faild = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            faild += 1
    if faild == 0:
        print("You Win")
        print("The word is: ",word)
        break
    guess = input("Guess a character: ").lower()
    if guess == "quit":
        print("Game Over")
        quit()
        
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have",turns,"more guesses")
        if turns == 0:
            print("You Loose")
    
    if turns == 0:
        print("The word is: ",word)