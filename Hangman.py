import random
import string

words = ["him","beautiful","stock","rocket","amazon","drift","car","headset","love","computer","calendar","stand","monitor","cup","jar","doll","bed","desk","mouse","mousepad","keyboard"]

def hangman():
    word = random.choice(words).upper()
    word_letters = set(word)
    used_letters = set()
    alpha = set(string.ascii_uppercase)
    lives = 6

    while len(word_letters) >= 0:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: " + ' '.join(word_list))
        print("You have guessed these letters: " + ' '.join(used_letters))
        print("**You have " + str(lives) + " lives left**")
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alpha and user_letter not in  used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -=1 
        elif user_letter in used_letters:
            print("You have already guess this letter.")
        else:
            print("Not a Letter.")
        
        if lives == 0:
            print("You have Lost!")
            break
        if len(word_letters) == 0 :
            print("You have won! The Answer was " + ' '.join(word))
            break



hangman()
