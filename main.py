import jdatetime
from telegram import Bot

# جایگزین کن:
TELEGRAM_TOKEN = '8194641881:AAG00njWpVCd2XML33fEqTJ4ivMD8WUp5sM'
YOUR_CHAT_ID = 113793191

projects = {
    1: {'day': 1, 'name': 'ایکا'},
    2: {'day': 5, 'name': 'پروژه 2'},
    3: {'day': 10, 'name': 'پروژه 3'},
    # ... ادامه بده
}

today_day = jdatetime.date.today().day
bot = Bot(token=TELEGRAM_TOKEN)

for project_id, info in projects.items():
    if info['day'] == today_day:
        message = f"امروز موعد پرداخت {info['name']} است."
        bot.send_message(chat_id=YOUR_CHAT_ID, text=message)
