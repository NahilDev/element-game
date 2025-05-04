import os
from rules import Actions, DetermineWinner

def main():
    print("Welcome to the Element Game!")
    print("Elements: Spirit, Air, Earth, Fire, Water")
    
    Player1Score = 0
    Player2Score = 0
    Rounds = 7

    for RoundNumber in range(1, Rounds + 1):
        print(f"\nRound {RoundNumber}:")
        
        # Get Player 1's choice
        Player1Choice = input("Player 1, choose your element: ").capitalize()
        os.system('cls')  # Clear the terminal
        
        # Get Player 2's choice
        Player2Choice = input("Player 2, choose your element: ").capitalize()
        os.system('cls')  # Clear the terminal

        # Validate choices
        if Player1Choice not in Actions or Player2Choice not in Actions:
            print("Invalid choice. Please choose from Spirit, Air, Earth, Fire, Water.")
            continue

        # Determine the winner
        Winner = DetermineWinner(Player1Choice, Player2Choice)

        if Winner == "Player 1":
            Player1Score += 1
            print("Player 1 wins this round!")
        elif Winner == "Player 2":
            Player2Score += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

        # Display current scores
        print(f"Score - Player 1: {Player1Score}, Player 2: {Player2Score}")

    # Determine the overall winner
    if Player1Score > Player2Score:
        print("\nPlayer 1 wins the game!")
    elif Player2Score > Player1Score:
        print("\nPlayer 2 wins the game!")
    else:
        print("\nThe game ends in a tie!")

if __name__ == "__main__":
    main()