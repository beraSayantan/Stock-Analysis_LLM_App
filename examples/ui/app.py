import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("Nifty 50 Stocks Ananlysis 📈")
st.markdown(
    """
    ## How to use:
    
    Enter a query concerning a price-action choice for any Nifty 50 stock or the whole market, and the AI will deliver a conclusion, as well as reason and explanation based on financial research.

    ---
    """
)

question = st.text_input(
    "Enter your question here (Please mention the stock by ticker symbol) ",
    placeholder="E.g., What will be my price-action decision for RELIANCE.NS stock today? , Find best stocks to buy today.",
)

# Handle the query submission
if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to obtain insights. Status code: {response.status_code}")