def get_prices():
    try:
        response = requests.get("https://api.nobitex.ir/market/stats")
        print("API Response:", response.text)
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
