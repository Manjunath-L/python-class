import time
from threading import Thread


class print_names(Thread):
    def run(self):
        names = ["Rama","krishna","arjuna"]
        for data in names:
            print(data)
            time.sleep(2)

class print_num(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(2)

class sum(Thread):
    def run(self):
        a = 10
        b = 20
        c = a + b
        print(c)
        time.sleep(2)

pna = print_names()
pnu = print_num()
s = sum()

pna.start()
pnu.start()
s.start()

pna.join()
pnu.join()
s.join()

print("program terminated")