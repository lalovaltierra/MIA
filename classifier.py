import numpy as np
from skimage import exposure
from skimage.io import imread
from skimage.transform import resize 
from tensorflow import keras
from keras.models import load_model


def load_and_preprocess_image(img):
    image = imread(img)
    img_resized = resize(image, (224, 224), anti_aliasing=True)
    # Mejora de contraste
    img_preprocessed = exposure.equalize_adapthist(img_resized)
    # Expandir las dimensiones de img_preprocessed para hacer la predicción
    img_for_prediction = np.expand_dims(img_preprocessed, axis=0)
    modelo_transferido = load_model('model.h5')
    prediction = modelo_transferido.predict(img_for_prediction)
    predicted_class = 'Maligno' if prediction[0][0] >= 0.5 else 'Benigno'
    return predicted_class
