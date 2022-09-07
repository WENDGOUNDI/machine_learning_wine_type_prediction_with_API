from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle
import json

app = Flask(__name__)

@app.route("/api/", methods=['POST'])
def makecalc():
    
    # Grab the input from the user
    data = request.get_json()
        
    if data != "":

        model1 = "models/DecisionTreeClassifier().pickle"
        model2 = "models/MLPClassifier().pickle"
        model3 = "models/RandomForestClassifier().pickle"
        model = pickle.load(open(model1, 'rb'))

        prediction = np.array2string(model.predict(data))
        if prediction=="[0.]":
             return jsonify(response=["Process Successful","This wine belongs to class_0"]), 200
        elif prediction=="[1.]":
             return jsonify(response=["Process Successful","This wine belongs to class_1"]), 200
        else:
             return jsonify(response=["Process Successful","This wine belongs to class_2"]), 200
    elif len(data[0]) < 13:
        return jsonify(response=["Process Failed","Check your data length."]), 401
    else:
        return jsonify(response=["Process Failed","Check your input data format."]), 401

if __name__ == "__main__":
    app.run(debug=True)