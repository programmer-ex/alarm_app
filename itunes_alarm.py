import random
import time
import subprocess

songs = [
    "花占い",
    "終わりなき旅",
    "Starting Over"
]

selected_song = random.choice(songs)

print("5秒後にiTunesの曲を再生します...")
time.sleep(5)

applescript = f'''
tell application "Music"
    activate
    play track "{selected_song}"
end tell
'''

subprocess.run(["osascript", "-e", applescript])
