def rps_winner(player1,player2):
    if player1 == player2:
        return "It's a tie!"
    elif(player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins!"
    elif(player2 == 'rock' and player1 == 'scissors') or (player2 == 'scissors' and player1 == 'paper') or (player2 == 'paper' and player1 == 'rock'):
        return "Player 2 wins!"
    else:
        return "Invalid input! Please enter rock, paper, or scissors."

player1 = input("Player 1, enter your choice (rock, paper, scissors): ").strip().lower()
player2 = input("Player 2, enter your choice (rock, paper, scissors): ").strip().lower()

result = rps_winner(player1,player2)
print(result)