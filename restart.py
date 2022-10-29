from cell import Cell
from tkinter import Button
from flag_counter import Counter


class Restart:
    def __init__(self):
        self.restart_object = self

    def create_restart_button(self, frame_pos):
        restart = Button(
            frame_pos,
            text="Restart",

        )
        restart.bind("<Button-1>", Restart.click)
        self.restart_object = restart

    @staticmethod
    def click(event):
        Cell.reset()
        Counter.reset_count()
        Counter.update_counter()
        #Cell.show_all_minecount()
