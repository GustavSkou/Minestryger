from tkinter import Label


class Counter:
    all = []

    def __init__(self, count, count10, count100):
        self.counter_object = self
        self.count = count
        self.count10 = count10
        self.count100 = count100

        Counter.all.append(self)

    def create_counter(self, frame_pos):
        counter = Label(
            frame_pos,
            text=str(self.count100) + str(self.count10) + str(self.count),
            font=('Arial 11')
        )

        self.counter_object = counter

    @staticmethod
    def minus():
        for counter in Counter.all:
            if counter.count != 0:
                counter.count -= 1
            else:
                if counter.count10 != 0:
                    counter.count10 -= 1
                    if counter.count10 == 0:
                        counter.count = 9
                else:
                    if counter.count100 != 0:
                        counter.count100 -= 1
                        if counter.count100 == 0:
                            counter.count = 9
                            counter.count10 = 9
                    else:
                        return

    @staticmethod
    def plus():
        for counter in Counter.all:
            counter.count += 1
            if counter.count == 10:
                counter.count = 0
                counter.count10 += 1
                if counter.count10 == 10:
                    counter.count10 = 0
                    counter.count100 += 1
    @staticmethod
    def update_counter():
        for counter in Counter.all:
            counter.counter_object.configure(
                text=str(counter.count100) + str(counter.count10) + str(counter.count),
                font=('Arial 11')
            )
