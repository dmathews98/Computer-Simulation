'''
Simulated Decay programme
'''

from Nuclei import Nuclei
from Decay import Decay

def main():

    lam = float(input("Enter lambda: "))
    length = input("Enter N: ")
    timestep = float(input("Enter timestep: "))

    l = Nuclei(length)
    d = Decay(lam, timestep)
    initialCount = l.nucleiCount(length)

    measured = d.decaying(l, length, timestep)
    count = l.nucleiCount(length)
    final = initialCount - count

    l.printNuclei(length)
    print("Initial count: " + str(initialCount))
    print("Final count: " + str(final))
    print("Measured half life: " + str(measured) + " mins")
    print("The actual half is 24.98 mins")

main()
