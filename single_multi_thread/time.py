import time


class Demo:
    def print_name(self):
        names = ["rama","krishna","arjuna"]
        for data in names:
            print(data)
            time.sleep(2)

    def print_num(self):
        for i in range(10):
            print(i)
            time.sleep(2)

    def sum(self):
        a = 10
        b = 20
        c = a+ b
        print(c)
        time.sleep(2)

d1 = Demo()
d1.print_name()
d1.print_num()
d1.sum()