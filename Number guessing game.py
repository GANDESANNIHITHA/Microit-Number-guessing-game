import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    
    while True:
        lower_bound = 1
        upper_bound = 100
        secret_number = random.randint(lower_bound, upper_bound)
        max_attempts = 7

        print(f"\nI'm thinking of a number between {lower_bound} and {upper_bound}.")
        print(f"You have {max_attempts} attempts to guess it correctly.\n")

        for attempt in range(1, max_attempts + 1):
            try:
                guess = int(input(f"🔢 Attempt {attempt}: Enter your guess → "))
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            if guess < lower_bound or guess > upper_bound:
                print(f"⚠️ Please guess a number between {lower_bound} and {upper_bound}.")
                continue

            if guess < secret_number:
                if abs(guess - secret_number) <= 5:
                    print("📉 Too low, but very close!")
                else:
                    print("📉 Too low!")
            elif guess > secret_number:
                if abs(guess - secret_number) <= 5:
                    print("📈 Too high, but very close!")
                else:
                    print("📈 Too high!")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempt} attempts!")
                break
        else:
            print(f"😢 You've run out of attempts. The correct number was {secret_number}.")

        # Ask the user if they want to play again
        play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye!")
            break

# Run the game
number_guessing_game()
