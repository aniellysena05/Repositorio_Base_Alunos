from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = ['Milla','Sena','Anny']
    return render_template('ex_3-2.html',lista = lista )


if __name__ == '__main__':
    app.run(debug=True)
