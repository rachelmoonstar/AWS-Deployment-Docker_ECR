#Second task is to build a Flask app using the treemodel
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
    data_unseen = pd.DataFrame([final], columns = col) #This is the new data
    ###########Enter code here to isolate the 'age' and 'bmi' features from data_unseen and
    #make a prediction. Output=rounded prediction to 2 decimal places
    output=None
    return render_template('home.html',pred='Expected Bill will be {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    ## Same as above, enter code here make a prediction using columns 0(age) and 2(bmi) only. Output is rounded to 2 decimal places
    #####Enter Code here
    output=None
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
