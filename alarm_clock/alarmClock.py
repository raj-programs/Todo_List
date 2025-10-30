from tkinter import *
from datetime import datetime, timedelta
import os

# Initialize global variables
alarm_time = None
alarm_active = False

# ----------------- Alarm Functions -----------------
def set_alarm():
    global alarm_time, alarm_active
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm_active = True
    status_label.config(text=f"Alarm set for {alarm_time}")
    snooze_btn.pack_forget()
    stop_btn.pack_forget()
    check_alarm()  # start checking

def check_alarm():
    global alarm_active
    if not alarm_active:
        return
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        status_label.config(text="⏰ Wake up!")
        try:
            os.system("start alarm.mp3")  # play sound
        except:
            print("Could not play alarm sound.")
        snooze_btn.pack(pady=5)
        stop_btn.pack(pady=5)
    else:
        root.after(1000, check_alarm)  # check every second

def stop_alarm():
    global alarm_active
    alarm_active = False
    status_label.config(text="Alarm stopped.")
    snooze_btn.pack_forget()
    stop_btn.pack_forget()

def snooze_alarm():
    global alarm_time
    now = datetime.now()
    snooze_time = (now + timedelta(minutes=5)).strftime("%H:%M:%S")
    alarm_time = snooze_time
    status_label.config(text=f"Snoozed until {snooze_time}")
    snooze_btn.pack_forget()
    stop_btn.pack_forget()
    check_alarm()

# ----------------- GUI -----------------
root = Tk()
root.title("Interactive Alarm Clock")
root.geometry("400x250")

Label(root, text="Set Time for Alarm", font=("Arial", 14)).pack(pady=10)

frame = Frame(root)
frame.pack()

hour = StringVar(value="00")
minute = StringVar(value="00")
second = StringVar(value="00")

Entry(frame, textvariable=hour, width=3, font=("Arial", 20)).pack(side=LEFT)
Label(frame, text=":", font=("Arial", 20)).pack(side=LEFT)
Entry(frame, textvariable=minute, width=3, font=("Arial", 20)).pack(side=LEFT)
Label(frame, text=":", font=("Arial", 20)).pack(side=LEFT)
Entry(frame, textvariable=second, width=3, font=("Arial", 20)).pack(side=LEFT)

Button(root, text="Set Alarm", command=set_alarm, font=("Arial", 12), bg="lightblue").pack(pady=10)

status_label = Label(root, text="", font=("Arial", 12))
status_label.pack()

# Create Stop and Snooze buttons but don't pack yet
stop_btn = Button(root, text="Stop", command=stop_alarm, bg="red", font=("Arial", 12))
snooze_btn = Button(root, text="Snooze", command=snooze_alarm, bg="yellow", font=("Arial", 12))

root.mainloop()
