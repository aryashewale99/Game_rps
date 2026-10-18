

import random

print("=" * 40)
print("      ROCK PAPER SCISSORS")
print("=" * 40)
print("      ✊ Rock")
print("      📄 Paper")
print("      ✂️ Scissors")
print("=" * 40)

player_score = 0
computer_score = 0

while True:
    player = input("\nEnter rock, paper, or scissors: ").lower()

    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("\nYou chose:     ", player)
    print("Computer chose:", computer)

    if player == computer:
        print("\n🤝 IT'S A DRAW!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("\n🎉 YOU WIN!")
        player_score += 1
    else:
        print("\n💻 COMPUTER WINS!")
        computer_score += 1

    print("-" * 40)
    print("       🏆 SCOREBOARD")
    print("-" * 40)
    print("Your score:    ", player_score)
    print("Computer score:", computer_score)
    print("-" * 40)

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing! 🎮")
        print("Final score:", player_score, "-", computer_score)
        break
