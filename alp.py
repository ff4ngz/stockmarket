import requests
import alpaca_trade_api as tradeapi
from datetime import datetime
import os 
from dotenv import load_dotenv # Load environment variables from .env file
load_dotenv()


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
API_KEY_ID = os.getenv("APCA_API_KEY_ID")
print(API_KEY_ID)
API_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY") # Your trading bot logic goes here
API_BASE_URL = os.getenv("APCA_API_BASE_URL")

# Create an Alpaca API instance
api = tradeapi.REST(API_KEY_ID, API_SECRET_KEY, base_url=API_BASE_URL)
print("login success")
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
