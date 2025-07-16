import requests

def send_telegram_message(token, user_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)
