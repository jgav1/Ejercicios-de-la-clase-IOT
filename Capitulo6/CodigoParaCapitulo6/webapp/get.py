from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/method_get", methods=["GET"])
def method_get():
    return render_template("method_get.html")

@app.route('/method_get_act', methods=["GET"])
def method_get_act():
    if request.method == "GET":
        id = request.args["id"]
        password = request.args.get("password")
        return render_template("method_get.html", id=id, password=password)
    
@app.route('/easterEgg')
def easterEgg():
    return 'Entraste al lado oscuro de la RPI 0.o'
    
if __name__ == '__main__':
    app.run(debug=True, port=88, host='0.0.0.0')    

