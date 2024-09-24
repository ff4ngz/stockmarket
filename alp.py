import requests
import alpaca_trade_api as tradeapi
from datetime import datetime

# Define the mapping of holidays to stocks (can be extended)
holiday_stock_mapping = {
    "Halloween": "SPY",
    "Thanksgiving": "XLP",
    "St. Patrick's Day": "BIR",
    "Christmas": "AMZN",
    "Valentine's Day": "HSY",
    "Mother's Day": "COST",
    "Father's Day": "HBI",
    "New Year's": "DIS",
}

# Your Alpaca API credentials
ALPACA_API_KEY = 'PKLSAC0BSIJY9VIEPLGF'
ALPACA_SECRET_KEY = 'Kdwmxj153OGX6UUM85OGeJR2yJ7a6XPhqmymU9gX'
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'

# Create an Alpaca API instance
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

# Function to check if today is a holiday
def is_today_holiday():
    today = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=efd4005bc9834b03b9b32d3876a9fcf4&country=US&year=2020&month=12&day=25")
    
    if response.status_code == 200:
        holidays_data = response.json()
        return len(holidays_data) > 0  # Return True if there are any holidays today
    else:
        print(f"Error fetching holiday data: {response.json()}")
        return False

# Function to buy stock for holidays
def buy_stock_if_today_is_holiday():
    if is_today_holiday():
        stock_to_buy = "AMZN"  # Default to Amazon
        api.submit_order(
            symbol=stock_to_buy,
            qty=2,  # Buy 2 stocks
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"Bought 2 shares of {stock_to_buy} because today is a holiday!")
    else:
        print("Today is not a holiday.")

# Run the function*
buy_stock_if_today_is_holiday()