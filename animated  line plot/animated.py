from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#create emty list for save a data
x , y = [], []

fig, ax = plt.subplots()

def animation(i):

	
    pt = randint(1,9)
    x.append(i)
    y.append(pt)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0,20])
    ax.set_ylim([0,10])


ani = FuncAnimation(fig, animation, frames=20, interval=500, repeat=False)

plt.show()


