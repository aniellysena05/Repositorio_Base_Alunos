from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return'Olá mundo!'

@app.route('/sobre')
def sobre():
    return 'oi anielly sena'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'oie {nome},tudo bem?'

if __name__ == '__main__':
    app.run(debug=True)

