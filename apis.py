import os
from dotenv import load_dotenv
import pykalshi
import requests
import pandas as pd

load_dotenv()

# Kalshi with your exact PEM file
kalshi_client = None
if os.path.exists('kalshi_private.pem'):
    with open('kalshi_private.pem', 'r') as f:
        pem = f.read().strip()
    kalshi_client = pykalshi.Kalshi(
        api_key_id=os.getenv('KALSHI_ACCESS_KEY'),
        private_key_pem=pem
    )

def get_kalshi_market(ticker):
    if not kalshi_client:
        return {"error": "Kalshi not loaded"}
    return kalshi_client.get_market(ticker)

# Rest of your functions (Polygon, Binance crypto, Polymarket) unchanged from previous
# ... (add your existing get_stock_data, get_crypto_data, etc.)