import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    print ("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print ("Please enter a valid number.")
            continue
        attempts += 1
        if guess < number_to_guess:
            print ("Your guess is too low.")
        elif guess > number_to_guess:
            print ("Your guess is too high.")
        else:
            print ("You've guessed the number in {} attempts.".format(attempts))

if __name__ == "__main__":
    guess_the_number()

