from playsound import playsound
import time

alarm_path = 'INSERT FULL ALARM PATH'

while True:
    playsound(alarm_path)
    time.sleep(60 * 15) # Every 15 minutes, play an alarm sound.