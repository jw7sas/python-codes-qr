# -*- Coding: utf-8 -*-
import qrcode
from config import Routes, Properties
from pyzbar.pyzbar import decode
from PIL import Image

def generate_code_qr(text):
    """ Generar código QR. """
    image = qrcode.make(text)
    file_image = open(Routes.base_code_qr + Properties.base_filename_code_qr, 'wb')
    image.save(file_image)
    file_image.close()

def read_code_qr():
    """ Método para leer codigos QR. """
    img = Image.open(Routes.base_code_qr + Properties.base_filename_code_qr)
    result = decode(img)
    text = None
    for i in result:
        text = i.data.decode("utf-8")

    return text