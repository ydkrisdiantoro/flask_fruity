from flask import Flask, render_template, url_for, request
from flask_restful import Resource, Api
import pickle
import numpy as np
import os

from sklearn.neighbors import KNeighborsClassifier

import joblib
from difflib import SequenceMatcher
import json
import pandas as pd

import io
import string
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

from googletrans import Translator

app = Flask(__name__)

def transform_image(image_bytes):
    tf = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(io.BytesIO(image_bytes))
    return tf(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, prediction = torch.max(outputs, 1)
    return classes[prediction]
    
def get_indo_result(preds):
    result = translator.translate(preds, dest='id')
    return result.text


def _check(test, data):
    return SequenceMatcher(a=test.lower(), b=data.lower()).ratio()


def _check_query(search): 
    label = df['name'].values
    temp = []
    index = 0
    for i in label:
        ratio = _check(search, i)
        if ratio > 0.65:
            temp.append((index, ratio))
        index += 1
    print(temp)
    if len(temp) > 0:
        temp.sort(key=lambda x: x[1], reverse=True)
        return temp[0][0]
    else:
        return 999

def _get_dataframe():
    df = pd.read_csv('./models/fruits.csv')
    df = df.replace('-', 0)
    for i in df.columns:
        if i != 'name' and i != 'energy (kcal/kJ)':
            df[i] = df[i].astype(float)
    return df


# ============== ML ===================

classes = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi',
           'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato', 'turnip', 'watermelon']

knn = joblib.load('./models/model_fruit.joblib')
df = _get_dataframe()
translator = Translator()
model = models.resnet18()
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, len(classes))
if torch.cuda.is_available():
    model.load_state_dict(torch.load(
        './models/image_model.pth'))
    model = model.to(device)
else:
    model.load_state_dict(torch.load(
        './models/image_model.pth', map_location=torch.device('cpu')))

@app.route('/fruit/<n>/<name>')
def get_nutrition(name, n):
    query = _check_query(name)
    print(query)
    if query != 999:
        X = df.drop(columns=['name', 'energy (kcal/kJ)'])
        preds = knn.kneighbors(X, n_neighbors=int(n))[1]

        arr_idx = preds[query]
        result = []
        for item in df.loc[arr_idx].values.tolist():
            result.append(dict(zip(df.columns, item)))
        return {
            'result': json.dumps(result, separators=(',', ':'))
        }
    else:
        return {
            'result': 0
        }


@app.route("/", methods=['GET', 'POST'])
@app.route('/predict', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        nutritions_arr = [
        "name",
        "energy (kcal/kJ)",
        "water (g)",
        "protein (g)",
        "total fat (g)",
        "carbohydrates (g)",
        "fiber (g)",
        "sugars (g)",
        "calcium (mg)",
        "iron (mg)",
        "magnessium (mg)",
        "phosphorus (mg)",
        "potassium (mg)",
        "sodium (g)",
        "vitamin A (IU)",
        "vitamin C (mg)",
        "vitamin B1 (mg)",
        "vitamin B2 (mg)",
        "viatmin B3 (mg)",
        "vitamin B5 (mg)",
        "vitamin B6 (mg)",
        "vitamin E (mg)"
        ]

        nutritions_male = {
            "energy (kcal/kJ)": 2650,
            "water (g)": 2500,
            "protein (g)": 65,
            "total fat (g)": 65,
            "carbohydrates (g)": 430,
            "fiber (g)": 37,
            "sugars (g)": 30,
            "calcium (mg)": 1000,
            "iron (mg)": 18,
            "magnessium (mg)": 330,
            "phosphorus (mg)": 700,
            "potassium (mg)": 4700,
            "sodium (g)": 1500,
            "vitamin A (IU)": 3000,
            "vitamin C (mg)": 90,
            "vitamin B1 (mg)": 1.2,
            "vitamin B2 (mg)": 1.3,
            "viatmin B3 (mg)": 16,
            "vitamin B5 (mg)": 5,
            "vitamin B6 (mg)": 1.3,
            "vitamin E (mg)": 15
        }

        nutritions_female = {
            "energy (kcal/kJ)": 2250,
            "water (g)": 2350,
            "protein (g)": 60,
            "total fat (g)": 65,
            "carbohydrates (g)": 360,
            "fiber (g)": 32,
            "sugars (g)": 30,
            "calcium (mg)": 1000,
            "iron (mg)": 18,
            "magnessium (mg)": 330,
            "phosphorus (mg)": 700,
            "potassium (mg)": 4700,
            "sodium (g)": 1500,
            "vitamin A (IU)": 2300,
            "vitamin C (mg)": 75,
            "vitamin B1 (mg)": 1.1,
            "vitamin B2 (mg)": 1.1,
            "viatmin B3 (mg)": 14,
            "vitamin B5 (mg)": 5,
            "vitamin B6 (mg)": 1.3,
            "vitamin E (mg)": 15
        }

        if 'file' not in request.files:
            nama_buah = request.form['nama_buah']
            jumlah = 5
            # return get_nutrition(nama_buah, jumlah)
            nuts = get_nutrition(nama_buah, jumlah)
            nuts_2 = json.loads(nuts['result'])
                    
            return render_template('hasil.html', kebutuhan=nutritions_arr, nutrisi_male=nutritions_male, nutrisi_female=nutritions_female, nutrisi=nuts_2)

        file = request.files.get('file')
        if not file:
            return
        img_bytes = file.read()
        preds = get_prediction(img_bytes)
        preds = get_indo_result(preds)
        return get_nutrition(preds, 5)
    return render_template('index.html')

# ============== ML ===================

@app.route("/home")
def main():
    return render_template('index.html')

@app.route("/index")
def index():
    return render_template('index.php')

@app.route("/about")
def about():
    return render_template('about.php')

@app.route("/chart")
def chart():
    return render_template('chart.html')

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
    knn = joblib.load('./models/model_fruit.joblib')
    df = _get_dataframe() 
    app.run(debug=True)
