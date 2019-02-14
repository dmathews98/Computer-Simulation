'''
Class for orbital motion of the inner solar system - animates orbit, finds new position and velocity, finds total energy and orbital time period
'''

import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random as r

class OrbitalMotion(object):

    def __init__(self, mass, vel, rad, radinit):
        self.niter = 20000 #num of iterations of animation
        self.G = 6.67e-11 #grav constant
        self.dt = 100000 #timestep in seconds
        self.time = 0 #initial time for use in orbital period
        self.m = mass #stores mass array passed
        self.ri = radinit #stores initial position array passed - avoids update of ri
        self.r = rad #stores initial postion vectors, but used to update postion during animation
        self.v = vel #stores initial velocity vectors, used to update
        self.aprev = [0]*8 #array for storing previous acceleration for Beeman 3 step integration
        self.stop = [0]*6 #array used to prevent reprinting of orbital time period
        self.satellitecheck = [0]*3 #used to ensure only one satellite added to each array; m, r, v, and time for probe 1 to reach mars printed once

        '''Finds acceleration'''
    def finda(self, rij, j):
        magr = np.linalg.norm(rij) #normalises position vector
        a = (-1)*((self.G)*(self.m[j])/((magr)**3))*(rij) #finds current accelration between masses

        return a

        '''Finds new position'''
    def findr(self, a, i):
        self.r[i] = self.r[i] + self.v[i]*self.dt +(1.0/6.0)*(4*a - self.aprev[i])*((self.dt)**2) #finds new position - updates position vector


        '''Finds new velocity'''
    def findv(self, a, anext, i):
        self.v[i] = self.v[i] + (1.0/6.0)*(2.0*anext + 5.0*a - self.aprev[i])*self.dt #velocity updated
        self.aprev[i] = a #replaces aprev with the current a, which will be aprev for the next calculation

        return self.v[i]

        '''Finds gravitational potential energy'''
    def gravE(self, r, i, j):
        magr = np.linalg.norm(r) #normalises position vector
        gpe = (-1.0)*((self.G*self.m[i]*self.m[j])/(magr)) #calculates the new grav potential

        return gpe

        '''Finds kinetic energy'''
    def KE(self, i):
        vel = np.linalg.norm(self.v[i]) #normalises velocity vector
        KE = (1.0/2.0)*self.m[i]*(vel**2) #calculates kinetic energy

        return KE

        '''Calculates the total energy and writes to file - Energy.data'''
    def Ewrite(self, grav, ke):
        gpet = 0 #stores grav potential energy total
        ket = 0 #stores kinetic energy total
        for i in range(0, len(grav)):
            gpet += grav[i] #calculates gpe total
            ket += ke[i] #calculates ke total

        '''Writes KE data'''
        fo = open("KE.data", "a")
        fo.write(str(self.time) + ',' + str(ket) + '\n')
        fo.close()
        
        '''Writes PE data'''
        fo = open("PE.data", "a")
        fo.write(str(self.time) + ',' + str(gpet) + '\n')
        fo.close()

        etot =  gpet + ket #calculates total energy
        '''Writes to Total Energy'''
        fo = open("EnergyTotal.data", "a")
        fo.write(str(self.time) + ',' + str(etot) + '\n') #prints time,energytotal
        fo.close()

        '''Contains iterations'''
    def step(self):
        accel = [0]*len(self.m) #stores current accelerations
        anext = [0]*len(self.m) #stores next step acclerations
        velocity = [0]*len(self.m) #stores velocity step
        gravstore = [0]*len(self.m) #stores gpe's
        kestore = [0]*len(self.m) #stores ke's
        self.time += self.dt/(365.25*24*60*60.0) #calculates time passed in earth years and stores in self.time
        '''
        Iterations for position and velocity
        '''
        for k in range(0, len(self.m)): #iterates through each body, k, for everyother body, j, where k!=j
            for j in range(0, len(self.m)):
                if k != j: #doesnt act on self
                    rij = self.r[k] - self.r[j] #position vector between masses
                    accel[k] += self.finda(rij, j) #sums accelerations from forces with other bodies
            self.findr(accel[k], k) #calculates new positon and updates for each body
            for j in range(0, len(self.m)):
                if k != j: #doesnt act on self
                    rij = self.r[k] - self.r[j] #position vector between masses
                    anext[k] += self.finda(rij, j) #calculates next step acceleration and sums from forces with each other body
            velocity[k] = self.findv(accel[k], anext[k], k) #calculates and updates new veolcity vector for each body
        '''
        Calculate KE list and PE list
        '''
        for k in range(0, len(self.m)):
            for j in range(0, len(self.m)):
                if k != j:
                    rij = self.r[k] - self.r[j] #position vector between masses
                    gravstore[k] += self.gravE(rij, k, j) #calculates total gpe for each body
            kestore[k] += self.KE(k) #calculates total ke for each body
        '''
        Energy write out
        '''
        if r.random() < 0.3: #prevents huge quantites of data by implementing random element
            self.Ewrite(gravstore, kestore) #finds total energy and writes to Energy.data
        '''
        Orbital Periods
        '''
        if self.time > 0.23: #ensures not printed at beginning of simulation
            for l in range(1, 6):
                rlinit = self.r[l]-self.ri[l] #finds vector between current inital position
                magrnow = np.linalg.norm(rlinit) #normalises the vector
                if magrnow < 4.8e9 and self.stop[l] < 1: #prints period when close enough to original position and hasnt previousy printed - number small enough to ensure not done at the beginning
                    print('Planet ' + str(l) + 's orbital time period is ' + str(self.time) + ' Earth years')
                    self.stop[l] += 1 #prevents reprinting
                    ''' Orbital Periods in Earth years:
                    Mercury - 0.240829467387
                    Venus - 0.611580094811
                    Earth - 0.998174766142
                    Mars - 1.87593479859
                    Jupiter - 11.8323319898
                    '''
        '''
        Satellite to Mars
        '''
        if self.time >= 2: #adding satellite from earth to mars after 2 years
            if self.satellitecheck[0] < 1: #checks not already added
                self.m.append(3527) #mass with fuel; wikipedia
                self.r = np.vstack((self.r, [self.ri[3][0] + 1, 0]))
                self.v = np.vstack((self.v, [2100, 33000]))
                self.satellitecheck[0] += 1 #stops readdition every animation step
            rmv = self.r[4] - self.r[6] #dist between probe 1 and mars
            probecheck = np.linalg.norm(rmv) #normalising
            if probecheck < 6e9 and self.satellitecheck[2] < 1: #check not already printed and close enough
                probetime = self.time - 2 #time since launch
                print('Probe took ' + str(probetime) + ' Earth years')
                '''
                Brief reference for some results:

                Took Viking 1 304 Days = 0.833 Earth Years

                4500, 32300 took 0.582579156843 Earth years - does not return
                2000, 33000 took 0.870940755951 Earth years - returns closely -> dots overlap
                2100, 33000 took 0.886784799858 Earth years - returns closely -> dots overlap
                2500, 32900 took 0.82340862423 Earth years - does not return -> roughly half way between mars and earth return distance
                2200, 32950 took 0.848759094481 Earth years - returns quite close but not completely -> slightly closer than 4500, 32300
                '''
                self.satellitecheck[2] += 1 #puts out of check range so doesnt readd
        '''
        Satellite to Jupiter
        '''
        if self.time >= 3: #adding satellite from earth to jupiter after 3 years
            if self.satellitecheck[1] < 1: #checks not already added
                self.m.append(3527) #mass with fuel; wikipedia
                self.r = np.vstack((self.r, [self.ri[3][0] + 1, 0]))
                self.v = np.vstack((self.v, [2500, 38525]))
                self.satellitecheck[1] += 1 #stops readdition every animation step
                '''
                Brief reference for some results:

                *Off grid implies not returned to orbit*

                Affecting Y component (More sensitive):

                1) 2500, 38450 = no slingshot and dragged into wide elliptical orbit;
                2500, 38475 = propelled further from sun and out of grid slightly diagonally down to left;
                2) 2500, 38485 = fired at increbidly high speed downwards off grid;
                3) 2500, 38490 = propelled off grid further from run diagonally upwards to left;
                4) 2500, 38495 = redirected upwards and back into orbit around sun in opposite direction to all other bodies;
                5) 2500, 38500 = slingshot off grid down in bottom right;
                6) 2500, 38505 = propelled very quickly to the right and out the opposite side of the grid;
                7) 2500, 38510 = drawn into orbit similar, but elliptical and smaller, to jupiters by a small slingshot;
                2500, 38515 = same occurs but more highly elliptical orbit;
                8) 2500, 38525 = same again but with slightly more elliptical orbit;
                2500, 38550 = slight slingshot back into ellipitical orbit;
                2500, 38600 = even less slingshot into much more ellipitical orbit;
                9) 2500, 38650 = slingshot but draws the satellite back into an elliptical orbit, v slow;

                Affecting X component:

                1) 2000, 38525 = slight slingshot with high exit path relative to entry around Sun;
                2200, 38525 = slight slingshot with high exit path relative to entry around Sun;
                2300, 38525 = slight slingshot but even shorter path still;
                2) 2400, 38525 = slight slingshot but directed back much more directly producing very short path back round sun at higher speed;
                2450, 38525 = moderate(no high speed or large angle change) slingshot back into quite elliptical orbit around Sun;
                3) 2550, 38525 = moderate(no high speed or large angle change) slingshot back into quite elliptical orbit around Sun;
                4) 3000, 38525 = propelled rapidly by slinghot back and through to exit opposite side of grid;
                5) 3500, 38525 = accelereated on outwards away from sun out of grid;
                '''

    def init(self):
        return self.patches

    def animate(self, i):
        self.step()

        self.patches[0].center = (self.r[0][0], self.r[0][1])
        self.patches[1].center = (self.r[1][0], self.r[1][1])
        self.patches[2].center = (self.r[2][0], self.r[2][1])
        self.patches[3].center = (self.r[3][0], self.r[3][1])
        self.patches[4].center = (self.r[4][0], self.r[4][1])
        self.patches[5].center = (self.r[5][0], self.r[5][1])
        if self.time >= 2: #satellite from earth to mars after 2 years
            self.patches[6].center = (self.r[6][0], self.r[6][1])
        if self.time >= 3: #satellite from earth to jupiter after 3 years
            self.patches[7].center = (self.r[7][0], self.r[7][1])

        return self.patches

    def run(self):
        fig = plt.figure()
        ax = plt.axes()
        ax.patch.set_facecolor('black')

        self.patches = []

        self.patches.append(plt.Circle((self.r[0][0], self.r[0][1]), 4e10, color = '#FF6103', animated = True))
        self.patches.append(plt.Circle((self.r[1][0], self.r[1][1]), 3e9, color = '#BFBFBF', animated = True))
        self.patches.append(plt.Circle((self.r[2][0], self.r[2][1]), 9e9, color = '#E3CF57', animated = True))
        self.patches.append(plt.Circle((self.r[3][0], self.r[3][1]), 9e9, color = 'b', animated = True))
        self.patches.append(plt.Circle((self.r[4][0], self.r[4][1]), 4e9, color = '#FF7F50', animated = True))
        self.patches.append(plt.Circle((self.r[5][0], self.r[5][1]), 2e10, color = 'r', animated = True))
        self.patches.append(plt.Circle((10e20, 10e20), 2e9, color = '#FAFAFA', animated = True))
        self.patches.append(plt.Circle((10e20, 10e20), 2e9, color = '#EEAD0E', animated = True))
        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])
        ax.axis('scaled')
        ax.set_xlim(-1e12, 1e12) #based on orbit radius and body diameter
        ax.set_ylim(-1e12, 1e12)

        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.niter, repeat = False, interval = 1, blit = True)

        plt.show()
