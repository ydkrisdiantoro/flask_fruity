from flask import Flask
from flask_restful import Resource, Api
from sklearn.neighbors import KNeighborsClassifier

import joblib
from difflib import SequenceMatcher
import json
import pandas as pd

app = Flask(__name__)
api = Api(app)


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
            'result': json.dumps(result,separators=(',', ':'))
        }
    else :
        return {
            'result':0
        }       

if __name__ == '__main__':
    knn = joblib.load('./model_fruit.joblib')
    df = pd.read_csv('./fruits.csv')
    df = df.replace('-',0)
    for i in df.columns:
      if i != 'name' and i!= 'energy (kcal/kJ)':
        df[i] = df[i].astype(float)

    app.run(debug=True)