import time
from queue import Queue
from threading import Thread

even_q = Queue()
odd_q = Queue()

class Even(Thread):
    def run(self):
        for i in range(0,100,2):
            even_q.put(i)
            time.sleep(1)

class Odd(Thread):
    def run(self):
        for i in range(1,100,2):
            odd_q.put(i)
            time.sleep(1)

e = Even()
o = Odd()
e.start()
o.start()
for _ in range(50):
    even_val = even_q.get()
    odd_val = odd_q.get()
    print(f"Even: {even_val}\n"
          f" Odd: {odd_val}")

e.join()
o.join()
print("Program ended")