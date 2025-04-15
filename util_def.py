from logger import setup_logger
import os
logger = setup_logger(name="util_def", log_file="logs/util_def.log")
from langchain_google_genai import ChatGoogleGenerativeAI

from pydantic_class import SearchOutput,NewsSearchResult,StockAnalysis
from prompts import search_symbol_prompt,news_prompt,stock_analysis_prompt
# from test_output import graph_output,news_response
import requests
from dotenv import load_dotenv
import yfinance as yf
import json
import finnhub
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from typing import Any, Dict
load_dotenv()
# Initialize the LLM
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=os.getenv('GOOGLE_API_KEY')
    )
    # llm = ChatOpenAI(
    #     model="gpt-4o",
    #     api_key=os.getenv('OPENAI_API_KEY')
    # )
    logger.info("LLM initialized successfully.")
except Exception as e:
    logger.error(f"Error initializing LLM: {e}")
    raise e

# Define the output schema

def search_keyword(query: str):
    """This function will return the stock symbol of the asked stock."""
    logger.info(f"Searching for stock symbol for query: {query}")
    try:
        llm_output = llm.with_structured_output(SearchOutput)
        formatted_prompt = search_symbol_prompt.format(query=query)
        answer = llm_output.invoke(formatted_prompt)
        print(f"Found Symbol: {answer.symbol}")
        return answer.symbol
    except Exception as e:
        logger.error(f"Unexpected error occurred while finding symbol: {e}")
        return e


def get_ticker(symbol: str):
    """
    Given a symbol name for a stock, this function returns the latest intraday
    information
    Parameters:
        symbol (str): The stock ticker symbol as required by yfinance (e.g., "AAPL", "HDFCBANK.NS").

    Returns:
        str: A JSON string that contains the symbol, a list of time-close dictionary entries as price_data,
             and a list of time-volume dictionary entries as volume_data.
    """
    try:
        # Download stock data for the last 1 day with 5-minute intervals
        data = yf.download(symbol, period="1d", interval="15m")
        
        # If no data is available, return an error message in JSON
        if data.empty:
            return json.dumps({"error": f"No data available for symbol {symbol}"})
        
        # Extract times as strings
        times = data.index.strftime('%Y-%m-%d %H:%M:%S').tolist()

        # Extract close prices, ensuring the object is a Series and then rounding values
        close_prices = data['Close'].squeeze().round(2).tolist()
        
        # Extract volume data
        volume_values = data['Volume'].squeeze().tolist()
        
        result = {
            "symbol": symbol,
            "price_data": [{"time": t, "close": c} for t, c in zip(times, close_prices)],
            "volume_data": [{"time": t, "volume": v} for t, v in zip(times, volume_values)]
        }
        
        logger.debug("Fetched the data for the given stock symbol successfully!")
        return json.dumps(result, indent=4)
    except Exception as e:
        logger.error("Unexpected error occurred while fetching and generating the data", e)
        raise e
    
def latest_news(symbol: str) -> str:
    """
        Fetch the latest news for a given stock symbol using finnhub.
    The output is returned in a structured JSON format that contains:
        - symbol: The queried stock symbol.
        - stock_name: The full name of the stock (using symbol as a placeholder if not available).
        - headline: A list of news headlines.
        - summary: A list of news summaries.
        - links: A list of news article URLs.
    """
    try:
        finnhub_api_key = os.getenv("FINNHUB_API_KEY")
        if not finnhub_api_key:
            raise ValueError("Finnhub API key is not set in environment variables.")

        # Initialize finnhub client
        finnhub_client = finnhub.Client(api_key=finnhub_api_key)
        
        # Fetch company news from finnhub for a given date range.
        # Adjust the _from and to dates as needed.
        news = finnhub_client.company_news(symbol, _from="2025-04-05", to="2025-04-15")
        logger.debug("Fetched the news successfully from finnhub")

        if news:
            newsRes = NewsSearchResult(
                symbol=symbol,
                headline=[item.get("headline", "") for item in news],
                summary=[item.get("summary", "") for item in news],
                links=[item.get("url", "") for item in news]
            )
            logger.debug("Successfully formatted the news in structured format")
            
            return newsRes
        else:
            logger.debug("No news found for the requested symbol")
            empty_result = NewsSearchResult(
                symbol=symbol,
                stock_name=symbol,
                headline=[],
                summary=[],
                links=[]
            )
            return empty_result
    
    except Exception as e:
        logger.error("Unexpected error occurred while fetching news.", exc_info=True)
        raise e

def analyze_stock_data(symbol,realtime_data, news_data):
    """
    Analyzes realtime stock data along with related news and returns a structured recommendation.
    
    This function uses an LLM agent to process the provided stock data and news summary.
    The agent returns its analysis in a structured JSON format defined by the StockAnalysis model.
    
    Parameters:
        realtime_data (str): A string containing the realtime stock information.
        news_data (str): A string with related news summaries and events.
    
    Returns:
        dict: The structured analysis result including the stock symbol, sentiment, recommendation,
              reasoning, and a summary of the news.
    
    Raises:
        Exception: Any exceptions encountered during analysis are logged and raised.
    """
    try:
        # Define tools if needed. In this example, we assume an empty list.
        tools = []
        # Create the agent using the global llm instance
        agent = create_react_agent(llm, tools, response_format=StockAnalysis)
        
        # Format the prompt by injecting the realtime_data and news_data into the prompt.
        formatted_prompt = stock_analysis_prompt.format(symbol=symbol,stock=realtime_data, news=news_data)
        
        payload = {'messages': [('user', formatted_prompt)]}
        response = agent.invoke(payload)
        structured_response = response.get('structured_response')
        result = []
        result.append(structured_response)
        if not structured_response:
            logger.warning("No structured response was returned by the agent.")
            return {}
        
        logger.debug("Stock analysis completed successfully for the provided data.")
        
        # Return the structured response. It's already of type dict if parsed correctly.
        return structured_response.dict()
    
    except Exception as e:
        logger.error("Unexpected error occurred while analyzing the stock data.", exc_info=True)
        raise e


# Example usage
# search_keyword("SBI stock analysis")
# search_keyword("Apple company")
# search_keyword("HDFC BANK stock")
# print(get_ticker("AAPL"))
# print(latest_news("AAPL"))

# print(analyze_stock_data(graph_output,news_response))
