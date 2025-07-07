import os
import requests
import time
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

SYMBOL = 'XAUUSDT'
INTERVAL = '60m'

bot = Bot(token=TELEGRAM_TOKEN)
last_signal = None

def send_signal(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def get_klines(symbol, interval, limit=100):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    return data

def calculate_ema(prices, window):
    ema_values = []
    k =
