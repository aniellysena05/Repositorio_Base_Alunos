from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return'Olá mundo!'

@app.route('/sobre')
def sobre():
    return 'oi anielly sena'


if __name__ == '__main__':
    app.run(debug=True)