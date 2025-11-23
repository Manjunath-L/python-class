import time
from threading import Thread
class VLC(Thread):
    def run(self):
        print("VLC application opened")
        time.sleep(3)

class video(Thread):
    def run(self):
        print("video started playing")
        time.sleep(3)

class audio(Thread):
    def run(self):
        print("Audio started playing")
        time.sleep(3)

class timer(Thread):
    def run(self):
        print("Timer is on")
        time.sleep(3)

class prog_bar(Thread):
    def run(self):
        print("Progress bar is activated")
        time.sleep(3)

v1 = VLC()
v2 = video()
v3 = audio()
v4 = timer()
v5 = prog_bar()

v1.start()
v2.start()
v3.start()
v4.start()
v5.start()

print("\nApplication closed")