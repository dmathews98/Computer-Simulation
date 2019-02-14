'''
Defines a polynomial, prints it, finds order, adds another to it, differentiates and finds antiderivative
'''

class Polynomial(object):

    '''
    Initialises the list supplied as coefficients of polynomial
    '''
    def __init__(self, coefficients):
        self.coeffs = coefficients
    '''
    Returns a string of the polynomial
    '''
    def __str__(self):
        polystr = str(self.coeffs[0])
        for i in range(1, len(self.coeffs)):
            if self.coeffs[i] == 0:
                continue
            polystr += " + " + str(self.coeffs[i]) + "x^" + str(i)
        return polystr
    '''
    Returns the order of polynomial
    '''
    def polyOrder(self):
        for i in range(len(self.coeffs), 0, -1):
            if self.coeffs[i-1] != 0 :
                return i-1
            else :
                continue
    '''
    Adds the origional polynomial and the new polynomial, returns polynomial
    '''
    def polyAdd(self, poly2):
        '''For differing orders, makes same - causes 0s found in d/dx and integration'''
        if len(poly2.coeffs) > len(self.coeffs):
            for i in range(len(self.coeffs), len(poly2.coeffs)):
                self.coeffs.append(0)
        elif len(self.coeffs) > len(poly2.coeffs):
            for i in range(len(poly2.coeffs), len(self.coeffs)):
                poly2.coeffs.append(0)
        '''New list for answer'''
        coeffsnew = [0]*len(poly2.coeffs)
        for i in range(0, len(poly2.coeffs)):
            coeffsnew[i] = self.coeffs[i] + poly2.coeffs[i]
        return Polynomial(coeffsnew)
    '''
    Differentiates origional polynomial and returns a polynomial
    '''
    def polyDiff(self):
        '''New list for answer'''
        coeffdiff = []
        for i in range(1, len(self.coeffs)):
            new = i*self.coeffs[i]
            coeffdiff.append(new)
        return Polynomial(coeffdiff)
    '''
    Finds antiderivative and returns polynomial
    '''
    def polyAntidiff(self):
        '''New list for answer, c added for integration constant'''
        coeffint = ['c']
        for i in range(0, len(self.coeffs)):
            new = self.coeffs[i]/(i+1)
            coeffint.append(new)
        return Polynomial(coeffint)
