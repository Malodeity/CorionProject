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
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class ReturnPredictor:
    def __init__(self):
        # TODO: Initialize a LinearRegression model
        self.model = LinearRegression()
        self.is_trained = False

        pass

    def train(self, stock_df):

        # TODO: Extract X (features) and y (target)
        X = stock_df[["Daily Return", "5D Volatility", "Market Cap"]]
        y = stock_df["5D Future Return"]

        # TODO: Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # TODO: Fit the model on training data
        self.model.fit(X_train, y_train)
        self.is_trained = True
    
        # TODO: Predict on the test set and compute Mean Squared Error
        # Mean Squared Error (MSE) used to evaluate the accuracy of a regression model.
        # It measures the average squared difference between actual values and predicted values.
        # MSE tells you how far off your predictions are, on average.
        # The lower the MSE, the better your model is performing.
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

        # TODO: Print or log the MSE
        return print(f"MSE on Test Set: {round(mse,4)}. RMSE on Test Set: {round(np.sqrt(mse))}")

    def predict(self, input_df):
        # TODO: Predict using the trained model on new input features
        if not self.is_trained:
            raise RuntimeError("Model has not been trained yet. Call `train()` before `predict()`.")

        required_features = ["Daily Return", "5D Volatility", "Market Cap"]

        return self.model.predict(input_df[required_features])

    
    