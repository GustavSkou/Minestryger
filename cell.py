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
            if self.mine_count != 0:
                self.is_open = True
                self.cell_object.configure(
                        bg="gray",
                        text=self.mine_count,
                        fg="black"
                    )
            else:
                self.is_open = True
                self.cell_object.configure(
                    bg="gray",
                    text=self.mine_count,
                    fg="black"
                )
                Cell.auto_open(self)

        elif self.is_mine and not self.is_flag:
            self.is_open = True
            self.cell_object.configure(
                bg="black",
                text="Ø",
                fg="white"
            )

        print(repr(self))

    def r_click(self, event):
        if not self.is_open:
            if not self.is_flag :
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
        else:
            return

        print(repr(self))

    def auto_open(self):
        x = self.x
        y = self.y

        cell_to_check = []
        cells_to_check = []

        surroundings_cells = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, +1], [1, -1], [1, 0], [1, 1]]
        def open_surrounding_cells(x, y):
            for n in range(8):
                for cell in Cell.all:
                    if cell.x == x + surroundings_cells[n][0] and cell.y == y + surroundings_cells[n][1]:
                        if cell.mine_count == 0:
                            cell.cell_object.configure(
                                bg="gray",
                                text=self.mine_count,
                                fg="black"
                            )
                            cell_to_check.append(cell.x)
                            cell_to_check.append(cell.y)
                            cells_to_check.append(cell_to_check)
                            cell_to_check.clear()

        open_surrounding_cells(x, y)

    @staticmethod
    def show_all_minecount():
        for cell in Cell.all:
            cell.is_open = True
            if cell.is_mine:
                cell.cell_object.configure(
                    bg="black",
                    text="Ø",
                    fg="white"
                )
            else:
                cell.is_mine = True
                cell.cell_object.configure(
                    bg="gray",
                    text=cell.mine_count,
                    fg="black"
                )

    @staticmethod
    def cell_from_axis(x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @staticmethod
    def calculate_minecount():
        for cell in Cell.all:
            x = cell.x
            y = cell.y
            Cell.surroundings_mines = 0

            print(str(x) + ", " + str(y), end=" : ")

            surroundings_cells = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, +1], [1, -1], [1, 0], [1, 1] ]
            for n in range(8):
                Cell.cell_from_axis(x + surroundings_cells[n][0], y + surroundings_cells[n][1])
                if cell.is_mine:
                    Cell.surroundings_mines = Cell.surroundings_mines + 1

            cell.mine_count = Cell.surroundings_mines
            print(Cell.surroundings_mines)

    @staticmethod
    def randomize():
        Cell.choosen_mines = r.sample(Cell.all, s.total_mines)
        for item in Cell.choosen_mines:
            item.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y}, {self.is_open}, {self.is_flag}, {self.is_mine}, {self.mine_count})"

