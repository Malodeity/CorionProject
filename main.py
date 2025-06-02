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

from database import SupabaseClientFactory, CompanyRepository, is_valid_symbol
from models import Company, StockRecord
from utils import calculate_average_close, StrategyContext, filter_high_volume, sort_by_close
from report_generator import PDFReport
import tkinter as tk
from tkinter import simpledialog

class StockAnalysisService:
    """
    Service Layer for orchestrating the stock report generation.
    Handles input, validation, transformation, and reporting.
    """
    def __init__(self, company_repo):
        self.repo = company_repo

    def run_report_for_symbol(self, symbol):
        if not is_valid_symbol(symbol):
            print("Invalid stock symbol format.")
            return

        company_data = self.repo.get_company_by_symbol(symbol)
        if not company_data:
            print("Company not found.")
            return

        # TODO: Wrap company, fetch and map stock data
        # TODO: Filter/sort if needed, then calculate average
        # TODO: Generate PDF using injected strategy and singleton
        pass

if __name__ == "__main__":
    # GUI input
    root = tk.Tk()
    root.withdraw()
    symbol = simpledialog.askstring("Input", "Enter stock symbol (e.g. AAPL):")

    # DI: Setup repository and service manually
    client = SupabaseClientFactory.get_client()
    repository = CompanyRepository(client)
    service = StockAnalysisService(repository)

    if symbol:
        service.run_report_for_symbol(symbol.strip().upper())