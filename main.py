from flask import Flask, render_template, make_response, redirect, request
from flask_bootstrap import Bootstrap
from PIL import Image

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    response = make_response(redirect('/inicio'))
    return response

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/clasificar', methods=['POST'])
def clasificar():
    try:
        imagen = request.files['imagenInput']
        # Realizar el procesamiento de la imagen (contar pixeles, etc.)
        pixel_count = procesar_imagen(imagen)

        return render_template('index.html', pixel_count=pixel_count)
    except Exception as e:
        return render_template('index.html', error=str(e))
    
def procesar_imagen(imagen):
    # Implementa aquí el algoritmo para procesar la imagen
    # Por ejemplo, contar el número de píxeles
    img = Image.open(imagen)
    pixel_count = img.width * img.height
    return pixel_count


if __name__ == '__main__':
    app.run(debug=True)