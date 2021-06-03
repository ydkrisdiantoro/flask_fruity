from flask import Flask, render_template, url_for, request
import pickle
import numpy as np
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(APP_ROOT, "./models/model_fruit.pkl")
model = pickle.load(open(MODEL_PATH, 'rb'))


@app.route("/")
@app.route("/home")
def main():
    return render_template('index.php')


@app.route("/about")
def about():
    return render_template('about.php')


@app.route("/credit")
def credit():
    return render_template('credit.php')


@app.route("/qbuah1")
def qbuah1():
    return render_template('qbuah1.php')


@app.route("/qbuah2", methods=['GET', 'POST'])
def qbuah2():
    if request.method == 'POST':
        nama_buah = request.form['nama_buah']
        jumlah = 5
        halaman = 'makan'
        recommend = model.predict(nama_buah)
        return render_template('hasil.html', nama_buah=nama_buah, jumlah=jumlah, halaman=halaman, recommend=recommend)
    return render_template('qbuah2.html')


@app.route("/qbuah3", methods=['GET', 'POST'])
def qbuah3():
    if request.method == 'POST':
        nama_buah = request.form['nama_buah']
        jumlah = 5
        halaman = 'suka'
        return render_template('hasil.html', nama_buah=nama_buah, jumlah=jumlah, halaman=halaman)
    return render_template('qbuah3.html')


# @app.route("/qsayur1")
# def qsayur1():
#     return render_template('qsayur1.php')


# @app.route("/qsayur2")
# def qsayur2():
#     return render_template('qsayur2.php')


# @app.route("/qsayur3")
# def qsayur3():
#     return render_template('qsayur3.php')

if __name__ == "__main__":
    app.run(debug=True)
