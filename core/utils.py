def is_valid_symbol(symbol):
    return symbol.endswith('USDT') and len(symbol) >= 6

def is_valid_side(side):
    return side.upper() in ["BUY", "SELL"]

def get_order_types():
    return ["MARKET", "LIMIT", "STOP_MARKET", "STOP", "TAKE_PROFIT", "OCO"]
