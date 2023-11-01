from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask'


@app.route('/easterEgg')
def easterEgg():
    return 'Entraste al lado oscuro de la RPI 0.o'


if __name__ == '__main__':
    app.run(debug=True, port=88, host='0.0.0.0')
