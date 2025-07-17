import os
from dotenv import load_dotenv
from job_sources.linkedin import get_linkedin_jobs
from utils.helpers import send_telegram_message

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID")

print("🚀 Бот запущено")
print(f"📦 TOKEN знайдено: {bool(TELEGRAM_TOKEN)}")
print(f"👤 USER_ID: {TELEGRAM_USER_ID}")

def main():
    try:
        jobs = get_linkedin_jobs()
        print(f"🔍 Знайдено вакансій: {len(jobs)}")

        if not jobs:
            send_telegram_message(TELEGRAM_TOKEN, TELEGRAM_USER_ID, "🔍 Нових вакансій не знайдено.")
            return

        for job in jobs:
            send_telegram_message(TELEGRAM_TOKEN, TELEGRAM_USER_ID, job)

        print("✅ Повідомлення надіслано")

    except Exception as e:
        print(f"❌ ПОМИЛКА: {e}")

if __name__ == "__main__":
    main()

