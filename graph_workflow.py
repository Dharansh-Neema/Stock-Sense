from langgraph.graph import StateGraph
from util_def import search_keyword,latest_news,get_ticker,analyze_stock_data
import os
from pydantic_class import AgentState 
from logger import setup_logger
from test_output import news_data,graph_data
logger = setup_logger(name="graph_workflow",log_file="logs/graph_workflow.log")
def search(agentState:AgentState):
    """This will search the stock and return symbol of it."""
    try:
        q = agentState['query']
        symbol = search_keyword(query=q)
        agentState['symbol'] = symbol
        print(agentState)
        logger.debug("Searched for symbol")
        return agentState
    except Exception as e:
        logger.error("Unexpected error occured",e)
        raise e

def get_graph_data(agentState:AgentState):
    """It will reterive the graph for the given symbol"""
    try:
        data = get_ticker(agentState['symbol'])
        print(data)
        agentState['graph_data'] = data
        logger.debug("stock ticker data collected ")
        return agentState

    except Exception as e:
        logger.error("Unexpected error occcurred while generating data for graph.")
        raise e
def get_latest_news(agentState:AgentState):
    """It will reterive the latest news about that stock"""
    try:
        news_data = latest_news(agentState['symbol'])
        result = []
        top_count = min(20, len(news_data.headline))
        for i in range(top_count):
            result.append({
                "headline":news_data.headline[i],
                "summary":news_data.summary[i]
            })
        # print(result)
        logger.debug("Successfully retrieved and structured the top %d news items for symbol: %s", top_count, agentState['symbol'])
        agentState['news_data'] = result
        return agentState
    except Exception as e:
        logger.error("Unexpected error while getting latest news.",e)
        raise e

def agent_analysis(agentState: dict) -> dict:
    """
    Performs analysis on the stock using the latest stock price, volume, and news trend.
    It calls the analysis agent and extracts key fields such as sentiment, recommendation,
    reasoning, and news summary from the agent's output.
    
    Parameters:
        agentState (dict): A dictionary that must contain 'symbol', 'graph_data', and 'news_data'.
    
    Returns:
        dict: The agentState dictionary updated with the analysis under the key 'agent_analysis'.
        
    Raises:
        Exception: Propagates any exception encountered during processing.
    """
    try:
        symbol = agentState['symbol']
        graph_data = agentState['graph_data']
        news_data = agentState['news_data']
        
        # Get analysis from our agent. This function is assumed to return either a list or dict.
        agentAnalysis = analyze_stock_data(symbol, realtime_data=graph_data, news_data=news_data)
        # print(agentAnalysis.get('StockAnalysis'))
        logger.debug("Agent analysis successfully completed for symbol: %s", symbol)
        agentState['agent_analysis'] = agentAnalysis
        return agentState
    
    except Exception as e:
        logger.error("Unexpected error while doing agent analysis", exc_info=True)
        raise e
if __name__ == '__main__':
    ag = {}
    ag.update(query="Apple stock analysis")
    ag.update(symbol="AAPL")
    ag.update(graph_data=graph_data)
    ag.update(news_data=news_data)
    # search(ag)
    # print(get_graph_data(ag))
    # print(get_latest_news(ag))
    print(agent_analysis(ag))