import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 27

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print(f"Temp: {temperature} C\n")
    print(f"Hum: {humidity} %\n\n")