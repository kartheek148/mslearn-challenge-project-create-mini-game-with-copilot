import random

# Initialize scores and rounds
user_score = 0
computer_score = 0
rounds = 0

while True:
    # Increment rounds
    rounds += 1

    # Read user choice and store
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    valid_choices = ['rock', 'paper', 'scissors']

    if user_choice not in valid_choices:
        print("Error: Invalid choice. Please enter either 'rock', 'paper', or 'scissors'.")
        continue

    # Generate random choice from computer
    computer_choice = random.choice(valid_choices)

    print(f"Computer choice: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        result = "User wins!"
    else:
        computer_score += 1
        result = "Computer wins!"

    print(result)
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")

    # Ask user to continue or exit
    continue_game = input("Do you want to continue? (Yes/No): ").lower()
    if continue_game != 'yes':
        if user_score > computer_score:
            print("User is the overall winner!")
        elif computer_score > user_score:
            print("Computer is the overall winner!")
        else:
            print("It's a tie overall!")
        print(f"Total rounds played: {rounds}")
        break