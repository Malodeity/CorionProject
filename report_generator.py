# ======================================================
# 📄 FILE: report_generator.py
# PURPOSE: Generate PDF report
# EXPECTED:
# - Class for formatting and exporting reports
# - Summary line and recent stock data
# RULES:
# - Handle errors, external packages (Unit 8)
# OUTCOME:
# - Build readable, exportable business reports
# ======================================================

from fpdf import FPDF

class PDFReport:
    """
    Generates a simple PDF report for stock summary.
    Contains company info and recent stock prices.
    """
    def __init__(self, company, stock_records, avg_close):
        # TODO: Save params, initialize FPDF instance
        pass

    def generate(self, filename):
        try:
            # TODO: Add company summary and stock stats to PDF
            pass
        except Exception as e:
            print(f"PDF error: {e}")
