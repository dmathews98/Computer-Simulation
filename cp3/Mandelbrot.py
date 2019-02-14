'''
Class for Mandelbrot Set
'''

import cmath as cm #needed for complex numbers
import numpy as np #needed for meshgrid 2D arrays and vectorization
import matplotlib.pyplot as plt #needed to plot the graph

class Mandelbrot(object):
    '''
    Initialises the C values, and creates the arrays for plotting and calculation by vectorisation
    '''
    def __init__(self, cmin, cmax, pts):
        self.C = np.linspace(cmin, cmax, pts)
        self.Creal = np.linspace(cmin.real, cmax.real, pts)
        self.Cimag = np.linspace(cmin.imag, cmax.imag, pts)
        self.Zo = complex(0, 0) #Sets intial Z
    '''
    Calculates next Z until convergence achieved, or assumed wont diverge above 4 and gives the iterations required
    '''
    def findn(self, CRe, CIm):
        '''For ease of calculation they were made complex'''
        Z = complex(CRe, CIm)
        C = complex(CRe, CIm)
        n = 1
        while n < 256:
            if abs(Z) > 4: #Check for assuming no longer diverges after 255 iterations
                break
            Z = Z**2 + C
            n += 1
        return n
    '''
    Creates the 2D arrays for plotting and finds the number of interations to provide the colour density and plots graph
    '''
    def grid(self):
        CReal, CImag = np.meshgrid(self.Creal, self.Cimag)
        vCalc_z = np.vectorize(self.findn) #Vectorises the function to allow supply of np array and to act on all values in the array
        N = vCalc_z(CReal, CImag)
        plt.imshow(N, extent = (CReal.min(), CReal.max(), CImag.min(), CImag.max()))
        plt.xlabel('C.Real')
        plt.ylabel('C.Imaginary')
        plt.show()
