# EjerciciosLEDs
Este repositorio sirve como base para los de todos los equipos
Proyectos: 

Retos en equipo: 
1) Programa click a un botón refleja un led encendido:
Requistos: LED GPIO17, Botón GPIO 2
3) Programa que con el tiempo escrito en la consola, refleje el led encendido ese tiempo
Requistos: LED GPIO17
4) Programa que genere secuencia de 1, 2, 3, 4, 4, 3, 2, 1 LEDs
Requistos: LED GPIO17, GPIO2, GPIO3, GPIO4
5) Programa control de leds para simbolizar un semaforo: LED rojo, verde y amarillo. Por consola se escribe si queremos el alto ( rojo), siga ( verde), precaución ( amarillo).
Requistos: LED GPIO 17, GPIO2, GPIO3, GPIO4
6) Programa de control de leds de manera que le mandes una secuencia de prendido y haga eso con los leds, por ejemplo 0100 prenderia solo el segundo led, 1111 prenderia los 3 leds 20 min. LED GPIO17, GPIO2, GPIO3, GPIO4
Programa para clave morse con un led. S.O.S  30 min:
Requistos: LED GPIO17



GPIOs:

![pinout](https://github.com/jgav1/EjerciciosLEDs/assets/36417687/db6c6350-d49a-47ca-8274-f02341fe73f7)



Ejemplo: 
from gpiozero import LED

led = LED(17)
led.on()
 https://gpiozero.readthedocs.io/en/stable/api_output.html 

LED connection: 

Siempre tenemos que conectar una resistencia en serie al led. 


![led conectado](https://github.com/jgav1/EjerciciosLEDs/assets/36417687/08e770cf-7fbe-4c03-8c30-d71fbf9b26cf)





Boton connection: 

![boton](https://github.com/jgav1/EjerciciosLEDs/assets/36417687/0b1698c3-45aa-484e-a45c-bdea63a12bd1)

from gpiozero import Button

button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")

https://gpiozero.readthedocs.io/en/stable/recipes.html 

![boton + led](https://github.com/jgav1/EjerciciosLEDs/assets/36417687/c4e4e7a7-8c2b-4074-87cf-543509158e05)





