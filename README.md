# EjerciciosLEDs
Este repositorio sirve como base para los de todos los equipos
Proyectos: 

Retos en equipo: 
Programa click a un botón refleja un led encendido: 
LED GPIO17, Botón GPIO 2
Programa que con el tiempo escrito en la consola, refleje el led encendido ese tiempo
LED GPIO17
Programa que genere secuencia de 1, 2, 3, 4, 4, 3, 2, 1 LEDs
LED GPIO17, GPIO2, GPIO3, GPIO4
Programa control de leds para simbolizar un semaforo: LED rojo, verde y amarillo. Por consola se escribe si queremos el alto ( rojo), siga ( verde), precaución ( amarillo). LED GPIO 17, GPIO2, GPIO3, GPIO4
Programa de control de leds de manera que le mandes una secuencia de prendido y haga eso con los leds, por ejemplo 0100 prenderia solo el segundo led, 1111 prenderia los 3 leds 20 min. LED GPIO17, GPIO2, GPIO3, GPIO4
Programa para clave morse con un led. S.O.S  30 min: LED GPIO17


GPIOs




Ejemplo: 
from gpiozero import LED

led = LED(17)
led.on()
 https://gpiozero.readthedocs.io/en/stable/api_output.html 

LED connection: 
Siempre tenemos que conectar una resistencia en serie al led. 



Boton connection: 


from gpiozero import Button

button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")

https://gpiozero.readthedocs.io/en/stable/recipes.html 





