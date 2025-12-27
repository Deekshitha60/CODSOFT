import random

print("🎮 Rock - Paper - Scissors Game 🎮")

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    # User Input
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.\n")
        continue

    # Computer Selection
    computer_choice = random.choice(options)

    print(f"\nYou chose     : {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print("Result: It's a tie! 😐")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You win! 🎉")
        user_score += 1
    else:
        print("Result: You lose! 😢")
        computer_score += 1

    # Score Display
    print(f"\nScores:")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break

print("Final Scores:")
print(f"You      : {user_score}")
print(f"Computer : {computer_score}")