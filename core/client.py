from binance.client import Client
from config.settings import API_KEY, API_SECRET, TESTNET, BASE_URL

def create_client():
    client = Client(API_KEY, API_SECRET)
    if TESTNET:
        client.FUTURES_URL = BASE_URL
    return client