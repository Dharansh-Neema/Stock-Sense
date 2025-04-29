import streamlit as st
import json
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import requests
from pydantic_class import AgentState
# Set page config
st.set_page_config(
    page_title="Stock Sense Dashboard",
    page_icon="📈",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stTitle {
        font-size: 42px;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 20px;
    }
    .news-box {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .analysis-box {
        background-color: #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
    }
    </style>
    """, unsafe_allow_html=True)

def load_data(query: str):
    try:
        # Create AgentState object
        state = AgentState(
            query=query,
            symbol=""  # Will be populated by the backend
        )
        
        # Make API call to the FastAPI endpoint
        response = requests.post(
            url="http://localhost:8000/run-graph",
            json=state.dict()
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # Parse the graph_data if it's a string
        if isinstance(data.get('graph_data'), str):
            data['graph_data'] = json.loads(data['graph_data'])
            
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {str(e)}")
        return None

def create_price_chart(price_data):
    df = pd.DataFrame(price_data)
    df['time'] = pd.to_datetime(df['time'])
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['time'],
        y=df['close'],
        mode='lines',
        name='Price',
        line=dict(color='#1E88E5', width=2)
    ))
    
    fig.update_layout(
        title='Stock Price Movement',
        xaxis_title='Time',
        yaxis_title='Price ($)',
        template='plotly_white',
        height=400
    )
    return fig

def create_volume_chart(volume_data):
    df = pd.DataFrame(volume_data)
    df['time'] = pd.to_datetime(df['time'])
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['time'],
        y=df['volume'],
        name='Volume',
        marker_color='#42A5F5'
    ))
    
    fig.update_layout(
        title='Trading Volume',
        xaxis_title='Time',
        yaxis_title='Volume',
        template='plotly_white',
        height=300
    )
    return fig

def main():
    # Title
    st.markdown('<p class="stTitle">Stock Sense Dashboard</p>', unsafe_allow_html=True)
    
    # User input bar
    query = st.text_input("Enter your stock/company query", value="Bank of America analysis")
    
    if query:
        st.session_state['query'] = query
        data = load_data(query=query)

        if data:
            # Stock Info Header
            col1, col2, col3 = st.columns([2, 2, 2])
            with col1:
                st.metric("Symbol", data["symbol"])
            with col2:
                latest_price = data["graph_data"]["price_data"][-1]["close"]
                st.metric("Latest Price", f"${latest_price}")
            with col3:
                st.metric("Sentiment", data["agent_analysis"]["sentiment"])

            # Charts
            st.plotly_chart(create_price_chart(data["graph_data"]["price_data"]), use_container_width=True)
            st.plotly_chart(create_volume_chart(data["graph_data"]["volume_data"]), use_container_width=True)

            # Analysis and News Section
            col1, col2 = st.columns([3, 2])

            with col1:
                st.subheader("AI Analysis")
                st.markdown('<div class="analysis-box">', unsafe_allow_html=True)
                st.write(f"**Recommendation:** {data['agent_analysis']['recommendation']}")
                st.write(f"**Buy/Sell Price:** {data['agent_analysis']['buy_or_sell_price']}")
                st.write("**Reasoning:**")
                st.write(data['agent_analysis']['reasoning'])
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.subheader("Latest News")
                for news in data["news_data"][:5]:
                    st.markdown('<div class="news-box">', unsafe_allow_html=True)
                    st.write(f"**{news['headline']}**")
                    st.write(news['summary'])
                    st.markdown('</div>', unsafe_allow_html=True)
