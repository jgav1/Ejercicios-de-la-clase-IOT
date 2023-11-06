import subprocess
import random
import time

topic = "gauge1"
message = "0"

# Construye el comando mosquitto_pub
command = ["mosquitto_pub", "-t", topic, "-m", message]

# Ejecuta el comando
while True:
	message = str(random.randint(0,100))
	command = ["mosquitto_pub", "-t", topic, "-m", message]
	try:
		subprocess.run(command, check=True)
		print(f"Mensaje enviado: {message}")
	except subprocess.CalledProcessError as e:
		print(f"Error al enviar el mensaje: {e}")
	print(command)
	time.sleep(1)
	
