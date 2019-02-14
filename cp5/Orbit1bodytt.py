'''
Class for Orbital Motion of Phobos around Mars
'''

import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class OrbitalMotion(object):

    def __init__(self):
        self.G = 6.67e-11
        self.m = np.array([6.4185e23, 1.06e16])
        self.r = 9.3773e6
        self.ri = np.array(([0, 0], [self.r, 0]))
        self.vi = np.array(([0, 0], [0, ((self.G*self.m[0]/self.r)**(1.0/2.0))]))
        self.dt = 100
        self.niter = 2000

    def finda(self, r, j):
        magr = np.linalg.norm(r) #Magnitude of R
        a = (-1)*((self.G*self.m[j])/((magr)**3))*r #acceleration calculation

        return a

    def findv(self, a, i):
            self.vi[i] = self.vi[i] + a*self.dt #Update velocity

    def findr(self, i):
            self.ri[i] = self.ri[i] + self.vi[i]*self.dt #position update

    def init(self):
        return self.patches

    def animate(self, i):
        accel = [0]*2
        for k in range(0, 2):
            for j in range(0, 2):
                if k != j:
                    rij = self.ri[k] - self.ri[j]
                    accel[k] += self.finda(rij, j)
            self.findv(accel[k], k)
            self.findr(k)

        self.patches[0].center = (self.ri[0][0], self.ri[0][1])
        self.patches[1].center = (self.ri[1][0], self.ri[1][1])

        return self.patches

    def run(self):
        fig = plt.figure()
        ax = plt.axes()

        self.patches = []

        self.patches.append(plt.Circle((self.ri[0][0], self.ri[0][1]), 1e6, color = 'r', animated = True))
        self.patches.append(plt.Circle((self.ri[1][0], self.ri[1][1]), 2e5, color = 'b', animated = True))

        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])

        ax.axis('scaled')
        ax.set_xlim(-1.2e7, 1.2e7)
        ax.set_ylim(-1.2e7, 1.2e7)

        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.niter, repeat = False, interval = 50, blit = True)

        plt.show()
