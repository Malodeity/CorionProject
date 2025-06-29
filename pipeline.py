# ======================================================
# 📄 FILE: pipeline.py (CSV version)
# PURPOSE: Handle CSV "database" connection and data retrieval
# ======================================================

import os
import re
import pandas as pd
from dotenv import load_dotenv
from functools import lru_cache

# Load environment variables
load_dotenv()

# Read CSV paths from environment variables
COMPANY_INFO_CSV = os.getenv("COMPANY_INFO_CSV_PATH")
STOCK_MARKET_CSV = os.getenv("STOCK_CSV_PATH")


# Factory to load DataFrames instead of DB connection
class CSVClientFactory:
    """
    Factory Pattern: creates and returns DataFrames as "tables".
    """

    @staticmethod
    @lru_cache(maxsize=1)
    def get_client():
        return CSVClient()

class CSVClient:
    @lru_cache(maxsize=1)
    def get_company_df(self):
        try:
            company_df = pd.read_csv(COMPANY_INFO_CSV)
            company_df = company_df.drop(columns=['Unnamed: 0'])

            # Function to normalize market cap to billions
            def normalize_market_cap(value):
                value = str(value).replace(",", "").strip()
                if value.endswith("T"):
                    return float(value[:-1]) * 1000
                elif value.endswith("B"):
                    return float(value[:-1])
                elif value.endswith("M"):
                    return float(value[:-1]) / 1000
                else:
                    try:
                        return float(value)
                    except ValueError:
                        return None  # or handle error/log

            # Apply normalization
            company_df["Market Cap"] = company_df["Market Cap"].apply(normalize_market_cap)

            return company_df
        except Exception as e:
            raise IOError(f"Failed to load company CSV: {e}")

    @lru_cache(maxsize=1)
    def get_stock_df(self):
        try:
            stock_df = pd.read_csv(STOCK_MARKET_CSV)
            return stock_df
        except Exception as e:
            raise IOError(f"Failed to load stock CSV: {e}")



# Regex validation
def is_valid_symbol(symbol):
    """
    Unit 9: Regex validation for stock ticker symbol.
    1–5 uppercase letters.

    ^ and $: Match the start and end of the string (ensures full string match).
    [A-Z]: Matches one uppercase letter (A to Z).
    {1,5}: Matches between 1 to 5 characters.
    """
    pattern = r"^[A-Z]{1,5}$"
    return bool(re.match(pattern, symbol))


class CompanyRepository:
    def __init__(self, client: CSVClient):
        # TODO: Store connection and create a cursor
        self.client = client

    def get_company_by_symbol(self, symbol):
        # TODO: Validate symbol using regex
        if not is_valid_symbol(symbol):
            raise ValueError(f"Invalid symbol: {symbol}")

        # TODO: Query company_info table by symbol
        # TODO: Handle any errors using try/except
        company_df = self.client.get_company_df()
        try:
            result = company_df[company_df['Symbol'] == symbol].iloc[0]
            if result.empty:
                return None
            return result
        except Exception as e:
            raise RuntimeError(f"Failed to query company by symbol: {e}")

    def get_stock_data_by_company(self, company_name):
        # TODO: Query stock_market_data table by company name
        # TODO: Return result list or handle errors
        stock_df = self.client.get_stock_df()
        try:
            result = stock_df[stock_df['Company Name'] == company_name]
            return result
        except Exception as e:
            raise RuntimeError(f"Failed to query stock data by company: {e}")

        
def load_and_prepare_data(symbol):
    """
    Skeleton for loading and preparing stock and company data.
    
    :param stock_data_path: Path to the stock market data CSV.
    :param company_info_path: Path to the company info CSV.
    :return: Prepared and merged DataFrame.
    """
     #Either you choose a company you want to focus on or you choose top 3 companies
    # TODO: Load both stock_market_data.csv and company_info.csv as DataFrames

    if is_valid_symbol(symbol):
        print(f"{symbol} is a valid symbol")

    # Get CSV client and repositories
    client = CSVClientFactory.get_client()
    repo = CompanyRepository(client)

    # Get company record
    company_info = repo.get_company_by_symbol(symbol)
    company_name = company_info["Company Name"]

    # Get stock data for this company
    stock_df = repo.get_stock_data_by_company(company_name)

    # TODO: Sort stock data by Name and Date to prepare for rolling/shift operations
    stock_df = stock_df.sort_values(by=["Company Name", "Date"]).copy()
    stock_df["Date"] = pd.to_datetime(stock_df["Date"])

    # TODO: Calculate daily return using pct_change()
    stock_df["Daily Return"] = stock_df["Close"].pct_change()

    # TODO: Calculate 5-day rolling volatility (standard deviation of daily returns)
    stock_df["5D Volatility"] = stock_df["Daily Return"].rolling(window=5).std()

    # TODO: Calculate 5-day future return (shift -5 and calculate percent change)
    stock_df["5D Future Return"] = stock_df["Close"].shift(-5).pct_change(periods=5, fill_method=None)

    # TODO: Validate rows with missing values in engineered columns
    stock_df = stock_df.dropna(subset=["Daily Return", "5D Volatility", "5D Future Return"])

    # TODO: Merge Market_Cap from company_info using Name = Symbol
    stock_df["Market Cap"] = company_info["Market Cap"]

    # TODO: Return the cleaned, merged DataFrame
    return stock_df
