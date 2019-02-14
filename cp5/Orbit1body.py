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
        self.M = 6.4185e23
        self.m = 1.06e16
        self.r = 9.3773e6
        self.RoM = np.array([0, 0])
        self.RoP = np.array([self.r, 0])
        self.VoM = np.array([0, 0])
        self.VoP = np.array([0, ((self.G*self.M/self.r)**(1.0/2.0))])
        self.dt = 500
        self.niter = 2000

    def finda(self):
        magr = np.linalg.norm(self.RoP) #Magnitude of R
        a = (-1)*((self.G*self.M)/((magr)**3))*self.RoP #acceleration calculation

        return a

    def findv(self, a):
        self.VoP = self.VoP + a*self.dt #Update velocity

    def findr(self):
        self.RoP = self.RoP + self.VoP*self.dt #position update

    def init(self):
        return self.patches

    def animate(self, i):
        accel = self.finda()
        self.findv(accel)
        self.findr()

        self.patches[0].center = (self.RoM[0], self.RoM[1])
        self.patches[1].center = (self.RoP[0], self.RoP[1])

        return self.patches

    def run(self):
        fig = plt.figure()
        ax = plt.axes()

        self.patches = []

        self.patches.append(plt.Circle((self.RoM[0], self.RoM[1]), 1e6, color = 'r', animated = True))
        self.patches.append(plt.Circle((self.RoP[0], self.RoP[1]), 2e5, color = 'b', animated = True))

        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])

        ax.axis('scaled')
        ax.set_xlim(-1.2e7, 1.2e7)
        ax.set_ylim(-1.2e7, 1.2e7)

        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.niter, repeat = False, interval = 50, blit = True)

        plt.show()
