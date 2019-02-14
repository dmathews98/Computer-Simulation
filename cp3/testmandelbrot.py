'''
Test for Mandelbrot Set
'''

from Mandelbrot import Mandelbrot

def main():
    '''Sets values to given, points high enough for quality resolution but not too long run time'''
    cmin = complex(-2.025, -1.125)
    cmax = complex(0.6, 1.125)
    pts = 1000 #1000 ~ 40sec, 500 < 10sec, 10000 > 5 min
    run = Mandelbrot(cmin, cmax, pts)
    run.grid()

main()
