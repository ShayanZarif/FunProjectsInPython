import numpy
import matplotlib.pyplot as plt

x = numpy.arange(0,4*numpy.pi,0.01)
y = numpy.sin(x)
plt.plot(x,y)
y1 = numpy.cos(x)
plt.plot(x,y1)
plt.xlabel("X values from 0pi to 4pi")
plt.ylabel("sin(X) and cos(X)")
plt.legend(["Sin(X)","Cos(X)"])
plt.show()
