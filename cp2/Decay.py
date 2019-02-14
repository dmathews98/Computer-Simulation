'''
Class for decay
'''
from Nuclei import Nuclei
import random as r
import time as t

class Decay(object):

    def __init__(self, h, dt):
        self.p = h*dt

    def decaying(self, nuclei, N, dt):
        undecnuc = 0
        k = 0
        while undecnuc >= 0:
            time = t.time()
            for i in range(N):
                for j in range(N):
                    if nuclei.nuclei[i][j] == 1:
                        if r.random() < self.p:
                            nuclei.nuclei[i][j] = 0
                            undecnuc += 1
            step = k*dt
            k += 1
            if undecnuc >= (N*N)/2:
                break

        return step
