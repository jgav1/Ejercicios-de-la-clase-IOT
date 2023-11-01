from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("test_html.html")
    
@app.route('/easterEgg')
def easterEgg():
    return 'Entraste al lado oscuro de la RPI 0.o'
    
if __name__ == '__main__':
    app.run(debug=True, port=88, host='0.0.0.0')    

