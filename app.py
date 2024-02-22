import pickle
from flask import Flask, request,app,jsonify,url_for,render_template
import numpy as np


app=Flask(__name__)

regmodel=pickle.load(open('xgbmodel.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    new_data=np.array(list(data.values())).reshape(1,-1)
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x)  for x in request.form.values()]
    final_input=np.array(data).reshape(1,-1)
    output=regmodel.predict(final_input)
    return render_template('home.html',prediction_text="House price is {}".format(output[0]))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)