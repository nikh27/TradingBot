from core.logging_config import logger

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == 'LIMIT':
            params.update({
                "timeInForce": 'GTC',
                "price": price
            })

        elif order_type in ['STOP_MARKET', 'STOP', 'TAKE_PROFIT']:
            params.update({
                "stopPrice": stop_price,
                "timeInForce": 'GTC'
            })
            if price:
                params["price"] = price
                params["type"] = "STOP"

        elif order_type == 'OCO':
            logger.info(f"[OCO REQUEST] Params: {symbol=} {side=} {quantity=} {price=} {stop_price=}")
            order = client.create_oco_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                stopLimitPrice=price,
                stopLimitTimeInForce='GTC'
            )
            logger.info(f"[OCO RESPONSE] {order}")
            return order

        logger.info(f"[ORDER REQUEST] {params}")
        order = client.futures_create_order(**params)
        logger.info(f"[ORDER RESPONSE] {order}")
        return order

    except Exception as e:
        logger.error(f"[ORDER ERROR] {e}")
        return {"error": str(e)}
