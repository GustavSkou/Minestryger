from tkinter import Label

class MineCounter:
    def __init__(self, count, count10, count100):
        self.counter_object = self
        self.count = count
        self.count10 = count10
        self.count100 = count100

    def create_counter(self, frame_pos):
        counter = Label(
            frame_pos,
            text=str(self.count) + str(self.count10) + str(self.count100),
            font = ('Arial 11')
        )
        self.counter_object = counter
