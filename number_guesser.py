__author__ = "Abrorjon Asralov"
from random import randint

def getUserInput() -> int:
    try:
        userInput = int(input("Please Enter Your Number: "))
        return userInput
    except ValueError:
        print("Please Enter a Valid Number: ")
        return -1

def getTheRandomNumber(userRange) -> int:
    return randint(0, userRange+1)

def getRange() -> int:
    try:
        userInputRange = int(input("Please Enter The Range You Would Like To Have Numbers: "))
        if not (isValidRange(userInputRange)):
            print("Please Enter A Valid Positive Integer Greater Than 0")
            return -1
        else:
            return userInputRange
    except ValueError:
        print("Please Enter A Valid Positive Integer Greater Than 0")
        return -1

def isValidRange(n:int) -> bool:
    return type(n)==int and n > 0

def startGame() -> None:
    welcomingText = "    Welcome To The Number Guessing Game    "
    name = "    Abrorjon Asralov    "
    date = "    9/30/2023    "
    print()
    print("+"+"="*(len(welcomingText)+2)+"+")
    print("||"+" "*(len(welcomingText))+"||")
    print("||"+welcomingText+"||")
    print("||"+" "*(len(welcomingText))+"||")
    print("+"+"="*(len(welcomingText)+2)+"+")
    print("||"+" "*(len(name))+"||"+" "*len(date)+"||")
    print("||"+name+"||"+date+"||")
    print("||"+" "*(len(name))+"||"+" "*len(date)+"||")
    print("+"+"="*(len(welcomingText)+2)+"+")
    print()

def isGuessed(user, rand) -> None:
    if (user == rand):
        print("Yay you have guessed the Number!!!")
    elif (user > rand):
        print("It is higher than expected, please choose a smaller value")
    elif (user < rand):
        print("It is smaller than expected, please take a guess with a higher value")

if __name__ == "__main__":
    startGame()
    userPreferredRange = getRange()
    userInput = None
    while (userPreferredRange==-1 or userInput==-1):
        if (userInput==-1):
            userInput = getUserInput()
        if (userPreferredRange==-1):
            userPreferredRange = getRange()
    randomNum = getTheRandomNumber(userPreferredRange)
    while (userInput!=randomNum):
        userInput = getUserInput()
        isGuessed(userInput, randomNum)
