# ======================================================
# 📄 FILE: utils.py
# PURPOSE: Analysis logic and reusable tools
# EXPECTED:
# - Strategy pattern for calculations
# - Average close + filter/sort helpers
# RULES:
# - Use list comprehensions and error handling (Unit 10)
# - Validate with regex (Unit 9)
# OUTCOME:
# - Abstraction and helper tools that plug into the flow
# ======================================================

class StrategyContext:
    """
    Context class for Strategy Pattern.
    Accepts a strategy function and executes it with provided data.
    Strategy Pattern is a behavioral design pattern used to
    define a family of algorithms, encapsulate each one, and make them interchangeable.

    """
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, *args, **kwargs):
        return self.strategy(*args, **kwargs)

def calculate_average_close(records):
    """
    Calculate the average of closing prices from stock records.
    Returns 0 if list is empty or error occurs.
    """
    try:
        if 'Close' not in records.columns:
            return 0
        return records['Close'].dropna().mean()
    except Exception as e:
        print(f"Error calculating average: {e}")
        return 0

def filter_high_volume(records, threshold):
    """
    Return list of records with volume above given threshold.
    """
    try:
        if 'Volume' not in records.columns:
            return records.iloc[0:0]
        return records[records['Volume'] > threshold]
    except Exception as e:
        print(f"Error filtering records: {e}")
        return records.iloc[0:0]

def sort_by_close(records, descending=True):
    """
    Return stock records sorted by close price.
    """
    try:
        if 'Close' not in records.columns:
            return records.iloc[0:0]
        return records.sort_values(by='Close', ascending=descending)
    except Exception as e:
        print(f"Error sorting records: {e}")
        return records.iloc[0:0]  # Return empty DataFrame on error