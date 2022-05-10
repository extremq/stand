from playsound import playsound
import time

alarm_path = 'alarm.wav'
alarm_count = 0

print(f"The alarm has been played 0 times.", end="\r")
while True:
    time.sleep(15 * 60) # Every 15 minutes, play an alarm sound.
    playsound(alarm_path)

    alarm_count += 1

    print(f"The alarm has been played {alarm_count} time(s).", end="\r")
