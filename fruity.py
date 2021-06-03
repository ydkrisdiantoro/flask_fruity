from flask import Flask, render_template, url_for, request
import pickle
import numpy as np
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# set file directory path
MODEL_PATH = os.path.join(APP_ROOT, "./models/model_fruit.pkl")
# set path to the model
model = pickle.load(open(MODEL_PATH, 'rb'))
# load the pickled model


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
