'''
Reads in the energy data and plots a graph of total energy against time
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    ke = [] #kinetic energy list
    pe = [] #potential energy list
    etot = [] #total energy list
    '''
    Mulitple times needed due to random element
    '''
    tke = [] #time list for ke
    tpe = [] #time list for pe
    tetot = [] #time list for etot

    '''KE data read'''
    f = open("KE.data", "r")
    for line in f.readlines():
        tokens = line.split(",")
        tke.append(float(tokens[0]))
        ke.append(float(tokens[1]))
    f.close()

    '''PE data read'''
    f = open("PE.data", "r")
    for line in f.readlines():
        tokens = line.split(",")
        tpe.append(float(tokens[0]))
        pe.append(float(tokens[1]))
    f.close()

    '''E Total data read'''
    f = open("EnergyTotal.data", "r")
    for line in f.readlines():
        tokens = line.split(",")
        tetot.append(float(tokens[0]))
        etot.append(float(tokens[1]))
    f.close()

    '''E Total vs Time plot'''
    plt.figure(1)
    plt.plot(tetot, etot)
    plt.xlabel('Time /Earth Years')
    plt.ylabel('Total Energy /J')
    plt.title('Total Energy v Time')

    '''KE(G), PE(R), E Total(R) vs Time plot'''
    plt.figure(2)
    plt.plot(tke, ke, 'g', tpe, pe, 'r', tetot, etot, 'b')
    plt.xlabel('Time /Earth Years')
    plt.ylabel('Total Energy /J')
    plt.title('Total(R), Kinetic(G) and Potential Energy(B) against Time')
    plt.show()

main()
