from words import words
import random
import string
from hangman_visual import hanged_man


def valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():

    alphabet = set(string.ascii_uppercase)
    word = valid_word(words)
    word_letters = set(word) #letter in word
    used_letter = set() #letters we've guessed
    lives = 7
  
    while len(word) > 0 and lives > 0:

        # ' '.join() makes it string [a, b , c] --> 'a b c'
        print(f"'You have {lives} lives, and have used these letters: {' '.join(used_letter)}")
        # W - R D
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ''.join(word_list))
        print(hanged_man[lives])
        # user input
        user_inpt_letter = input("Guess a letter: ").upper()
        if user_inpt_letter in alphabet - used_letter: 
            used_letter.add(user_inpt_letter)
            if user_inpt_letter in word_letters:
                word_letters.remove(user_inpt_letter)
            else:
                lives = lives - 1
                print(f"Your letter { user_inpt_letter }, is not in the word.")
        elif user_inpt_letter in used_letter:
            print("You've already guessed that. Try Again!")
        else:
            print("Invalid Character. Try again. ") 
    
    if lives == 0:
        print(f"You died, sorry! The word was {word}")
        print(hanged_man[lives])
    else:
        print(f"Yay, you have guessed the {word}")

hangman()










