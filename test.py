from pipeline import load_and_prepare_data
from ml_model import ReturnPredictor

symbol = "AAPL"

# Step 1: Load and prepare the data for the given symbol
stock_df = load_and_prepare_data(symbol)

# Step 2: Initialize the ML model (in this case is LinearRegression model)
predictor = ReturnPredictor()

# Step 3: Train the model using the calculated features: "Daily Return", "5D Volatility"
predictor.train(stock_df)

# Step 4: Test a small sample of data
prediction_input = stock_df[["Daily Return", "5D Volatility", "Market Cap"]].tail(5)
predictions = predictor.predict(prediction_input)

# Step 5: Display results
print()
print("Sample Predictions:")
for i, pred in enumerate(predictions, 1):
    print(f"Day {i}: Predicted 5D Future Return = {round(pred, 4)}")
