from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
from src.feature_module.build_features import *

app = Flask(__name__)

model = pickle.load(open('./Final_Project/models/model.pkl', 'rb'))
data = pd.read_csv('./Final_Project/data/processed/preproces_data.csv')

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/result", methods = ["POST"])
def predict():
    values =  request.form.values()
    features = []
    for i in values:
        if i[0] >= '0' and i[0] <= '9':
            features.append(np.array(float(i)))
        else:
            features.append(convert(label_district(data), label_street(data), i))
            
    features = np.array(features)
    features = np.reshape(features, (1, 5))
    pred = model.predict(features)
    
    return render_template('result.html', prediction = 'Giá: {:.1f} (Triệu/tháng)'.format(float(pred)))

if __name__ == "__main__":
    app.run(debug = True)