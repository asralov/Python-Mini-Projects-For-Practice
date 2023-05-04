'''
Author: Abrorjon Asralov
Description: This is a program that gets coefficients of a quadratic
             expression and solves for x solutions. User should enter
             coefficients in one line with commas between coefficients.
             Then it will produce the answer. If there are no solutions,
             program exits the system and prints the message that there
             is no solution.
'''
import sys
import cmath


class Quadratic:
    '''
    This is an template for Quadratic class instances and it does all
    calulations in it. It produces the resulting solutions those are 
    entered by users.
    Attributes: self._a that is a coefficient a from ax^2 + bx + c form.
                self._b that is a coefficient b from ax^2 + bx + c form.
                self._c that is a coefficient c from ax^2 + bx + c form.
    Methods: __init__(self) => is a special method to initialize attributes
             above.
             setCoefs => is a setter method that gets three arguments those
             are a, b, and c coefficients, and sets to be self._a, self._b,
             and self._c.
             getA, getB, getC => are small getter methods that return the
             values of self._a, self._b, and self._c attributes.  
             __str__ is a special method that is used to reprsent the 
             information about this instance of Quadratic.
    '''
    def __init__(self) -> None:
        self._a = None
        self._b = None
        self._c = None

    def setCoefs(self, elementA: int, elementB: int, elementC: int) -> None:
        if self._a is None and self._b is None and self._c is None:
            self._a = elementA
            self._b = elementB
            self._c = elementC
        else:
            return None

    def getA(self) -> int:
        return self._a

    def getB(self) -> int:
        return self._b

    def getC(self) -> int:
        return self._c

    def solveForDiscriminant(self) -> int:
        '''
        This is a method that calculates the discriminant of the given
        coefficients, and if the discriminant is a non-negative number
        returns it, otherwise after importing sys, it exits a program,
        printing the message that discriminant is a negative value, that
        means that there is no solution.
        '''
        DISCRIMINANT = (self.getB())**2-(4*self.getA()*self.getC())
        if DISCRIMINANT < 0:
            print('Oops, The discriminant is negative; NO SOLUTIONS FOUND!')
            sys.exit()
        else:
            return DISCRIMINANT

    def solveForXs(self) -> tuple[int]:
        '''
        This is a method that solves for all possible x's after getting
        the discriminant. If the discriminant is 0, that shows that there
        are only 1 intersection (solution) so, it returns a tuple with
        (solution 1, None), otherwise if discriminant is greater than
        0 then it returns a tuple with two possible solutions. =>
        (solution 1, soultion 2).
        '''
        # getting the discrimiant using the mehtod of this class.
        disc = self.solveForDiscriminant()
        if disc == 0:
            # one solution since discriminant is 0 and using
            # simple math (formula -b/2a) we are getting that
            # one solution.
            return (int((-self.getB())/2*self.getA()), None)
        else:
            # otherwise, by importing cmath module,
            # we are solving for two x's. 
            s1 = -self.getB()-cmath.sqrt(disc)/2*self.getA()
            s2 = -self.getB()+cmath.sqrt(disc)/2*self.getA()
            return s1, s2

    def __str__(self) -> str:
        return f'Quadtratic{self.solveForDiscriminant()}'


def processInput(coefs: str) -> list[int]:
    '''
    This is a small function that gets a string of
    coefficients as a parameter (thos are separated
    with commas. After that, usint a list comprehension
    gets a list with those coefficients, but this time
    they are converted to be integers.
    '''
    resCoefs = coefs.split(',')
    resListOfCoefs = [int(num) for num in resCoefs]
    return resListOfCoefs


def main():
    userWants = True
    while userWants:
        # every time user wants to get answers for new
        # quadratics, therefore, in the while loop it 
        # creates new instances of this class as soon as
        # user gets desired answer. Otherwise program exits.
        quadratic = Quadratic()
        coefs = input('''Enter your coefficients 
of your quadratic formula
with commas. Example a,b,c\n''')
        # getting a list with all coefficients as integers.
        coefList = processInput(coefs)
        coefA = coefList[0]
        coefB = coefList[1]
        coefC = coefList[2]
        # setting all three gotten coefficinets to be 
        # attributes to our Quadratic instance.
        quadratic.setCoefs(coefA, coefB, coefC)
        # solving for possible solutions.
        # and it gets a tuple with two solutions
        # or one soltuion and None as a second.
        xs = quadratic.solveForXs()
        # if the second value of the tuple is None
        # it will print only one solution.
        if xs[1] == None:
            print(f'Your Solution is: {xs[0]}')
        else:
            # else prints two possinle solutions.
            print(f'Your solutions are: x1 = {xs[0]}, x2 = {xs[1]}')
        print('If you want to exit, type \'exit\' command')
        print('If you want to continue solving, press enter')
        # if user does not want to continue using this program 
        # after getting an exit command it extis the program.
        userDesire = input().lower()
        if userDesire == 'exit':
            userWants = False
        else:
            continue


if __name__ == '__main__':
    main()
