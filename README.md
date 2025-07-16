# Payroll Vacancy Bot

Цей бот щодня шукає вакансії Payroll Accountant у Вроцлаві або Remote і надсилає їх у Telegram.

## Інструкція

1. Створи `.env` файл зі змінними:
```
TELEGRAM_TOKEN=твій_токен
TELEGRAM_USER_ID=твій_ID
```

2. Встанови залежності:
```
pip install -r requirements.txt
```

3. Запусти:
```
python bot.py
```

4. Додай Cron Job у Render для автоматичного запуску щодня.
