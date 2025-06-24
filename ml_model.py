# ======================================================
# 📄 FILE: ml_model.py
# PURPOSE: Machine Learning Logic Layer for Prediction
# EXPECTED:
# - Create, train, and use a regression model
# - Use sklearn for training and evaluation
# - Provide clean interface for model usage
# RULES:
# - Do not hardcode data paths or pipeline logic
# - Only define logic for training and inference
# - Keep class interface decoupled from I/O
# OUTCOME:
# - Understand ML abstraction via class-based design
# ======================================================

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class ReturnPredictor:
    def __init__(self):
        # TODO: Initialize a LinearRegression model
        pass

    def train(self, df):
        # TODO: Extract X (features) and y (target)

        # TODO: Split data into training and testing sets

        # TODO: Fit the model on training data
        
    
        # TODO: Predict on the test set and compute Mean Squared Error
        

        # TODO: Print or log the MSE
        pass

    def predict(self, input_df):
        # TODO: Predict using the trained model on new input features
        pass
    
    