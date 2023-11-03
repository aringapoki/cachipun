import random
import pytest

def play_game(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "User wins"
    else:
        return "Computer wins"

def test_play_game():
    random.seed(42)  # Fijamos la semilla para que los resultados sean predecibles
    assert play_game("rock", "scissors") == "User wins"
    assert play_game("rock", "rock") == "Tie"
    assert play_game("scissors", "paper") == "User wins"
    assert play_game("paper", "rock") == "User wins"
    assert play_game("rock", "paper") == "Computer wins"
    assert play_game("paper", "scissors") == "Computer wins"

if __name__ == "__main":
    pytest.main()
