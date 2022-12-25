import pickle
from flask import Flask, request
from sklearn.preprocessing import StandardScaler

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create an API endpoint
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input parameters
    volume = request.form['volume']
    dapp_transactions = request.form['dapp_transactions']
    matching_transactions = request.form['matching_transactions']
    age = request.form['age']
    reviews = request.form['reviews']
    
    # Preprocess the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform([[volume, dapp_transactions, matching_transactions, age, reviews]])

    # Make a prediction
    prediction = model.predict(scaled_data)[0]

    # Return the result
    return str(prediction)

if __name__ == '__main__':
    app.run()