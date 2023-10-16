from flask import Flask
import waitress
from flask import request
from flask import jsonify
import pickle


model_file = 'model2.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load( f_in )

with open(dv_file, 'rb') as f_in:
    dv = pickle.load( f_in )

client = {"job": "retired", "duration": 445, "poutcome": "success"}

'''
X = dv.transform(client)
round(model.predict_proba(X)[0,1],3)
'''

app = Flask('app')


@app.route('/app', methods = ['POST'])
def predict():
    customer = request.get_json()
    
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5
    
    result = {
        'probability': float(y_pred),
        'churn':bool(churn)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 9696)