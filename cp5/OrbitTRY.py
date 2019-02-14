'''
Class for Orbital Motion of Phobos around Mars
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class OrbitalMotion(object):

    def __init__(self):
        self.G = 6.67e-11
        self.m = [6.4185e23, 1.06e16]
        self.r = 9.3773e6
        self.R = np.array([[0, 0], [self.r, 0]])
        self.V = np.array([[0, 0], [0, ((self.G*self.m[0]/self.r)**(1.0/2.0))]])
        self.dt = 500
        self.niter = 2000

    def init(self):
        return self.patches

    def animate(self, c):
        a = []
        for i in range(0, len(self.m)):
            for j in range(0, len(self.m)):
                if i == j :
                    continue
                else:
                    self.rij = self.R[i] - self.R[j]
                    magrij = np.linalg.norm(self.rij) #Magnitude of R
                    a[i] = (-1)*((self.G*self.m[j])/((magrij)**3))*self.rij #acceleration calculation

            accel = a[i]
            self.V[i] = self.V[i] + accel[i]*self.dt #Update velocity
            self.R[i] = self.R[i] + self.V[i]*self.dt #position update

        self.patches[0].center = (self.R[0][0], self.R[0][1])
        self.patches[1].center = (self.R[1][0], self.R[1][1])

        return self.patches

    def run(self):
        fig = plt.figure()
        ax = plt.axes()

        self.patches = []

        self.patches.append(plt.Circle((self.R[0][0], self.R[0][1]), 1e6, color = 'r', animated = True))
        self.patches.append(plt.Circle((self.R[1][0], self.R[1][1]), 2e5, color = 'b', animated = True))

        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])

        ax.axis('scaled')
        ax.set_xlim(-1.2e7, 1.2e7)
        ax.set_ylim(-1.2e7, 1.2e7)

        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.niter, repeat = False, interval = 50, blit = True)

        plt.show()
