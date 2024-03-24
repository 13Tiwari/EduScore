from flask import Flask, request, Response, jsonify, make_response
from joblib import load
import os
import pickle
app = Flask(__name__)


# # Load the SVM model
module_dir = os.path.abspath(os.path.dirname(__file__))

# svm_model = load("/svm_modelFIRST.joblib")
# Path to your SVM model file


model_file_path = "svm_model.pkl"

# Load the SVM model from the file
with open(model_file_path, 'rb') as model_file:
    svm_model = pickle.load(model_file)

# Load the SVM model from the file
with open("scaler.pkl", 'rb') as model_file:
    scaler = pickle.load(model_file)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Input Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
        }
        .input-group {
            margin-bottom: 15px;
        }
        .input-group label {
            display: block;
            margin-bottom: 5px;
        }
        .input-group input[type="number"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            float: right;
        }
        .btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Financial Input Form</h2>
        <form id="financialForm" method="get" action="/predict">
            <div class="input-group">
                <label for="income">Income:</label>
                <input type="number" id="income" name="income" required>
            </div>
            <div class="input-group">
                <label for="savings">Savings:</label>
                <input type="number" id="savings" name="savings" required>
            </div>
            <div class="input-group">
                <label for="debt">Debt:</label>
                <input type="number" id="debt" name="debt" required>
            </div>
            <button type="submit" class="btn">Submit</button>
        </form>
    </div>
</body>
</html>

    """



@app.route('/predict', methods=['GET'])
def predict():
    # Get the query parameters from the URL
    income = float(request.args.get('income'))
    savings = float(request.args.get('savings'))
    debt = float(request.args.get('debt'))
    CAT_CREDIT_CARD = float(request.args.get('credit_card'))
    CAT_MORTGAGE = float(request.args.get('mortage'))
    CAT_SAVINGS_ACCOUNT = float(request.args.get('savings_account'))
    CAT_DEPENDENTS = float(request.args.get('dependents'))

    # Create a NumPy array containing the values
    values = [[income, savings, debt, CAT_CREDIT_CARD, CAT_MORTGAGE, CAT_SAVINGS_ACCOUNT, CAT_DEPENDENTS]]

    # Scale the values using the loaded scaler
    scaled_values = scaler.transform(values)

    # Scaled values will be a 2D array, so you can access the scaled values like this
    scaled_income, scaled_savings, scaled_debt, scaled_CAT_CREDIT_CARD, scaled_CAT_MORTGAGE, scaled_CAT_SAVINGS_ACCOUNT, scaled_CAT_DEPENDENTS = scaled_values[0]

    # Make prediction using the loaded SVM model
    prediction = svm_model.predict([[scaled_income, scaled_savings, scaled_debt, scaled_CAT_CREDIT_CARD, scaled_CAT_MORTGAGE, scaled_CAT_SAVINGS_ACCOUNT, scaled_CAT_DEPENDENTS]])
    #response.headers.add("Access-Control-Allow-Origin", "*")

    if prediction[0] < 350:
        prediction[0]=350
    if prediction[0] > 850:
        prediction[0] =850
    response = jsonify({"prediction": prediction[0]})   #{}
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    #return Response(response=f'{{"prediction": {prediction[0]}}}'

if __name__ == '__main__':
    app.run()
