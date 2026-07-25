# PRODIGY_02
# 🎯 Number Guessing Game

A console-based number guessing game built in Python for **Task 02** of the
**PRODIGY INFOTECH** Programming Internship.

The program secretly picks a random number inside a range you choose. You
keep guessing, getting a **"too high"** or **"too low"** hint after every
try, until you land on the exact number — then it tells you how many
attempts it took.

---

## 📋 Task Description

> Build a program that generates a random number and challenges the user
> to guess it. The program should prompt the user to input their guess,
> compare it to the generated number, and provide feedback if the guess
> is too high or too low. It should continue until the user correctly
> guesses the number and then display the number of attempts it took to
> win the game.

## ✨ Features

- 🎲 Random number generation using Python's built-in `random` module
- 🕹️ Three selectable difficulty levels — Easy (1–50), Medium (1–100),
  and Hard (1–500)
- 🔁 Keeps prompting until the correct number is guessed — no attempt limit
- 📈 "Too high" / "too low" feedback after every guess, plus an extra
  "getting warm" / "SO close" hint the nearer you get
- 🛡️ Input validation — non-numeric and out-of-range guesses are rejected
  with a friendly message instead of crashing the program
- 🚫 Detects and blocks re-using a guess you already made
- 🔢 Tracks and displays the total number of attempts
- 🏆 Rates your performance and keeps your best score for the session
- 🔄 "Play again" loop to play multiple rounds without restarting

## 🖥️ Demo

<p align="center">
  <img src="screenshots/gameplay-medium.png" alt="Medium mode gameplay" width="640"><br>
  <em>A full round on Medium difficulty</em>
</p>

<p align="center">
  <img src="screenshots/gameplay-validation.png" alt="Input validation demo" width="640"><br>
  <em>Handling invalid, out-of-range, and repeated guesses</em>
</p>

<p align="center">
  <img src="screenshots/gameplay-replay.png" alt="Replay and scoring demo" width="640"><br>
  <em>Hard mode, then "play again" into an Easy round with running best score</em>
</p>

### Sample output (text)

```
========================================================
                  NUMBER GUESSING GAME
========================================================
I have picked a secret number. Try to guess it!
========================================================

Choose a difficulty level:
  1) Easy    -> numbers between 1 and 50
  2) Medium  -> numbers between 1 and 100
  3) Hard    -> numbers between 1 and 500

Enter choice (1/2/3): 2

Great! I'm thinking of a number between 1 and 100 (Medium mode).
Let's begin!

Your guess (1-100): 50
Too HIGH.

Your guess (1-100): 25
Too HIGH.

Your guess (1-100): 12
Too HIGH, and getting warm.

Your guess (1-100): 6
Too LOW... but you're SO close!

Your guess (1-100): 9
Too HIGH... but you're SO close!

Your guess (1-100): 7
Too LOW... but you're SO close!

Your guess (1-100): 8

Correct! The number was 8.
You guessed it in 7 attempts.
Good job, you got there!
Games played: 1  |  Best score: 7

Play again? (y/n): n

Thanks for playing. Goodbye!
```

## 🚀 How to Run

1. Make sure Python 3.7+ is installed:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
3. Run the game:
   ```bash
   python guessing_game.py
   ```

No third-party packages are required — the game only uses Python's
standard library (`random`, `sys`).

## 🗂️ Project Structure

```
PRODIGY_PY_02_Guessing_Game/
├── guessing_game.py           # Main game source code
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
├── .gitignore
└── screenshots/
    ├── gameplay-medium.png
    ├── gameplay-validation.png
    └── gameplay-replay.png
```

## 🧠 How It Works

1. The player picks a difficulty, which sets the number range.
2. `random.randint(low, high)` generates the secret number.
3. Each guess is validated, then compared to the secret number.
4. Feedback is returned: too high, too low, or correct — with a bonus
   hint when the guess is close.
5. Once correct, the loop ends and the attempt count is reported.
6. The player can choose to play again; the session tracks games played
   and the best (lowest-attempt) score so far.

## 🛠️ Built With

- **Python 3** (standard library only — `random`, `sys`)

## 📌 About This Task

This project was completed as part of the **PRODIGY INFOTECH** internship
program — Task 02 of the Python Programming track.

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE)
for details.

⭐ If you found this project helpful, consider giving it a star!
