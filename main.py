# ======================================================
# 📄 FILE: main.py
# PURPOSE: Entry point and Service Layer for coordination
# EXPECTED:
# - Apply Service Layer to isolate orchestration logic (Unit 12)
# - Use GUI for user input (Unit 11)
# - Fetch, validate, process, and report on data
# RULES:
# - Only high-level logic in main function
# - Pass dependencies explicitly (DI)
# OUTCOME:
# - Learn to architect modular apps with pattern-based structure
# ======================================================
import pandas as pd

from pipeline import CSVClientFactory, CompanyRepository, is_valid_symbol
import tkinter as tk
from tkinter import simpledialog
from models import Company, StockRecord
from utils import StrategyContext, calculate_average_close, filter_high_volume, sort_by_close
from pipeline import load_and_prepare_data
from ml_model import ReturnPredictor


class StockAnalysisService:
    """
    Service Layer for orchestrating the stock report generation.
    Handles input, validation, transformation, and reporting.
    """

    def __init__(self, company_repo):
        self.repo = company_repo

    def run_report_for_symbol(self, symbol):

        # TODO: Generate PDF using injected strategy and singleton

        if not is_valid_symbol(symbol):
            print("Invalid stock symbol format.")
            return

        # TODO: Wrap company, fetch and map stock data
        company_by_symbol = self.repo.get_company_by_symbol(symbol)
        # if not company_by_symbol:
        #     print("Company not found.")
        #     return

        company_details = Company(symbol=company_by_symbol["Symbol"],
                                  name=company_by_symbol["Company Name"],
                                  industry=company_by_symbol["Industry"],
                                  market_cap=company_by_symbol["Market Cap"])
        print(company_details)

        # Get timeseries of stock data
        stock_data_timeseries = self.repo.get_stock_data_by_company(company_name=company_by_symbol["Company Name"])
        # print(stock_data_timeseries.head(3))

        # Convert row to dict
        record_data = stock_data_timeseries.iloc[0].to_dict()

        # Create StockRecord object
        record = StockRecord(record_data)
        # print(record.summary())

        # TODO: Filter/sort if needed, then calculate average
        # Using StrategyContext to calculate average close
        context = StrategyContext(strategy=calculate_average_close)
        average = context.execute(stock_data_timeseries)

        # Using StrategyContext to indicate where volume is over threshold
        context = StrategyContext(strategy=filter_high_volume)
        high_volume = context.execute(stock_data_timeseries, threshold=50000000)

        # Using StrategyContext to sort close price
        context = StrategyContext(strategy=sort_by_close)
        close_sorted = context.execute(stock_data_timeseries, descending=False)

        print(f"Average close price: {round(average, 2)}")
        print(high_volume.head(5))
        print(close_sorted['Close'].head(5))

        pass


if __name__ == "__main__":
    # GUI input
    root = tk.Tk()
    root.withdraw()
    symbol = simpledialog.askstring("Input", "Enter stock symbol (e.g. AAPL):")
    symbol = symbol.strip().upper()

    # DI: Setup repository and service manually
    client = CSVClientFactory.get_client()
    repository = CompanyRepository(client)
    service = StockAnalysisService(repository)

    if symbol:
        service.run_report_for_symbol(symbol)
        
    # Machine Learning Model Operations
    # TODO: Load and prepare the data by calling the pipeline function
    stock_df = load_and_prepare_data(symbol)

    # TODO: Instantiate and train the prediction model
    predictor = ReturnPredictor()
    predictor.train(stock_df)

    # TODO: Select last N rows to simulate “new” data for prediction
    prediction_input = stock_df[["Daily Return", "5D Volatility", "Market Cap"]].tail(5)

    # TODO: Run predictions on these rows
    predictions = predictor.predict(prediction_input)

    print()
    print("Sample Predictions:")
    for i, pred in enumerate(predictions, 1):
        print(f"Day {i}: Predicted 5D Future Return = {round(pred, 4)}")

    # TODO: Add predictions to DataFrame and save results to CSV
    predictions_df = pd.DataFrame(predictions)
    predictions_df.to_csv('Predictions Result.csv', index=False)

    pass
