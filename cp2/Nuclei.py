'''
Class for nuclei
'''

class Nuclei(object):

    def __init__(self, N):
        self.nuclei = []
        for i in range(N):
            self.nuclei += [[1]*N]

    def printNuclei(self, N):
        s = ''
        for i in range(N):
            s += "\n"
            for j in range(N):
                s += (str(self.nuclei[i][j]) + " ")
        print(s + "\n")

    def nucleiCount(self, N):
        countUndec = 0
        for i in range(N):
            for j in range(N):
                if self.nuclei[i][j] == 1:
                    countUndec += 1
        return countUndec
