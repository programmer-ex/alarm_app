import random
import time
from playsound import playsound
import os

songs = [f for f in os.listdir() if f.endswith('.mp3')]
if not songs:
    print("MP3ファイルが見つかりません。")
    exit()

selected_song = random.choice(songs)

print("5秒後に音楽を再生します...")
time.sleep(5)
print(f"再生中: {selected_song}")
playsound(selected_song)
