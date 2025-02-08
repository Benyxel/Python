import random
min_value = 1 
max_value = 6

roll = random.randint(min_value, max_value)



while True:
    players = input("Enter a number of players(1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break


print(players)

