from flask import render_template as render, request, redirect, flash, url_for
from app.utils import file_exits
from config import Routes, Properties
from .services import generate_code_qr
from . import qr

@qr.route('/', methods=['GET', 'POST'])
def generateQR():
    """ vista de generación de códigos QR. """
    if request.method == 'POST':
        text = request.form.get("text_qr")
        if text == "":
            flash("El campo texto es obligatorio(*)", category='is-danger')
        else:
            generate_code_qr(text)
            flash("El código QR se genero de manera exitosa!!", category='is-success')
        
        return redirect(url_for('qr.generateQR'))
    else:
        if file_exits(Routes.base_code_qr + Properties.base_filename_code_qr) is False:
            generate_code_qr('https://asperos_geek')
        
        return render('qr.html')
