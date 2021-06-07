from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def main():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.php')

@app.route("/index")
def index():
    return render_template('index.php')

@app.route("/index2")
def index2():
    return render_template('index2.html')

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
        return render_template('hasil.html', nama_buah=nama_buah, jumlah=jumlah, halaman=halaman)
    return render_template('qbuah2.html')


@app.route("/qbuah3", methods=['GET', 'POST'])
def qbuah3():
    if request.method == 'POST':
        nama_buah = request.form['nama_buah']
        jumlah = 5
        halaman = 'suka'
        return render_template('hasil.html', nama_buah=nama_buah, jumlah=jumlah, halaman=halaman)
    return render_template('qbuah3.html')


if __name__ == "__main__":
    app.run(debug=True)
