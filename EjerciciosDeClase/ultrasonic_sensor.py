from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo = 18, trigger = 17)

while True:
    print("Distance: ", round(ultrasonic.distance * 100, 3))
    sleep(1)