import os
import requests
from flask import Flask
from telegram import Bot
from telegram.error import TelegramError

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
last_prices = {}

def get_prices():
    try:
        response = requests.get("https://api.nobitex.ir/market/stats")
        data = response.json()["market"]

        prices = {
            "طلا ۱۸ عیار": int(float(data["gold18"]["latest"])),
            "دلار (تتر)": int(float(data["usdt-rls"]["latest"])),
            "یورو": int(float(data["eur-rls"]["latest"])),
            "بیت‌کوین": int(float(data["btc-usdt"]["latest"])),
        }

        return prices
    except Exception as e:
        print(f"خطا در دریافت قیمت‌ها: {e}")
        return None

def compare_prices(new_prices):
    global last_prices
    result_lines = []

    for name, price in new_prices.items():
        if name in last_prices:
            if price > last_prices[name]:
                symbol = "🟢"
            elif price < last_prices[name]:
                symbol = "🔴"
            else:
                symbol = "⚪️"
        else:
            symbol = "⚪️"

        line = f"{name}: {price:,} تومان {symbol}"
        result_lines.append(line)

    last_prices = new_prices
    return "\n".join(result_lines)

def send_update():
    if not TOKEN or not CHAT_ID:
        return "❌ توکن یا چت‌آیدی تنظیم نشده"

    bot = Bot(token=TOKEN)
    prices = get_prices()

    if prices:
        message = compare_prices(prices)
        message += "\n\n📡 @Forexfaarsi"

        try:
            bot.send_message(chat_id=CHAT_ID, text=message)
            return "✅ قیمت‌ها ارسال شد"
        except TelegramError as e:
            return f"❌ خطا در ارسال پیام: {e}"
    else:
        return "❌ دریافت قیمت‌ها ناموفق بود"

@app.route("/")
def index():
    return send_update()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
