import os
import requests
from telegram import Bot
from telegram.error import TelegramError
from time import sleep

TOKEN = os.getenv("TELEGRAM_TOKEN")  # توکن ربات از متغیر محیطی می‌گیریم
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # آیدی کانال یا گروه هدف

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,usd,euro&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    bitcoin_price = data.get("bitcoin", {}).get("usd")
    usd_price = 1  # چون دلار به دلار = 1
    euro_price = data.get("euro", {}).get("usd")
    return bitcoin_price, usd_price, euro_price

def main():
    bot = Bot(token=TOKEN)
    while True:
        try:
            btc, usd, eur = get_prices()
            message = (
                f"💰 قیمت‌ها:\n"
                f"بیت‌کوین: ${btc}\n"
                f"دلار: ${usd}\n"
                f"یورو: ${eur}\n"
            )
            bot.send_message(chat_id=CHAT_ID, text=message)
        except TelegramError as e:
            print(f"خطا در ارسال پیام: {e}")
        sleep(3600)  # هر ۱ ساعت قیمت‌ها رو می‌فرسته

if __name__ == "__main__":
    main()
