from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)
model=pickle.load(open('treemodel.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    int_features=[x for x in request.form.values()]
    final=np.array(int_features)
    col = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    data_unseen = pd.DataFrame([final], columns = col)
    input_data=data_unseen[['age','bmi']].values
    print(int_features)
    print(final)
    prediction=model.predict(input_data)
    output=round(prediction[0],2)
    return render_template('home.html',pred='Expected Bill will be {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    cols=[0,2]
    input_data=data_unseen[data_unseen.columns[cols]]
    prediction = model.predict(input_data)
    output = round(prediction[0],2)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
