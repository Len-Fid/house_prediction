import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass # do something
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('welcome.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    	return render_template('form.html')
    elif request.method == 'GET':
	return render_template('result2.html', form=form)

@app.route('/predict',methods=['POST'])
def predict():
    bedrooms = request.form.get("Number of bedrooms", type=int)
    facades = request.form.get("Number of facades", type=int)
    liv_area = request.form.get("Living area", type=int)
    surface_area = request.form.get("Surface area land", type=int)
    fireplace = request.form.get("Open fireplace")
    if fireplace == "Yes":
        fireplace = 1
    else:
        fireplace = 0  
    terrace = request.form.get("Terrace")
    if terrace == "Yes":
        terrace = 1
    else:
        terrace = 0  
    garden = request.form.get("Garden")
    if garden == "Yes":
        garden = 1
    else:
        garden = 0   
    pool = request.form.get("Pool")
    if pool== "Yes":
        pool = 1
    else:
        pool = 0  
    condition = request.form.get("Condition")
    if condition == "Needs work":
        condition = 1
    else:
        condition = 0
    
    request_values = [bedrooms,facades,liv_area,surface_area,fireplace,terrace,garden,pool,condition]
    int_features = [int(x) for x in request_values]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0])
    entry = output
    return render_template('result.html', entry=entry)

if __name__ == "__main__":
    app.run(debug=True)