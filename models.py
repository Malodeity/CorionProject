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
        # Validate symbol
        if isinstance(symbol, str):
            self.symbol = symbol
        else:
            self.symbol = "N/A"

        # Validate name
        if isinstance(name, str):
            self.name = name
        else:
            self.name = "N/A"

        # Validate industry
        if isinstance(industry, str):
            self.industry = industry
        else:
            self.industry = "N/A"

        # Validate market_cap
        if isinstance(market_cap, (int, float)):
            self.market_cap = market_cap
        else:
            self.market_cap = "N/A"

    def __str__(self):
        # TODO: Return a string like "Apple Inc. (AAPL) - Tech, $2T"
        return f"{self.name} ({self.symbol}) - {self.industry}, ${self.market_cap}T"

class StockRecord:
    def __init__(self, record):
        # TODO: Extract fields from record dictionary and assign
        try:
            self.date = record.get("Date", "Unknown")
            self.name = record.get("Name", "Unknown")
            self.open = round(float(record.get("Open", 0.0) or 0.0), 2)
            self.close = round(float(record.get("Close", 0.0) or 0.0), 2)
            self.high = round(float(record.get("High",0.0) or 0.0), 2)
            self.low = round(float(record.get("Low", 0.0) or 0.0), 2)
            self.volume = round(float(record.get("Volume", 0) or 0.0), 2)
        except KeyError as e:
            print(f"Missing key: {e}")

    def summary(self):
        # TODO: Format a string showing open, close, volume for the day
        return f"On {self.date} {self.name} opened at {self.open}, closed at {self.close}, volume was {self.volume}"