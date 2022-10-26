from cell import Cell
from tkinter import Button


class Restart:
    def __init__(self):
        self.restart_object = self

    def create_restart_button(self, frame_pos):
        restart = Button(
            frame_pos,
            text="Restart",

        )
        restart.bind("<Button-1>", self.click)
        self.restart_object = restart

    def click(self, event):
        Cell.clear_board()
        Cell.randomize()
        Cell.calculate_minecount()
        #Cell.show_all_minecount()
        print("restart")