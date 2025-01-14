import random 
def roll():
    min=1
    max=6
    roll = random.randint(min, max) 
    return roll

while True: 
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if players>=1 and players<=4:
            break
        else:
            print("Invalid number of players. Please enter a number between 1 and 4.")
    else: 
        print("Invalid input. Please enter a number.")

max_score=60
player_score=[0 for _ in range(players)]
print(player_score)

while max(player_score)<max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index+1, "turn has just begun.\n")
        print ("Your total score is:", player_score[player_index], "\n")
        current_score=0
        while True: 
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break 
            value=roll()
            if value == 1:
                current_score=0
                print("You rolled a 1! Turn done!")
                break 
            else: 
                current_score +=value 
                print("You rolled a:", value)

            print("Your score is:", current_score) 
        
        player_score[player_index] += current_score
        print("Your total score is: ", player_score[player_index])

max_score=max(player_score)
winning_index= player_score.index(max_score)
print("Player number", winning_index+1, "is the winner with a score of",max_score )
