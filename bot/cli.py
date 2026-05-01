import argparse
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.orders import place_market_order, place_limit_order
from bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Validation
        validate_symbol(args.symbol)
        args.side = validate_side(args.side)
        args.type = validate_order_type(args.type)
        validate_quantity(args.qty)
        validate_price(args.type, args.price)

        # Print request
        print("\n=== Order Request ===")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.qty}")
        if args.price:
            print(f"Price    : {args.price}")

        logger.info(
            f"REQUEST | symbol={args.symbol} side={args.side} "
            f"type={args.type} qty={args.qty} price={args.price}"
        )

        # Execute order
        if args.type == "MARKET":
            response = place_market_order(args.symbol, args.side, args.qty)
        else:
            response = place_limit_order(
                args.symbol, args.side, args.qty, args.price
            )

        logger.info(
            f"RESPONSE | orderId={response.get('orderId')} "
            f"status={response.get('status')} "
            f"executedQty={response.get('executedQty')} "
            f"avgPrice={response.get('avgPrice')}"
        )

        # Print response
        print("\n=== Order Response ===")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

        print("\nOrder placed successfully!")

    except Exception as e:
        logger.error(f"ERROR | {str(e)}", exc_info=True)
        print("\nOrder failed:", str(e))


if __name__ == "__main__":
    main()