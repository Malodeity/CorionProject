import pandas as pd

from pipeline import CSVClientFactory, CompanyRepository, is_valid_symbol
from models import Company, StockRecord
from utils import StrategyContext, calculate_average_close, filter_high_volume, sort_by_close

#  Need to drop Unnamed column
symbol = "AAPL"

if is_valid_symbol(symbol):
    print(f"{symbol} is a valid symbol")

# Create the client
client = CSVClientFactory.get_client()

# Test the client, ensure both methods are instance methods (operates on an instance of that class)
company_data = client.get_company_df()
print(f"Company CSV file was read and has {len(company_data)} rows")

stock_data = client.get_stock_df()
print(f"Stock CSV file was read and has {len(stock_data)} rows")

# Create the repository of the data
# Repository hides the fact that data is coming from CSV files, if later we are able to connect to database only the repository changes
repository = CompanyRepository(client)
company_by_symbol = repository.get_company_by_symbol(symbol)

# Output the relevant company details as a string
company_details = Company(symbol=company_by_symbol["Symbol"],
                          name=company_by_symbol["Company Name"],
                          industry=company_by_symbol["Industry"],
                          market_cap=company_by_symbol["Market Cap"])
print(company_details)

# Get timeseries of stock data
stock_data_timeseries = repository.get_stock_data_by_company(company_name=company_by_symbol["Company Name"])
print(stock_data_timeseries.head(3))

# Convert row to dict
record_data = stock_data_timeseries.iloc[0].to_dict()

# Create StockRecord object
record = StockRecord(record_data)

# Call summary method
print(record.summary())

# Using StrategyContext to calculate average close
context = StrategyContext(strategy=calculate_average_close)
average = context.execute(stock_data_timeseries)

# Using StrategyContext to indicate where volume is over threshold
context = StrategyContext(strategy=filter_high_volume)
high_volume = context.execute(stock_data_timeseries,threshold=50000000)

# Using StrategyContext to sort close price
context = StrategyContext(strategy=sort_by_close)
close_sorted = context.execute(stock_data_timeseries, descending=False)

print(f"Average close price: {round(average,2)}")
print(high_volume.head(5))
print(close_sorted['Close'].head(5))

