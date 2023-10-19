from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# crea una lista vacia para "x" y "y"
x = []
y = []

# crea una figura y sus ejes
figura, ejes = plt.subplots()

# funcion the dibuja cada frame de la animacion
def animate(i):
    pt = randint(1,9) # numero al azar del 1 al 9
    x.append(i)
    y.append(pt)

    ejes.clear()
    ejes.plot(x, y)
    ejes.set_xlim([0,20])
    ejes.set_ylim([0,10])

# iniciar animacion
ani = FuncAnimation(figura, animate, frames=20, interval=500, repeat=False)

plt.show()