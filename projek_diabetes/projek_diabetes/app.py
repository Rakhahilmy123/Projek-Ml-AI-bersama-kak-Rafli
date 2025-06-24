from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import joblib
import os

app = Flask(__name__)
model = None
model_accuracy = None

def load_and_train_model():
    global model, model_accuracy
    
    try:
        data = pd.read_csv("projek_diabetes/diabetes.csv")
        
        X = data[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                 "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]]
        y = data["Outcome"]
        

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
        model = LogisticRegression(solver="liblinear")
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        model_accuracy = metrics.accuracy_score(y_test, y_pred)
        
        joblib.dump(model, 'diabetes_model.pkl')
        
        print(f"Model trained successfully with accuracy: {model_accuracy:.4f}")
        return True
        
    except FileNotFoundError:
        print("Error: diabetes.csv file not found!")
        return False
    except Exception as e:
        print(f"Error training model: {str(e)}")
        return False

def load_saved_model():
    global model
    
    if os.path.exists('diabetes_model.pkl'):
        try:
            model = joblib.load('diabetes_model.pkl')
            print("Saved model loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading saved model: {str(e)}")
            return False
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    global model
    
    if model is None:
        return jsonify({
            'error': 'Model not loaded. Please check if the model is trained properly.'
        }), 500
    
    try:
        data = request.get_json()
        required_fields = ['pregnancies', 'glucose', 'bloodPressure', 'skinThickness', 
                          'insulin', 'bmi', 'diabetesPedigreeFunction', 'age']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        input_data = pd.DataFrame({
            'Pregnancies': [float(data['pregnancies'])],
            'Glucose': [float(data['glucose'])],
            'BloodPressure': [float(data['bloodPressure'])],
            'SkinThickness': [float(data['skinThickness'])],
            'Insulin': [float(data['insulin'])],
            'BMI': [float(data['bmi'])],
            'DiabetesPedigreeFunction': [float(data['diabetesPedigreeFunction'])],
            'Age': [float(data['age'])]
        })
        
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]
        
        result = {
            'prediction': int(prediction),
            'prediction_text': 'Diabetes' if prediction == 1 else 'Tidak Diabetes',
            'probability': {
                'no_diabetes': float(prediction_proba[0]),
                'diabetes': float(prediction_proba[1])
            },
            'confidence': float(max(prediction_proba)),
            'model_accuracy': model_accuracy
        }
        
        return jsonify(result)
        
    except ValueError as e:
        return jsonify({'error': f'Invalid input data: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

@app.route('/api/model-info', methods=['GET'])
def model_info():
    global model, model_accuracy
    
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    return jsonify({
        'model_type': 'Logistic Regression',
        'accuracy': model_accuracy,
        'features': ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'],
        'status': 'ready'
    })

@app.route('/api/retrain', methods=['POST'])
def retrain_model():
    success = load_and_train_model()
    
    if success:
        return jsonify({
            'message': 'Model retrained successfully',
            'accuracy': model_accuracy
        })
    else:
        return jsonify({'error': 'Failed to retrain model'}), 500

if __name__ == '__main__':
    print("Starting Diabetes Prediction API...")
    
    if not load_saved_model():
        print("No saved model found, training new model...")
        if not load_and_train_model():
            print("Failed to train model. Make sure diabetes.csv is in the same directory.")
            exit(1)
    
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    print("Server starting on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)