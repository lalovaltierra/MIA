from flask import Flask, render_template, make_response, redirect, request, url_for
from flask_bootstrap import Bootstrap
#from PIL import Image
from classifier import load_and_preprocess_image
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
#print('aqui',app.root_path, "   ", url_for('static', filename='uploads/277680132_968447457191019_3473232396717729394_n.png', _external=True))

@app.route('/')
def index():
    response = make_response(redirect('/inicio'))
    return response

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/clasificar', methods=['POST'])
def clasificar():
    
    # Borrar imágenes previas en la carpeta 'static/uploads/'
    clear_upload_folder()

    # Obtener la imagen del formulario
    uploaded_file = request.files['image']

    # Guardar la imagen en el servidor
    image_path = 'static/uploads/' + uploaded_file.filename
    uploaded_file.save(image_path)

    # Contar los píxeles y devolver el resultado
    clasificacion = load_and_preprocess_image(image_path)

    return {'result': clasificacion, 'image_path': image_path}
    
def clear_upload_folder():
    # Obtener la ruta de la carpeta 'static/uploads/'
    folder_path = 'static/uploads/'

    # Borrar archivos en la carpeta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Error al borrar {file_path}: {e}')

if __name__ == '__main__':
    app.run(debug=True)