from flask import Flask, request, render_template
import numpy as np
import pickle
from src.feature_module.build_features import *

app = Flask(__name__)

model = pickle.load(open('D:\\University\\INTRO_2_DS\\Final_Project\\models\\model.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods = ["POST"])
def predict():
    values =  request.form.values()
    features = []
    for i in values:
        if i[0] >= '0' and i[0] <= 9:
            features.append(np.array(float(i)))
        else:
            features.append(convert(i))
    features = np.array(features)
    pred = model.predict(features)
    
    return render_template('index.html', prediction_text = 'Giá: {}'.format(pred))

if __name__ == "__main__":
    app.run(debug = True)