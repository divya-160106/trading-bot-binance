def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT (e.g., BTCUSDT)")

def validate_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")

def validate_price(order_type, price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires price")