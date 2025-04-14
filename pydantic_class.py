from pydantic import BaseModel,Field
from typing import List
class SearchOutput(BaseModel):
    symbol: str = Field(description="Stock symbol as per yfinance (e.g., AAPL, MSFT). Returns 'NA' if no stock symbol is found.")


class NewsSearchResult(BaseModel):
    symbol: str = Field(..., description="Stock symbol")
    headline: List[str] = Field(..., description="List of important news related to the stock")
    summary : List[str] = Field(...,description="Summary of the news report")
    links: List[str] = Field(..., description="List of links associated with the news sources")

class StockAnalysis(BaseModel):
    symbol: str = Field(..., description="The stock symbol.")
    sentiment: str = Field(..., description="Overall market sentiment regarding the stock.")
    recommendation: str = Field(..., description="Final recommendation for the stock, such as buy, sell, or hold.")
    reasoning: str = Field(..., description="The rationale behind the recommendation, highlighting key factors.")
    news_summary: str = Field(..., description="A summary of the news and events impacting the stock.")

class AgentState(BaseModel):
    query : str
    symbol : str



