'''
Test for Traffic
'''

from Traffic import Traffic
import matplotlib.pyplot as plt

def main():

    #rho = 0.3 #car density; no. cars/N ; at N=20 can use every 0.05 rho
    N = 20
    k = 20
    '''
    run = Traffic(N, k, rho) #shows the grid of road
    trial = run.timestep()
    run.grid()
    '''
    graphspeed = [0]
    densities = [0]
    r = 0.1

    for r in range(1, 11): #for graph of av speeds at densities
        ro = r/10.0
        s = Traffic(N, k, ro)
        sres = s.timestep()
        graphspeed.append(sres)
        densities.append(ro)
        s.grid()

        #Unusual flaw when using while loop and incrementing by 0.1, at 0.3 it always added an extra count
        #Unsure why but to avoid the for loop with /10 was used which solved the error

    plt.plot(densities, graphspeed)
    plt.xlabel("Density")
    plt.ylabel("Steady State Average Speed")
    plt.show()

main()
