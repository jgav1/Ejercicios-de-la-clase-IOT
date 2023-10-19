from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 27

# crea una lista vacia para "x" y "y"
x = []
y = []


# crea una figura y sus ejes
figura, ejes = plt.subplots()

# funcion the dibuja cada frame de la animacion
def animate(i):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    x.append(i)
    y.append(temperature)

    ejes.clear()
    ejes.plot(x, y)
    ejes.set_xlim([0,200])
    ejes.set_ylim([0,50])

# iniciar animacion
ani = FuncAnimation(figura, animate, frames=200, interval=50, repeat=False)

plt.show()