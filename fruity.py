from flask import Flask, render_template, url_for, request
import pickle
import numpy as np
import os

from sklearn.neighbors import KNeighborsClassifier

import joblib
from difflib import SequenceMatcher
import json
import pandas as pd


app = Flask(__name__)

# ============== ML ===================

def _check(test, data):
    return SequenceMatcher(a=test.lower(), b=data.lower()).ratio()

def _check_query(search):
    label = df['name'].values
    temp = []
    index = 0
    for i in label:
        ratio = _check(search, i)
        if ratio > 0.65:
            temp.append((index,ratio))
        index+=1
    print(temp)
    if len(temp)>0:
        temp.sort(key=lambda x: x[1], reverse=True)
        return temp[0][0]
    else:
        return 999

def _get_dataframe():
    df = pd.read_csv('./models/fruits.csv')
    df = df.replace('-',0)
    for i in df.columns:
      if i != 'name' and i!= 'energy (kcal/kJ)':
        df[i] = df[i].astype(float)
    return df

@app.route('/fruit/<n>/<name>')
def get(name, n):
    query = _check_query(name)
    print(query)
    if query != 999:
        X = df.drop(columns=['name','energy (kcal/kJ)'])
        preds = knn.kneighbors(X, n_neighbors=int(n))[1]
        
        arr_idx = preds[query] 
        result = []
        for item in df.loc[arr_idx].values.tolist():
            result.append(dict(zip(df.columns, item)))
        return {
            'result': json.dumps(result, separators=(',', ':'))
        }
    else :
        return {
            'result':0
        }

# ============== ML ===================

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
    knn = joblib.load('./models/model_fruit.joblib')
    df = _get_dataframe()    
    app.run(debug=True)
