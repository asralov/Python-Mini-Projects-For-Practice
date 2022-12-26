# Full_name: Abrorjon Asralov

import random


def valid_answer(ask_user):
    if ask_user == 'yes' or ask_user == 'Yes' or ask_user == 'YES':
        return True
    else:
        return False


def get_user_number():
    user_num = int(input("Choose a number between 0 and 20 (it must be an integer)\n"))
    return user_num


def get_comp_number():
    rand_num = random.randint(0, 20)
    return rand_num


def compare_numbers(user, computer):
    if user == computer:
        return True
    return False


def main():
    print('| - - - Welcome to "Number Guesser" game! - - - |')
    ask_user = input('Do you want to start playing this game? (Yes or No)\n')
    user_wants_to_continue = True
    while user_wants_to_continue:
        if valid_answer(ask_user):
            user = get_user_number()
            comp = get_comp_number()
            if compare_numbers(user, comp):
                print('Your number is', user)
                print('Computer\'s number is', comp)
                print('Congratulations, you guessed the number!')
            else:
                print('Your number is', user)
                print('Computer\'s number is', comp)
                print('Sorry, you did not guess the number!')
            ask_again = input('Would you like to play this game again? (Yes or No)\n')
            if ask_again == 'yes' or ask_again == 'Yes' or ask_again == 'YES':
                user_wants_to_continue = True
            else:
                print('Sorry for that! Maybe next time you would like to play this game :)')
                user_wants_to_continue = False

        else:
            print('Sorry for that! Maybe next time you would like to play this game :)')


main()

