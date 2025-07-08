import os
import requests
from telegram import Bot
from time import sleep

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    btc = data.get("bitcoin", {}).get("usd")
    eth = data.get("ethereum", {}).get("usd")
    return btc, eth

def main():
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text="✅ ربات روشن شد و فعاله 🚀")
    
    while True:
        try:
            btc, eth = get_prices()
            message = (
                "📊 قیمت‌ها:\n"
                f"💰 بیت‌کوین: ${btc}\n"
                f"🪙 اتریوم: ${eth}"
            )
            bot.send_message(chat_id=CHAT_ID, text=message)
        except Exception as e:
            print(f"خطا: {e}")
        sleep(10800)  # هر ۳ ساعت

if __name__ == "__main__":
    main()
