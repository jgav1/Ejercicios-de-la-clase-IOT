from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 27

figura = plt.figure()
ejes = plt.axes(xlim=(0, 30), ylim=(15, 45))
max_points = 30
line, = ejes.plot(np.arange(max_points),
                  np.ones(max_points, dtype=np.float) * np.nan, lw=1, c='blue', marker='d',ms=2
                 )

def init():
    return line

h, t = Adafruit_DHT.read_retry(sensor, pin)

def animate(i):
    h, t = Adafruit_DHT.read_retry(sensor, pin)
    y = t
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line,

anim = animation.FuncAnimation(figura, animate, init_func=init, frames=200, interval=20, blit=False)

plt.show()