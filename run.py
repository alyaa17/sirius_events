import schedule
import time
import subprocess
import pytz


def run_script():
    subprocess.run(["python3", "main.py"])


schedule.every().day.at("10:44", "Europe/Moscow").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(60)
