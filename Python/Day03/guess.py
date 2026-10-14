# Number guessing game (guess.py): pick a secret number, keep asking until the user guesses it, and print how many attempts it took.
secret_number = 7
guess = 0 
attempts = 0
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    attempts += 1
print(f"Correct! It took you {attempts} attempts.")