import time
from threading import Thread,Condition

condition = Condition()
turn = "odd"
class Even(Thread):
    def run(self):
        global turn
        for i in range(0,100,2):
            with condition:
                while turn != "even":
                    condition.wait()
                print("Even :",i)
                time.sleep(1)
                turn = "odd"
                condition.notify()

class Odd(Thread):
    def run(self):
        global turn
        for i in range(1,100,2):
            with condition:
                while turn != "odd":
                    condition.wait()
                print("Odd: ",i)
                time.sleep(1)
                turn = "even"
                condition.notify()

e = Even()
o = Odd()
e.start(),o.start()
e.join(),o.join()
print("Program Ended")