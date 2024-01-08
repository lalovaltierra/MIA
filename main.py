from flask import Flask, make_response, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from clasificador import contar_pixeles

app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.route('/')
def index():
    response = make_response(redirect('/inicio'))
    return response

@app.route('/inicio', methods=['GET','POST'])
def inicio():
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        cantidad_pixeles = contar_pixeles(imagen)
        return render_template('inicio.html', resultado=cantidad_pixeles)
    return render_template('inicio.html')


if __name__=='__main__':
    app.run()