"""Animating Plots
Quinn Smiley, 2026-04-28, CS 211"""

# # Line Plot
# import matplotlib.pyplot as plt
# from numpy import pi, arange
# from math import sin
# x = [i for i in arange(0, 2 * pi, 2*pi/100)]
# y = [sin(i) for i in x]
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()


# # Scaatter Plot
# import matplotlib.pyplot as plt
# from random import random
# from math import sin
# n_points = 100
# x = [random() for i in range(n_points)]
# y = [random() for i in range(n_points)]
# fig, ax = plt.subplots()
# ax.scatter(x, y)
# plt.show()


# # Histogram
# import matplotlib.pyplot as plt
# import numpy as np
# gaussian_numbers = np.random.normal(size=1000)
# num_bins = 5
# plt.hist(gaussian_numbers)
# plt.title("Gaussian Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


# Animation Plot
import numpy as np
from math import sin, cos
from numpy import pi, arange
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def animate_plot(t, v1, v2):
    x = []
    y = []
    z = []
    # function that draws each frame of the animation
    def animate(i):
        x.append(i)
        y.append(v1[i])
        z.append(v2[i])

        ax.clear()

        ax.plot(x, y, z)
        ax.set_xlim([0, n])
        ax.set_ylim([-1, 1])
    # create the figure and axes objects
    fig, ax = plt.subplots()
    # run the animation
    ani = FuncAnimation(fig, animate, frames=n, interval=30, repeat=False)
    plt.show()


n = 100
x = [i for i in arange(0, 2 * pi, 2*pi/100)]
y1 = [sin(i) for i in x]
y2 = [cos(i) for i in x]
animate_plot(x, y1, y2)
