# === File: config/settings.py ===

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Testnet usage
TESTNET = True

# Binance Futures Testnet base URL
BASE_URL = 'https://testnet.binancefuture.com/fapi'
