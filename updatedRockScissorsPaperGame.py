"""
Author: Abrorjon Asralov
Purpose: This is a small text-typed game called Rock Paper Scissors, and 
this time it is more interractive with user experience
"""
import random

def printWelcoming():
    greeting = "    Welcome To The Rock/Scissors/Paper Game    "
    author = "Abrorjon Asralov"
    date = "09/29/2023"
    print("+"+"-"*len(greeting)+ "+")
    print("|"+" "*len(greeting)+"|")
    print("|"+greeting+"|")
    print("|"+" "*len(greeting)+"|")
    print("+"+"-"*len(greeting)+ "+")
    print("|  "+"Author: "+author+" | " + "Date: "+ date+"  |")
    print("+"+"-"*len(greeting)+ "+")
    print()

def isValid(userChoice) -> bool:
    userChoice = userChoice.lower()
    return userChoice=="rock" or userChoice=="paper" or userChoice=="scissors"

def getUserChoice() -> str:
    try:
        userInput = input("Please Enter Your Choice (Rock/Scissors/Paper): ")
        if (isValid(userInput)):
            return userInput.lower()
        else: # if it is an invalid string, the user will be promted again
            print("Please Enter A Valid Input")
            print()
            return -1 # returning -1 to give a command to repromt the user
    except ValueError: # to handle wrong inputs such as integer inputs
        print("Please Enter A Valid Input")
        print()
        return -1

def getComputerChoice() -> str:
    randomChoicePercentage = random.randint(0,100) # gives numbers 0~99
    if (randomChoicePercentage in range(0, 34)):
        return "rock"
    elif (randomChoicePercentage in range(34,67)):
        return "scissors"
    else:
        return "paper"

def computeTheWinner(user, comp) -> tuple[tuple[bool, str], tuple[bool, str]]:
    if (user==comp):
        return ((False,user), (False, comp))
    elif ((user=="rock" and comp=="scissors")or(user=="scissors" and comp=="paper")or(user=="paper" and comp=="rock")):
        return ((True,user), (False, comp))
    else: # the case when computer wins
        return ((False,user), (True, comp))
    
def userWantsToStop() -> bool:
    try:
        userChoice = input('Please Enter "Yes" to continue, "No" otherwise: ')
        print()
        if (userChoice.lower()=="no"):
            return True
        elif (userChoice.lower()=="yes"):
            return False
        else: # the case when the user input is neither NO nor YES
            return -1
    except ValueError:
        print("Please Enter A Valid Command (Yes, No): ")
        print()
        return -1


if (__name__ == "__main__"):
    printWelcoming()
    userWantsToPlay = True
    while userWantsToPlay:
        user = getUserChoice()
        # to handle the perfect user input
        # the case when it is not -1
        # it will not even enter to the loop
        while (user==-1):
            user = getUserChoice()

        # get a computer choice
        comp = getComputerChoice()

        # decide who is the winnder
        isUser, isComp = computeTheWinner(user, comp)
        print()
        if (not isUser[0] and not isComp[0]):
            print("<---It is a tie!--->")
            print()
        elif (isUser[0] and not isComp[0]):
            print("<---Yay User Has Won!--->")
            print()
        else:
            print("<---Oopsie... Computer has won--->")
            print()
        print("---")
        print(f"User has chosen: {isUser[1]}")
        print(f"Computer has chosen: {isComp[1]}")
        print("---")
        print()

        userDesire = userWantsToStop()
        while (userDesire==-1):
            userDesire = userWantsToStop()
        if (userDesire):
            byeMessage = "    Thanks for playing this game!    "
            print("+"+"-"*len(byeMessage)+"+")
            print("|"+" "*len(byeMessage)+"|")
            print("|"+byeMessage+"|")
            print("|"+" "*len(byeMessage)+"|")
            print("+"+"-"*len(byeMessage)+"+")
            userWantsToPlay = False