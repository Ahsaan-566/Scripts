import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('twitter-out.csv','r').read()
    lines = data.split('\n')

    x_array = []
    y_array = []

    x = 0
    y = 0

    for l in lines:
        x += 1
        if l >= 0.0:
            y += 1

        elif l < 0.0:
            y -= 1

        x_array.append(x)
        y_array.append(y)
        print x_array,y_array


    ax1.clear()
    ax1.plot(x_array,y_array)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


