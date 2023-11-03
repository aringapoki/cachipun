import random

user_name = input("Enter your name: ")
options = ("rock", "paper", "scissors")

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print(f"***** ROUND: {rounds} *****")
    print(f"Computer wins: {computer_wins}")
    print(f"{user_name} wins: {user_wins}")

    user_choice = input("Enter a choice (rock, paper, scissors): ")
    user_choice = user_choice.lower()

    rounds += 1

    if not user_choice in options:
        print("Invalid input, try again.")
        continue

    computer_choice = random.choice(options)

    if computer_choice == user_choice:
        print("Tie")
    elif computer_choice == "rock":
        if user_choice == "scissors":
            print("Computer wins")
            computer_wins += 1
        else:
            print(f"{user_name} wins")
            user_wins += 1
    elif computer_choice == "paper":
        if user_choice == "rock":
            print("Computer wins")
            computer_wins += 1
        else:
            print(f"{user_name} wins")
            user_wins += 1
    elif computer_choice == "scissors":
        if user_choice == "paper":
            print("Computer wins")
            computer_wins += 1
        else:
            print(f"{user_name} wins")
            user_wins += 1

    if computer_wins == 3:
        print("Computer won the game!")
    elif user_wins == 3:
        print(f"{user_name} won the game!")
