"""
Number Guessing Game
=====================
PRODIGY INFOTECH - Python Programming Internship
Task 02: Guessing Game

WHAT THIS PROGRAM DOES
-----------------------
The program randomly generates a secret number inside a range chosen
by the player. The player repeatedly enters a guess and receives
"too high" / "too low" feedback after every attempt. The game keeps
going until the secret number is guessed correctly, at which point
the total number of attempts is displayed.

Extra touches added on top of the core requirement:
  * Three difficulty levels (Easy / Medium / Hard) that change the range
  * Friendly validation of bad input (letters, decimals, out-of-range)
  * A "getting warm" hint when a guess is close to the target
  * Duplicate-guess detection
  * A performance rating and a running "best score" for the session
  * A "play again" loop so multiple rounds can be played without
    restarting the program

Run with:
    python guessing_game.py
"""

import random
import sys

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

APP_TITLE = "NUMBER GUESSING GAME"
LINE_WIDTH = 56

# Each difficulty maps to (display name, lowest number, highest number)
DIFFICULTIES = {
    "1": ("Easy", 1, 50),
    "2": ("Medium", 1, 100),
    "3": ("Hard", 1, 500),
}


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def print_line(char="="):
    """Print a full-width divider line."""
    print(char * LINE_WIDTH)


def print_header():
    """Print the game's title banner."""
    print_line()
    print(APP_TITLE.center(LINE_WIDTH))
    print_line()
    print("I have picked a secret number. Try to guess it!")
    print_line()


# ---------------------------------------------------------------------------
# Input handling
# ---------------------------------------------------------------------------

def choose_difficulty():
    """Ask the player to pick a difficulty and return (name, low, high)."""
    print("\nChoose a difficulty level:")
    print("  1) Easy    -> numbers between 1 and 50")
    print("  2) Medium  -> numbers between 1 and 100")
    print("  3) Hard    -> numbers between 1 and 500")

    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid input. Please type 1, 2, or 3.")


def read_guess(low, high):
    """Keep asking until the player enters a valid whole number in range."""
    while True:
        raw_value = input(f"Your guess ({low}-{high}): ").strip()

        try:
            guess = int(raw_value)
        except ValueError:
            print(f">> '{raw_value}' is not a whole number. Try again.\n")
            continue

        if not (low <= guess <= high):
            print(f">> Please enter a number between {low} and {high}.\n")
            continue

        return guess


# ---------------------------------------------------------------------------
# Game logic
# ---------------------------------------------------------------------------

def hint_for(guess, target, low, high):
    """Return feedback text for a wrong guess, including a closeness hint."""
    span = max(high - low, 1)
    closeness = abs(guess - target) / span
    direction = "LOW" if guess < target else "HIGH"

    if closeness <= 0.03:
        return f"Too {direction}... but you're SO close!"
    if closeness <= 0.10:
        return f"Too {direction}, and getting warm."
    return f"Too {direction}."


def play_round():
    """Play a single round and return the number of attempts taken."""
    level_name, low, high = choose_difficulty()
    target = random.randint(low, high)

    print(f"\nGreat! I'm thinking of a number between {low} and {high} ({level_name} mode).")
    print("Let's begin!\n")

    attempts = 0
    guessed_values = set()

    while True:
        guess = read_guess(low, high)

        if guess in guessed_values:
            print(f">> You already tried {guess}. Pick a different number.\n")
            continue

        guessed_values.add(guess)
        attempts += 1

        if guess == target:
            print(f"\nCorrect! The number was {target}.")
            plural = "s" if attempts != 1 else ""
            print(f"You guessed it in {attempts} attempt{plural}.")
            return attempts

        print(hint_for(guess, target, low, high) + "\n")


def rate_performance(attempts):
    """Return a short comment based on how many attempts were used."""
    if attempts <= 3:
        return "Outstanding! Are you psychic?"
    if attempts <= 6:
        return "Nicely done!"
    if attempts <= 10:
        return "Good job, you got there!"
    return "Phew, that was a close one! Practice makes perfect."


# ---------------------------------------------------------------------------
# Program entry point
# ---------------------------------------------------------------------------

def main():
    print_header()

    games_played = 0
    best_score = None

    while True:
        attempts = play_round()
        games_played += 1
        best_score = attempts if best_score is None else min(best_score, attempts)

        print(rate_performance(attempts))
        print(f"Games played: {games_played}  |  Best score: {best_score}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThanks for playing. Goodbye!")
            break
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame ended. Goodbye!")
        sys.exit(0)
