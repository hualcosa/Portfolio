##### Imports that are needed to serve the model and run the flask app
from flask import Flask, request
import numpy as np
import os
from xgboost import XGBClassifier
import json

# Initializing Flask app
app = Flask(__name__)

# Flask route for status checking
@app.route('/')
def hello():
    return 'Welcome to the Loan forecaster API'

# Flask Route to run the inference on given test data
@app.route('/eligibility', methods=['POST'])
def eligibility_check():
    try:
        # deserializing data
        data = eval(json.loads(request.data)['data'])
        # the input dataset should have 16 columns (SEE R&D Notebook)
        X_test = np.array(data).reshape(-1, 16)
        # instanciate trained model
        clf = XGBClassifier()
        clf.load_model("booster_vanilla.bst")
        y_pred = clf.predict(X_test)
        print(y_pred)
        return {
                    "code": "200",
                    "msg": "Predicted Successfully",
                    "prediction": "Loan approved" if y_pred.tolist()[0] else "Loan Denied"
                }
    except Exception as e:
         print(e)
         return {
                    "code": 500,
                    "msg": "Something went wrong"
                }



if __name__ == "__main__":
     app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080))) 
