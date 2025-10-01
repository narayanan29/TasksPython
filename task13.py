from random import randint
EASY_LEVEL_=10
HARD_LEVEL=5

#Guess the user against actual answer
def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("You guessed too high.")
        # Track the number of turns and reduce by 1 if they got wrong
        return turns - 1
    elif user_guess<actual_answer:
        print("You guessed too low.")
        return turns - 1
    else:
        print("Congradulations,you got it you win")

# Function to set difficulty
def set_difficulty():
    level=input("Choose a difficulty level(easy/hard): ").lower()
    if level == "easy":
        return EASY_LEVEL_
    elif level == "hard":
        return HARD_LEVEL
    else:
        return 0

def game():
    # choosing a random number between 1 to 100
    print("Welcome to number guessing game..!")
    print("Im thinking of a number between 1 to 100: ")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get wrong

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaing to guess the number")
        # Let the user guess the answer
        guess = int(input("Guess a number between 1 to 100: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of guesses ,You lose ")
            return
        elif guess != answer:
            print("Guess again")

game()






