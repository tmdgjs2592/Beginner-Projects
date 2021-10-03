import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    count = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Guessed Too High")
        elif guess < random_number:
            print("Guessed Too low")
        count +=1
    print(f"You guessed correctly in {count} times. The Answer was {random_number}")

def computer_guess():
    Low = 1
    High = int(input("How big should the number be?: "))
    you = random.randint(Low,High)
    print(f"(Your number is {you}")
    guess = 0
    while guess != you:
        guess = random.randint(Low, High)
        answer = input(f"is {guess} the right number? Too high(H), Too low(L), Correct(C): ").lower()
        if answer == 'h':
            High = guess -1
        elif answer == 'l':
            Low = guess + 1
        elif answer == 'c': 
            print("The computer guessed correctly")
            break

computer_guess()

