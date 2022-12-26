# Abrorjon Asralov
# Description: This is the program that keeps passwords in encrypted style and views that in decrypted view if
#              user asks to view his/her passwords in file called passwords.txt
from cryptography.fernet import Fernet
'''
def wrtie_key():
    key = Fernet.generate_key()
    key_file = open('key.key', 'wb')
    key_file.write(key)
'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def add_password():
    user_name = input('Username: ')
    password = input('Password: ')
    file_name = open('passwords.txt', 'a')
    file_name.write(user_name + '--->' + fer.encrypt(password.encode()).decode() + '\n')
    file_name.close()

def view_password():
    file_name = open('passwords.txt', 'r')
    passw = file_name.readlines()
    for content in passw:
        password = content.strip('\n').split('--->')
        print('Username---> '+password[0]+' and Password---> '+ str(fer.decrypt(password[1].encode()).decode()))
    file_name.close()

def main():
    ask_user = input('Do you want to add/view your file of passwords (Yes or No)?\n')
    user_wants_modify = True
    while user_wants_modify:
        if ask_user.lower() == 'yes':
            mode = input('Choose what do you want to do '
                        'Add(add a new password) or View(view passwords those already exist)?\n')
            if mode.lower() == 'add':
                add_password()
            elif mode.lower() == 'view':
                view_password()
            else:
                print('Please enter a valid mode (Add/View)')
            ask_again = input('Would you like to continue (Yes or No)?\n')
            if ask_again.lower() == 'yes':
                user_wants_modify = True
            elif ask_again.lower() == 'no':
                print('Your password(s)/nickname(s) in passwords.txt!\nThank You!')
                user_wants_modify = False
        else:
            print('Ok maybe next time ;-)')
            user_wants_modify = False

main()
