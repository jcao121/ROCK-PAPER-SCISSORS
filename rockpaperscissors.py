
game_score = 0
while game_score < 3:
    player1 = input("Rock, Paper or Scissors: ").lower()
    player2 = input("Rock, Paper or Scissors: ").lower()

    if player1 == "rock" and player2 == "scissors":
        print("Player 1 Wins")
        game_score += 1
        break
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins")
        game_score += 1
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins")
        game_score += 1
    elif player2 == "rock" and player1 == "scissors":
        print("Player 2 Wins")
        game_score += 1
    elif player2 == "paper" and player1 == "rock":
        print("Player 2 wins")
        game_score += 1
    elif player2 == "scissors" and player1 == "paper":
        print("Player 2 wins")
        game_score += 1
    else:
        print("Unrecognized Option")
