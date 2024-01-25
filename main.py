from flask import Flask,render_template,request
import pickle
import requests
import numpy as np

app = Flask(__name__)
model = pickle.load(open('loan_approval.pkl','rb'))
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')

@app.route('/predict',method=['POST'])
def predict():
    if request.method == 'POST':
        pass