from random import randint
temp = "" # a temp variable to store temporary files
guess_count = 3

def route():
    start()


def start():
    print("Welcome to the guess the number game!")
    temp = input("Do you want to start (y or n) ? : ")
    if temp.lower() == "y":
        print("You said yes!")
        game()
    elif temp.lower() == "n":
        print("You said no")
        quit()
    else:
        print("We did not understand")
        route()


def game():
    guess_count = 3
    random_int = randint(1, 10)
    while guess_count != 0:
        print(random_int)
        guess = input("Guess a number between 1 and 10: ")
        if int(guess) == random_int:
            correct()
        else:
            guess_count  = guess_count - 1
            print(f"You have {guess_count} more guesses left")
            if guess_count == 0:
                print("You have no guesses left:(")
                route()


def correct():
    print("You were correct!")
    start()


route()