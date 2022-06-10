player1_score = 0  # I wanted to keep score so added variable, need to use while loop for these variables to be useful
player2_score = 0
while player1_score != 3 and player2_score != 3:
    # had issue with while loop not working because I kept setting conditions that were true so, it kept running
    # while loop runs until it is false so needed to do opposite
    player1 = input("YOU ARE PLAYER1! Please Choose Rock, Paper or Scissors: ").lower() # added user input and .lower so it would not be case-sensitive
    player2 = input("YOU ARE PLAYER2! Please Choose Rock, Paper or Scissors: ").lower()

    if player1 == "rock" and player2 == "scissors":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point") # Added F-string to keep track of points
    elif player1 == "paper" and player2 == "rock":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif player1 == "scissors" and player2 == "paper":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif player2 == "rock" and player1 == "scissors":
        player2_score += 1
        print(f"PLAYER 2 WINS and has {player2_score} point")
    elif player2 == "paper" and player1 == "rock":
        player2_score += 1
        print(f"PLAYER 2 WINS and has {player2_score} point")
    elif player2 == "scissors" and player1 == "paper":
        player2_score += 1
        print(f"PLAYER 2 WINS and has {player2_score} point")
    elif player1 == player2:
        print("ITS A TIE! WE GO AGAN")
    else:
        print("Unrecognized Option")
