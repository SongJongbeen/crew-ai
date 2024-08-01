from crewai_tools import BaseTool
from crewai_tools import tool
from crewai_tools import ScrapeWebsiteTool
import yfinance as yf
from typing import ClassVar

class StockNewsTool(BaseTool):
    name: str = "stock_news"
    description: str = (
        "Useful to get news about a stock."
        "The input should be a ticker, for example AAPL, NET."
    )

    def _run(self, ticker: str) -> str:
        ticker = yf.Ticker(ticker)
        return ticker.news

class StockPriceTool(BaseTool):
    name: str = "stock_price"
    description: str = (
        "Useful to get the stock price data."
        "The input should be a ticker, for example AAPL, NET."
    )

    def _run(self, ticker: str) -> str:
        ticker = yf.Ticker(ticker)
        return ticker.history(period="1mo")
    
class IncomeStmtTool(BaseTool):
    name: str = "income_stmt"
    description: str = (
        "Useful to get the income statement of a company."
        "The input to this tool should be a ticker, for example AAPL, NET."
    )

    def _run(self, ticker: str) -> str:
        ticker = yf.Ticker(ticker)
        return ticker.income_stmt

class BalanceSheetTool(BaseTool):
    name: str = "balance_sheet"
    description: str = (
        "Useful to get the balance sheet of a company."
        "The input to this tool should be a ticker, for example AAPL, NET."
    )

    def _run(self, ticker: str) -> str:
        ticker = yf.Ticker(ticker)
        return ticker.balance_sheet

class InsiderTransactionsTool(BaseTool):
    name: str = "insider_transactions"
    description: str = (
        "Useful to get the insider transactions of a company."
        "The input to this tool should be a ticker, for example AAPL, NET."
    )

    def _run(self, ticker: str) -> str:
        ticker = yf.Ticker(ticker)
        return ticker.insider_transactions
