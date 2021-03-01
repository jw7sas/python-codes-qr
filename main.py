# -*- Coding: utf-8 -*-
from flask import Flask, render_template as render, send_from_directory, url_for, redirect
from app import create_app
from config import Routes, Properties
app = create_app()

@app.route("/")
def index():
    return redirect(url_for('products'))


@app.route("/asperos/geek/products")
def products():
    context = {
        'products': [{"code": 1},{"code": 2},{"code": 3},{"code": 4},{"code": 5},{"code": 6},{"code": 7},{"code": 8},{"code": 9},{"code": 10}]
    }

    return render('index.html', **context)

@app.route("/images/qr/code/<path:filename>")
def get_img_qr(filename):
    return send_from_directory(Routes.base_code_qr, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
