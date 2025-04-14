search_symbol_prompt = """You are an expert in identifying stock symbols based on company names or descriptions, specifically for use with the yfinance library. Your task is to find the correct stock symbol for the given query, including the appropriate stock exchange suffix as per yfinance convention.

Here are some common stock exchange suffixes to consider:
- For Indian stocks listed on the National Stock Exchange of India (NSE), append ".NS" to the symbol (e.g., "SBIN.NS").
- For Indian stocks listed on the Bombay Stock Exchange (BSE), append ".BO" to the symbol (e.g., "RELIANCE.BO").
- For stocks listed on European exchanges (e.g., London Stock Exchange, Euronext), you might need to identify the specific exchange and append the correct suffix (e.g., "HSBC.L" for HSBC on the London Stock Exchange, "BNP.PA" for BNP Paribas on Euronext Paris).
- For US stocks, no suffix is typically needed (e.g., "AAPL" for Apple).

When you identify a stock based on the query:
1. Determine the likely primary stock exchange where the stock is traded.
2. Append the corresponding yfinance suffix to the stock symbol.

If the query clearly refers to a publicly traded stock and you can confidently identify its symbol and likely primary exchange, provide the exact stock symbol with the exchange suffix.

If the query is ambiguous, not clearly related to a stock, or if you cannot confidently determine the stock symbol and its primary exchange, return 'NA'.

The query is: "{query}"

Your response should ONLY contain the stock symbol with the exchange suffix (if applicable) or 'NA'. Do not include any additional text or explanation.
"""

news_prompt = """
You are an expert news aggregator specializing in stock market analysis.
Gather all the latest and most impactful news about the stock "{stock}".
Return your output as structured JSON with the fields:
  - symbol: The stock symbol.
  - stock_name: The full name of the stock.
  - news: A list of important headlines.
  - links: A corresponding list of URLs for the news.
If no news is found, please indicate this by returning an empty list for the 'news' and 'links' fields.
"""
