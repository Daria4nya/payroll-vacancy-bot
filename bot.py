import os
from dotenv import load_dotenv
from job_sources.linkedin import get_linkedin_jobs
from utils.helpers import send_telegram_message

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_USER_ID = os.getenv("TELEGRAM_USER_ID")

def main():
    jobs = get_linkedin_jobs()
    if not jobs:
        send_telegram_message(TELEGRAM_TOKEN, TELEGRAM_USER_ID, "🔍 Нових вакансій не знайдено.")
        return

    for job in jobs:
        send_telegram_message(TELEGRAM_TOKEN, TELEGRAM_USER_ID, job)

if __name__ == "__main__":
    main()
