from datetime import datetime

open_time = 10
close_time = 8

current_time = datetime.now().strftime("%I")
am_pm = datetime.now().strftime("%p")

current_time = int(current_time)

if am_pm == "AM" and current_time >= open_time:
    print("Shop status:The shop is open.")
elif am_pm == "PM" and (current_time < close_time or current_time == 12):
    print("Shop status:The shop is open.")
else:
    print("Shop status:The shop is closed.")
