# Author: Abrorjon Asralov
# Purpose: This is a program that solves quadratic formulas given by the user
#          input.
import sys
import cmath


class Quadratic:
    def __init__(self) -> None:
        self._a = None
        self._b = None
        self._c = None
        self._solutions = []

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
        DISCRIMINANT = (self.getB())**2-(4*self.getA()*self.getC())
        if DISCRIMINANT < 0:
            print('Oops, Discriminant is Negative, NO SOLUTIONS!')
            sys.exit()
        else:
            return DISCRIMINANT

    def solveForXs(self) -> tuple[int]:
        disc = self.solveForDiscriminant()
        if disc == 0:
            return (int((-self.getB())/2*self.getA()), None)
        else:
            s1 = -self.getB()-cmath.sqrt(disc)/2*self.getA()
            s2 = -self.getB()+cmath.sqrt(disc)/2*self.getA()
            return s1, s2

    def __str__(self) -> str:
        return f'Quadtratic{self.solveForDiscriminant()}'


def processInput(coefs: str) -> list[int]:
    resCoefs = coefs.split(',')
    resListOfCoefs = [int(num) for num in resCoefs]
    return resListOfCoefs


def main():
    userWants = True
    while userWants:
        quadratic = Quadratic()
        coefs = input('''Enter your coefficients 
of your quadratic formula
with commas. Example a,b,c\n''')
        coefList = processInput(coefs)
        coefA = coefList[0]
        coefB = coefList[1]
        coefC = coefList[2]
        quadratic.setCoefs(coefA, coefB, coefC)
        xs = quadratic.solveForXs()
        if xs[1] == None:
            print(f'Your Solution is: {xs[0]}')
        else:
            print(f'Your solutions are: x1 = {xs[0]}, x2 = {xs[1]}')
        print('If you want to exit, type \'exit\' command')
        print('If you want to continue solving, press enter')
        userDesire = input()
        if userDesire == 'exit':
            userWants = False
        else:
            continue


if __name__ == '__main__':
    main()
