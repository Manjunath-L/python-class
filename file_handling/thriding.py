import time
class VLC:
    def apl_open(self):
        print("VLC application opened")
        time.sleep(3)
    def video_play(self):
        print("Video starting playing")
        time.sleep(3)
    def audio_play(self):
        print("Audio started playing")
        time.sleep(3)
    def timer_on(self):
        print("Time is on")
        time.sleep(3)
    def prog_bar(self):
        print("progress bar is active")
        time.sleep(3)

v = VLC()
v.apl_open()
v.video_play()
v.audio_play()
v.timer_on()
v.prog_bar()
print("Application closed")