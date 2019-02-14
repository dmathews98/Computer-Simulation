import math
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SineCosineAnimation(object):

    def __init__(self):
        # set initial and final x coordinates of circle
        self.xpos = 0.0
        self.xmax = 2*math.pi

        # set up simulation parameters
        self.niter = 500
        self.xincr =  (self.xmax - self.xpos)/self.niter

    def init(self):
        # initialiser for animator
        return self.patches


    def animate(self, i):
        # update the position of the circles
        self.xpos += self.xincr*i
        self.patches[0].center = (self.xpos, math.sin(self.xpos))
        self.patches[1].center = (self.xpos, math.cos(self.xpos))
        return self.patches


    def run(self):
        # create plot elements
        fig = plt.figure()
        ax = plt.axes()

        # create list for circles
        self.patches = []

        # create circles of radius 0.1 centred at initial position and add to list
        self.patches.append(plt.Circle((self.xpos, math.sin(self.xpos)), 0.1, color = 'g', animated = True))
        self.patches.append(plt.Circle((self.xpos, math.cos(self.xpos)), 0.1, color = 'b', animated = True))
        # add circles to axes
        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])

        # set up the axes
        ax.axis('scaled')
        ax.set_xlim(self.xpos, self.xmax)
        ax.set_ylim(-1.1, 1.1)
        ax.set_xlabel('x (rads)')
        ax.set_ylabel('sin(x)')

        # create the animator
        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.niter, repeat = False, interval = 50, blit = True)

        # show the plot
        plt.show()



sc = SineCosineAnimation()
sc.run()
