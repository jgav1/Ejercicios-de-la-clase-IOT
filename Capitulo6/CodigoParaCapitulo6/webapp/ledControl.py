from flask import Flask, render_template, request
from gpiozero import LED
led = LED(17)
led.off()

app = Flask(__name__)

@app.route("/led_control")
def led_control():
    return render_template("LED_Control.html")

@app.route('/led_control_act', methods=["GET"])
def led_control_act():
    if request.method == "GET":
        status = ""
        ledStatus = request.args["led"] 
        if ledStatus == "1":
            led.on()
            status = "ON"
        else: 
            led.off()
            status = "OFF"
        return render_template("LED_Control.html", ret=status)
    
@app.route('/easterEgg')
def easterEgg():
    return 'Entraste al lado oscuro de la RPI 0.o'
    
if __name__ == '__main__':
    app.run(debug=True, port=88, host='0.0.0.0')    

