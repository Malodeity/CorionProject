# ======================================================
# 📄 FILE: models.py
# PURPOSE: Define Company and StockRecord using OOP
# EXPECTED:
# - Class definitions with init methods and str/summary functions
# - Handle missing attributes safely (Unit 8)
# RULES:
# - Use OOP concepts (Unit 6)
# OUTCOME:
# - Learn reusable data models with encapsulation
# ======================================================

class Company:
    def __init__(self, symbol, name, industry, market_cap):
        # TODO: Assign parameters to instance variables
        self.symbol = symbol
        self.name = name
        self.industry = industry
        self.market_cap = market_cap
        pass

    def __str__(self):
        # TODO: Return a string like "Apple Inc. (AAPL) - Tech, $2T"
        pass

class StockRecord:
    def __init__(self, record):
        try:
            # TODO: Extract fields from record dictionary and assign
            pass
        except KeyError as e:
            print(f"Missing key: {e}")

    def summary(self):
        # TODO: Format a string showing open, close, volume for the day
        pass