import time
from threading import Thread,Lock
lock = Lock()
class Even(Thread):
    def run(self):
        for i in range(0,100,2):
            with lock:
                print("Even: ",i)
                time.sleep(1)

class Odd(Thread):
    def run(self):
        for i in range(1,100,2):
            with lock:
                print("Odd: ",i)
                time.sleep(1)

e = Even()
o = Odd()
e.start(),o.start()
e.join(),o.join()
print("Program Ended")