import random 
from words import words
import string


def get_random_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_random_word(words).upper() # hello
    word_len = len(word)
    word_letters = set(word)  # {'h','e','l','o'}
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # {}
    print('The given word is ' + ' - ' * word_len, '(', word_len, 'letters )')

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        user_letter = input('Guess a letter: ').upper()
        print('You have', lives, 'lives and you have used these letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word is: ', ' '.join(word_list) + '\n')

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word.\n')

        elif user_letter in used_letters:
            print('You have already used that character. Please Try Again!\n')
        else:
            print('Invalid character. Please Try Again!\n')

    # finishing the game, either user won or hangman died!
    if lives == 0:
        print('Sorry the hangman is dead! The word was:', word)
    else:
        print('You guessed the word', word, '!!!')


hangman()
