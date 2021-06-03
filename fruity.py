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


if __name__ == "__main__":
    app.run(debug=True)
