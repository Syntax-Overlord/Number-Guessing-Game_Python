# Number Guessing Game

A simple command-line number guessing game written in Python.

## How It Works

1. The computer generates a random number between 1 and 100.
2. The player has a maximum of 7 attempts.
3. On each attempt, the player enters a guess.
4. The game compares the guess with the generated number:
   - `Too Low!` means the guess is smaller than the number.
   - `Too High!` means the guess is larger than the number.
   - A congratulations message is displayed when the guess is correct.
5. The game ends after 7 attempts or when the player guesses correctly.

## Input Rules

- Guesses must be whole numbers.
- Guesses must be between 1 and 100, inclusive.
- Invalid input displays `Invalid input!`.

## Requirements

- Python 3.8 or later

## Running the Game

From the project directory, run:

```bash
python main.py
```

## Project Structure

```text
Number-Guessing-Game_Python/
├── main.py
└── README.md
```
