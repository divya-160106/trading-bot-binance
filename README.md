#  Binance Futures Testnet Trading Bot

A lightweight Python CLI application to place **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M).  
Built with clean architecture, structured logging, and robust error handling.

---

## Features

- **Place Orders:** Supports MARKET and LIMIT order types  
- **Directional Trading:** Supports both BUY and SELL  
- **CLI Interface:** Command-line input via `argparse`  
- **Validation:** Input validation for symbol, side, type, quantity, and price  
- **Logging:** Structured logging for requests, responses, and errors  
- **Error Handling:** Handles API and validation errors gracefully  
- **Modular Design:** Separation between client, logic, and CLI layers  

---

## Project Structure


trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│ └── cli.py
│
├── logs/ # Ignored in repo (used locally)
│ └── bot.log
│
├── .env # Not included (contains API keys)
├── requirements.txt
└── README.md


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/divya-160106/trading-bot-binance.git
cd trading_bot
2. Install dependencies
pip install -r requirements.txt
3. Setup environment variables

Create a .env file in the root directory:

BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
4. Binance Testnet Setup
Register at: https://testnet.binancefuture.com
Go to API Management
Generate API keys
Ensure Futures Testnet is enabled
---

Usage
🔹 Place a MARKET order
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
🔹 Place a LIMIT order
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --qty 0.003 --price 20000
Sample Output
=== Order Request ===
Symbol   : BTCUSDT
Side     : BUY
Type     : LIMIT
Quantity : 0.003
Price    : 20000.0

=== Order Response ===
Order ID     : 13095676683
Status       : NEW
Executed Qty : 0.0000
Avg Price    : 0.00

Order placed successfully!
---

Logging

All API activity is logged locally in:

logs/bot.log
Example Logs

MARKET Order

2026-05-01 12:37:31 | INFO | REQUEST | symbol=BTCUSDT side=BUY type=MARKET qty=0.001 price=None
2026-05-01 12:37:32 | INFO | RESPONSE | orderId=13095640572 status=NEW executedQty=0.0000 avgPrice=0.00

LIMIT Order

2026-05-01 12:50:11 | INFO | REQUEST | symbol=BTCUSDT side=BUY type=LIMIT qty=0.003 price=20000.0
2026-05-01 12:50:12 | INFO | RESPONSE | orderId=13095676683 status=NEW executedQty=0.0000 avgPrice=0.00
---

Notes / Assumptions
Uses Binance Futures Testnet (USDT-M) only
Minimum order value must be ≥ 50 USDT
LIMIT orders may remain in NEW state if not filled
Tested primarily with BTCUSDT
---

Tech Stack
Python 3.x
python-binance
python-dotenv
argparse
logging
---

Future Improvements
Add Stop-Limit / OCO order support
Improve CLI UX (interactive prompts)
Build a lightweight UI dashboard
