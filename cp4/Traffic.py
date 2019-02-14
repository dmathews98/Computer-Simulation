'''
Class for traffic
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random as r

class Traffic(object):

    def __init__(self, N, k, rho):
        self.length = N+2 #N is length of road, need halo slots
        self.niter = k+1 #j is number of iterations
        self.cars = rho*N
        self.road = np.zeros((k+1, N+2))
        c = 0
        '''
        Option for 1 as reduces run time due to random aspect; no need as whole road full
        '''
        if rho == 1:
            for j in range(1, N+1): #iterate through road length
                if self.road[0][j] == 0: #ensures not counting already filled slot
                    self.road[0][j] = 1 #sets to full
        else:
            while c < self.cars: #maintian density
                for j in range(1, N+1): #iterate through road length
                    if self.road[0][j] == 0: #ensures not counting already filled slot
                        if r.random() < 0.5: #random factor either full or empty so 1 in 2
                            self.road[0][j] = 1 #sets to full
                            c += 1 #increases car count
                            if c >= self.cars: #ends when reaches count, stops the 1 over error
                                break

    def timestep(self):
        for i in range(0, self.niter-1):
            speedcount = 0 #speed count to use to find av speed
            for j in range(1, self.length-1):
                self.road[i][0] = self.road[i][self.length-2]
                self.road[i][self.length-1] = self.road[i][1]
                if self.road[i][j] == 1: #car in slot so check front
                    if self.road[i][j+1] == 1: #car in front
                        self.road[i+1][j] = 1 #therefore car in same slot next step
                    else:
                        self.road[i+1][j] = 0 #no car in front so car moves
                        speedcount += 1
                elif self.road[i][j] == 0: #no car in slot so check behind
                    if self.road[i][j-1] == 1: #car behind
                        self.road[i+1][j] = 1 #so car moves forward
                    else:
                        self.road[i+1][j] = 0 #no care behind so no car moving in
            avspeed = speedcount/self.cars
            print(str(i) + "  " + str(avspeed))

        return avspeed


    def grid(self):
        display = self.road[:,1:-1] #displays only road not halo regions
        ax = plt.axes()
        r = 0.3 #radius of dot representing car
        for t in range(len(display)):
            for c in range(len(display[t])):
                if (display[t,c] == 1): #flipped so that we get the layout intended, trafiic left to right and timesteps upwards increasing
                    ax.add_patch(patches.Circle((c,t), r, color = 'green'))
        plt.axis('scaled') #cricles appear circular
        plt.show()
