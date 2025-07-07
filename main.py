from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

@app.route("/")
def index():
    return "✅ Bot is running"

@app.route("/send")
def send_signal():
    text = request.args.get("text")
    if not text:
        return "❌ No text provided", 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    r = requests.post(url, json=payload)

    if r.status_code == 200:
        return "✅ Message sent"
    else:
        return f"❌ Failed: {r.text}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
