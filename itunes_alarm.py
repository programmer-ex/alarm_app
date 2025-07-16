import random
import time
import datetime
import subprocess

songs = [
    "花占い",
    "終わりなき旅",
    "Starting Over"
    "彩り"
]

selected_song = random.choice(songs)

target_hour = 7
target_minute = 00

print(f"{target_hour}:{target_minute} にアラームが鳴ります...")

while True:
    now = datetime.datetime.now()
    if now.hour == target_hour and now.minute == target_minute:
        break
    time.sleep(30)  # 30秒ごとに確認


applescript = f'''
tell application "Music"
    activate
    play track "{selected_song}"
end tell
'''

subprocess.run(["osascript", "-e", applescript])
