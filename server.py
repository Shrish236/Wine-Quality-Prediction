from flask import Flask, jsonify, render_template, request
import json
from json import JSONEncoder
import joblib
import warnings
warnings.filterwarnings("ignore")
app = Flask (__name__)

model =  joblib.load("C:\\Users\\shris\\Downloads\\WineQuality\\model\\model.joblib")

@app.route('/', methods = ['GET', 'POST'])
def func1():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def func():
    if request.method == 'POST':
        values = []
        for key, value in request.form.items():
            print(key,  value)
            values.append(value)
        quality = model.predict([values])
        print(quality)
        return render_template('result.html', res=quality[0])
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
