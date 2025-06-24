# Binance Futures Trading Bot

A simple Python bot for placing orders on Binance Futures Testnet. Modular structure, logging, and easy configuration.

---

## 🚀 Features

- Tkinter-based desktop GUI
- Place MARKET, LIMIT, STOP_MARKET, STOP, TAKE_PROFIT, and OCO orders
- Modular codebase (config, core, logs, tests)
- Logging of all requests, responses, and errors
- Uses `.env` or `config/settings.py` for API keys
- Safe for learning & testing (Testnet only)

---

## 🗂️ Directory Structure

```
Tradingbot/
├── config/
│   └── settings.py
├── core/
│   ├── client.py
│   ├── orders.py
│   ├── utils.py
│   └── logging_config.py
├── logs/
│   └── binance_bot.log
├── tests/
│   └── test_orders.py
├── .env
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

1. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2. **Configure API keys**

    - Option 1: Create a `.env` file in the root directory:
        ```
        API_KEY=your_testnet_key
        API_SECRET=your_testnet_secret
        ```
    - Option 2: Edit `config/settings.py` with your keys.

3. **Run the app**
    ```bash
    python app.py
    ```

---

## 🧪 Example Input

| Field    | Value     |
|----------|-----------|
| Symbol   | BTCUSDT   |
| Side     | BUY       |
| Type     | LIMIT     |
| Quantity | 0.001     |
| Price    | 65000.0   |

---

## 📌 Notes

- **Works only on Binance Futures Testnet**
- Logging stored in `logs/binance_bot.log`
- For educational and testing purposes only

---