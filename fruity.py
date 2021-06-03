from flask import Flask, render_template
import os

app = Flask(__name__)


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

@app.route("/qbuah2")
def qbuah2():
    return render_template('qbuah2.php')

@app.route("/qbuah3")
def qbuah3():
    return render_template('qbuah3.php')

@app.route("/qsayur1")
def qsayur1():
    return render_template('qsayur1.php')

@app.route("/qsayur2")
def qsayur2():
    return render_template('qsayur2.php')

@app.route("/qsayur3")
def qsayur3():
    return render_template('qsayur3.php')


if __name__ == "__main__":
    app.run(debug=True)
