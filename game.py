import random


def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 10. Try to guess it!")

    while True:
        guess = input("Enter your guess: ")
        attempts += 1

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


# Run the game
guess_the_number()
