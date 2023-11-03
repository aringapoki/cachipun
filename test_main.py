import pytest
from main import play_game

def test_invalid_input():
    with pytest.raises(SystemExit):
        play_game("test", "invalid")

def test_computer_wins():
    result = play_game("test", "rock")
    assert "Computer wins" in result

def test_user_wins():
    result = play_game("test", "paper")
    assert "test wins" in result

def test_tie():
    result = play_game("test", "scissors")
    assert "Tie" in result