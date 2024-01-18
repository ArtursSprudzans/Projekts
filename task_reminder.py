from datetime import datetime
import time

def task_reminder(task, time_to_remind):
  while True:
    current_time = datetime.now(),strftime("%H:%M:%S")
    if current_time == time_to_remind:
      print(f"Reminder: {Uzdevums}")
      break
    time.sleep(60)

task_reminder("Iznes ārā miskasti", "08:00:00")
