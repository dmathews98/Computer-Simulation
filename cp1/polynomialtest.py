'''
Tests polynomial.py
'''

from polynomial import Polynomial

def main():
    coefficients = []
    '''Collects coefficients, appends to list for polynomial, stop with non floating point number'''
    while True:
        try:
            coeff = float(input("Enter next coefficient: "))
            if True:
                coefficients.append(coeff)
        except:
            break
    '''Creates polynomial and tests methods'''
    poly = Polynomial(coefficients)
    print("P1(x) = " + str(poly))
    '''
    Tests order
    '''
    print("The order of P1(x) is " + str(poly.polyOrder()))
    '''
    List and collection of second polynomial, test add methods
    '''
    testpolyAdd = []
    while True:
        try:
            coeff2 = float(input("Enter next coefficient: "))
            if True:
                testpolyAdd.append(coeff2)
        except:
            break
    poly2 = Polynomial(testpolyAdd)
    print("P2(x) = " + str(poly2))
    polyadd = poly.polyAdd(poly2)
    print("P1(x) + P2(x) = " + str(polyadd))
    '''
    Tests differentiation
    '''
    polydiff = poly.polyDiff()
    print("d/dxP1(x) = " + str(polydiff))
    '''
    Tests antiderivative
    '''
    polyint = polydiff.polyAntidiff()
    print("Antiderivative of d/dxP1(x) = " + str(polyint))

main()
