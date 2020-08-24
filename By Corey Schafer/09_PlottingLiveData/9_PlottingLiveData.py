import random
import pandas as pd
from itertools import count
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

#For changing data

# x_vals = []
# y_vals = []
#
# index = count()
#
# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0,5))
#
#     plt.cla()
#     plt.plot(x_vals, y_vals)
#
# ani = FuncAnimation(plt.gcf(), animate, interval=1000)
xx = 0

def animate(i):
    df = pd.read_csv('live_data.csv')

    x = df['x_val']
    y1 = df['total_1']
    y2 = df['total_2']

    plt.cla()
    plt.plot(x, y1, label = 'Channel 1')
    plt.plot(x, y2, label = 'Channel 2')

    plt.legend(loc = 'upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()