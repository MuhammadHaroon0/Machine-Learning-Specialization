from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)

# Load the model

@app.route('/predict', methods=['POST'])
def predict():
   # Create a DataFrame from the incoming data
    data=request.json
    df = pd.DataFrame(data)
    
    # Reorder columns based on the training data column order
    df = df.reindex(columns=cols)
    
    # Scale the incoming data using the loaded scaler
    scaled_data = scaler.transform(df)
    
    # Make predictions using the loaded model
    prediction = list(model.predict(scaled_data))
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    model = load('C://Users//HP//final_model.pkl')
    cols = load('C:/Users/HP/col_names.pkl')
    scaler = load('C:/Users/HP/advertising_scaler.pkl')
    app.run(port=6000)
