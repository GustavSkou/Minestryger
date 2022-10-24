from tkinter import Button
import random as r
import settings as s
r.seed()


class Cell:
    all = []
    choosen_mines = []
    surroundings_mines = 0

    def __init__(self, x, y, is_open, is_flag, is_mine, mine_count):
        self.cell_object = self
        self.x = x
        self.y = y
        self.is_flag = False
        self.is_mine = False
        self.is_open = False
        self.mine_count = mine_count

        Cell.all.append(self)

    def create_cell(self, frame_pos, txt):
        cell = Button(
            frame_pos,
            text=txt,
            bg="gray",
            height=1,
            width=2

        )
        cell.bind("<Button-1>", self.l_click)
        cell.bind("<Button-3>", self.r_click)

        self.cell_object = cell

    def l_click(self, event):
        if not self.is_open and not self.is_flag and not self.is_mine:
            self.is_open = True
            self.cell_object.configure(
                    bg="gray",
                    text=self.mine_count,
                    fg="black"
                )
        elif self.is_mine and not self.is_flag:
            self.cell_object.configure(
                bg="black",
                text="Ø",
                fg="white"
            )

        print(repr(self))

    def r_click(self, event):
        if not self.is_open and not self.is_flag:
            self.is_flag = True
            self.cell_object.configure(
                bg="gray",
                text="F",
                fg="red"
            )
        else:
            self.is_flag = False
            self.cell_object.configure(
                bg="gray",
                text="",
                fg="white"
            )

        print(repr(self))

    @staticmethod
    def show_all_minecount():
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_object.configure(
                    bg="black",
                    text="Ø",
                    fg="white"
                )
            else:
                cell.cell_object.configure(
                    bg="gray",
                    text=cell.mine_count,
                    fg="black"
                )

    @staticmethod
    def cell_from_axis(x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                if cell.is_mine:
                    Cell.surroundings_mines = Cell.surroundings_mines + 1

    @staticmethod
    def calculate_minecount():
        for cell in Cell.all:
            x = cell.x
            y = cell.y

            print(str(x) + ", " + str(y), end=" : ")

            Cell.surroundings_mines = 0

            Cell.cell_from_axis(x - 1, y - 1)
            Cell.cell_from_axis(x - 1, y)
            Cell.cell_from_axis(x - 1, y + 1)

            Cell.cell_from_axis(x, y - 1)
            Cell.cell_from_axis(x, y + 1)

            Cell.cell_from_axis(x + 1, y - 1)
            Cell.cell_from_axis(x + 1, y)
            Cell.cell_from_axis(x + 1, y + 1)

            cell.mine_count = Cell.surroundings_mines
            print(Cell.surroundings_mines)

    @staticmethod
    def randomize():
        Cell.choosen_mines = r.sample(Cell.all, s.total_mines)
        for item in Cell.choosen_mines:
            item.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y}, {self.is_open}, {self.is_flag}, {self.is_mine}, {self.mine_count})"
