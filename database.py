# ======================================================
# 📄 FILE: database.py
# PURPOSE: Handle PostgreSQL connection and data retrieval
# EXPECTED:
# - Load DATABASE_URL from .env
# - Use Factory Pattern to connect to PostgreSQL using psycopg2 (Unit 12)
# - Implement Repository Pattern for company and stock data queries (Unit 12)
# - Validate input using regex (Unit 9)
# - Handle errors gracefully (Unit 8)
# RULES:
# - Do not hardcode connection details
# - Keep raw SQL inside repository methods
# - Make the code modular and testable
# OUTCOME:
# - Understand database abstraction and clean architecture
# ======================================================

import os
import re
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

class PostgresClientFactory:
    """
    Factory Pattern: creates and returns a PostgreSQL connection.
    """
    @staticmethod
    def get_connection():
        # TODO: Raise exception if DATABASE_URL is missing
        # TODO: Return a psycopg2 connection using DATABASE_URL
        pass

def is_valid_symbol(symbol):
    """
    Unit 9: Regex validation for stock ticker symbol.
    """
    # TODO: Check that symbol is 1–5 uppercase letters using regex
    pass

class CompanyRepository:
    """
    Repository Pattern: abstracts SQL logic into a reusable interface.
    """
    def __init__(self, conn):
        # TODO: Store connection and create a cursor
        pass

    def get_company_by_symbol(self, symbol):
        # TODO: Validate symbol using regex
        # TODO: Query company_info table by symbol
        # TODO: Handle any errors using try/except
        pass

    def get_stock_data_by_company(self, company_name):
        # TODO: Query stock_market_data table by company name
        # TODO: Return result list or handle errors
        pass