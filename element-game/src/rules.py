Actions = {
    "Spirit": {"Air", "Earth"},
    "Air": {"Earth", "Fire"},
    "Earth": {"Fire", "Water"},
    "Fire": {"Water", "Spirit"},
    "Water": {"Spirit", "Air"},
}

def DetermineWinner(Player1Choice, Player2Choice):
    """Determine the winner between two elements."""
    if Player1Choice == Player2Choice:
        return None  # It's a tie
    elif Player2Choice in Actions[Player1Choice]:
        return "Player 1"
    else:
        return "Player 2"