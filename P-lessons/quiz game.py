


print("Welcome to the quiz game!")

playing = input("Do you want to play? ")
if playing.lower() != "yes": 
    print("Goodbye!")
    exit()

print("Let's start!")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ") 
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 
    
print(f"Your score is {score} out of 2")