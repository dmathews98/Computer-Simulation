'''
Class for Bodies - Reads in data and creates 2D arrays of initial conditions
                 - Also runs the orbit simulation
'''

import numpy as np
from Orbit import OrbitalMotion

class Body(object):

    def __init__(self):
        self.G = 6.67e-11 #grav constant
        self.m = [] #masses of planets - ordered from sun outwards
        self.r = np.zeros((6,2)) #postion vectors of planets - sun at origin originally
        self.v = np.zeros((6,2)) #velocity vectors - initially based from circular orbit of sun

        '''
        Reads in mass and initial radius from Sun data fro files and adds to mass list and radius 2D vector list, also creates velocity 2D list
        '''
    def Gather(self):
        initialr = np.zeros((6,2)) #initail r vector array - prevents updating of initial array in Orbit during animation
        '''Sun - 0'''
        f = open("Sun.data", "r")
        for line in f.readlines():
            tokens = line.split(",")
            self.m.append(float(tokens[0]))
            self.r[0][0] = float(tokens[1])
            initialr[0][0] = float(tokens[1])
        f.close()

        '''Mercury - 1'''
        f = open("Mercury.data", "r")
        for line in f.readlines():
            tokens = line.split(",")
            self.m.append(float(tokens[0]))
            self.r[1][0] = float(tokens[1])
            initialr[1][0] = float(tokens[1])
        f.close()

        '''Venus - 2'''
        f = open("Venus.data", "r")
        for line in f.readlines():
            tokens = line.split(",")
            self.m.append(float(tokens[0]))
            self.r[2][0] = float(tokens[1])
            initialr[2][0] = float(tokens[1])
        f.close()

        '''Earth - 3'''
        f = open("Earth.data", "r")
        for line in f.readlines():
            tokens = line.split(",")
            self.m.append(float(tokens[0]))
            self.r[3][0] = float(tokens[1])
            initialr[3][0] = float(tokens[1])
        f.close()

        '''Mars - 4'''
        f = open("Mars.data", "r")
        for line in f.readlines():
            tokens = line.split(",")
            self.m.append(float(tokens[0]))
            self.r[4][0] = float(tokens[1])
            initialr[4][0] = float(tokens[1])
        f.close()

        '''Jupiter - 5'''
        f = open("Jupiter.data", 'r')
        for line in f.readlines():
            tokens = line.split(",")
            self.m.append(float(tokens[0]))
            self.r[5][0] = float(tokens[1])
            initialr[5][0] = float(tokens[1])
        f.close()

        for i in range(1, len(self.m)): #calculates the initial velocities and puts them in the array
            self.v[i][1] = (((self.G*self.m[0])/self.r[i][0]))**(1.0/2.0)

        s = OrbitalMotion(self.m, self.v, self.r, initialr)
        s.run()
