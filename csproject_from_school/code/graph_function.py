from matplotlib import pyplot as plt
from math import *
import numpy

def damped_oscillations(m,b,k):
    try:
        x = numpy.linspace(0,100,1000)
        y = []
        for i in x:
            y.append(e**(-b*i/2*m)*cos(((k/m - (b**2/4*m**2))**(1/2))*i))
        plt.plot(x,y)
        plt.show()
    except:
        print('hello world!')
        x = numpy.linspace(0,100,1000)
        y = []
        for i in x:
            y.append(e**(-b*i/2*m)*cos(((k/m + (b**2/4*m**2))**0.5)*i))
        plt.plot(x,y)
        plt.show()

def sum_of_sin_wav():
    pass
