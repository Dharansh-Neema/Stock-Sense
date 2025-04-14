from pydantic import BaseModel,Field
from typing import List
class SearchOutput(BaseModel):
    symbol: str = Field(description="Stock symbol as per yfinance (e.g., AAPL, MSFT). Returns 'NA' if no stock symbol is found.")


class NewsSearchResult(BaseModel):
    symbol: str = Field(..., description="Stock symbol")
    stock_name: str = Field(..., description="Name of the stock")
    headline: List[str] = Field(..., description="List of important news related to the stock")
    summary : List[str] = Field(...,description="Summary of the news report")
    links: List[str] = Field(..., description="List of links associated with the news sources")

class AgentState(BaseModel):
    query : str
    symbol : str



