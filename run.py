import schedule
import time
import subprocess


def run_script():
    subprocess.run(["python3", "main.py"])


schedule.every().day.at("00:00").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(60)
