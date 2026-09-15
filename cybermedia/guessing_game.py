"""A small terminal number guessing game."""

import random


def play_round() -> bool:
    secret_number = random.randint(1, 20)
    attempts = 0

    print("\nI am thinking of a number from 1 to 20.")

    while True:
        answer = input("Your guess: ").strip()

        try:
            guess = int(answer)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 20:
            print("Choose a number between 1 and 20.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"You got it in {attempts} guess(es)!")
            return True


def main() -> None:
    print("=== Number Guessing Game ===")

    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
