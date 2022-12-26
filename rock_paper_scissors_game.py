# Abrorjon Asralov
import random


def get_user_answer():
    user_answer = input('Please enter your answer (rock, paper or scissors)\n')
    valid_user_answer = user_answer.lower()
    return valid_user_answer


def get_comp_answer():
    random_per = random.randint(0, 99)
    if random_per >= 0:
        if random_per <= 33:
            return 'rock'
    if random_per > 33:
        if random_per <= 66:
            return 'paper'
    if random_per > 66:
        if random_per <= 99:
            return 'scissors'


def compare_answers(user, comp):
    if user == 'rock':
        if comp == 'scissors':
            return 'User Won'
    if user == 'paper':
        if comp == 'rock':
            return 'User Won'
    if user == 'scissors':
        if comp == 'paper':
            return 'User Won'
    if user == comp:
        return 'It is a tie!'
    else:
        return 'Computer Won'


def main():
    user_wants_to_continue = True
    while user_wants_to_continue:
        user = get_user_answer()
        comp = get_comp_answer()
        print('Your answer:', user)
        print('Computer\'s answer:', comp)
        print(compare_answers(user, comp))
        ask_again = input('Would you like to continue? (yes or no)\n')
        valid_ask_again = ask_again.lower()
        if valid_ask_again == 'yes':
            user_wants_to_continue = True
        else:
            print('Thanks for playing this game :)')
            user_wants_to_continue = False


main()
