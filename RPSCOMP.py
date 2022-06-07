from random import choice
player1_score = 0
comp_score = 0
while player1_score != 3 and comp_score != 3:

    player1 = input("Rock, Paper or Scissors: ").lower()
    comp = choice(["Rock", "Paper", "Scissors"]).lower()
    print(f"Computer CHOOSES {comp}")
    if player1 == "rock" and comp == "scissors":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif player1 == "paper" and comp == "rock":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif player1 == "scissors" and comp == "paper":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif comp == "rock" and player1 == "scissors":
        comp_score += 1
        print(f"COMP WINS and has {comp_score} point")
    elif comp == "paper" and player1 == "rock":
        comp_score += 1
        print(f"COMP WINS and has {comp_score} point")
    elif comp == "scissors" and player1 == "paper":
        comp_score += 1
        print(f"COMP WINS and has {comp_score} point")
    elif player1 == comp:
        print("ITS A TIE! WE GO AGAN")
    else:
        print("Unrecognized Option")
