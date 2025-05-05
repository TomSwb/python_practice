import random

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:

    # Display the game instructions
    print("\nLet's play rock, paper, or scissors")
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate input
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Randomly select the computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
        winner = "Player"
    elif player_choice == computer_choice:
        winner = "Tie"
    else:
        winner = "Computer"

    # Announce the result of the round
    if winner == "Player":
        print("You won")
        player_wins += 1
    elif winner == "Computer":
        print("Computer won")
        computer_wins += 1
    else:
        print("It's a tie")

    # Display the current score
    print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

# End of the game - announce the overall winner
if player_wins > computer_wins:
    print("\nCongratulations! You won.")
else:
    print("\nComputer won!")
