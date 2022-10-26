from tkinter import Button
import random as r
import settings as s
r.seed()


class Cell:
    all = []
    choosen_mines = []
    surroundings_mines = 0
    is_first_click = True

    def __init__(self, x, y, is_open, is_flag, is_mark, is_mine, mine_count):
        self.cell_object = self
        self.x = x
        self.y = y
        self.is_flag = False
        self.is_mark = False
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
        if Cell.is_first_click:
            Cell.is_first_click = False
            Cell.first_click(self)
        else:
            if not self.is_open and not self.is_flag and not self.is_mine:
                if self.mine_count > 0:
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

                Cell.lost()

            print(repr(self))

    def r_click(self, event):
        if not self.is_open:
            if not self.is_flag and not self.is_mark:
                self.is_flag = True
                self.cell_object.configure(
                    bg="gray",
                    text="F",
                    fg="red"
                )
            elif self.is_flag:
                self.is_flag = False
                self.is_mark = True
                self.cell_object.configure(
                    bg="gray",
                    text="?",
                    fg="white"
                )
            else:
                self.is_mark = False
                self.cell_object.configure(
                    bg="gray",
                    text="",
                    fg="white"
                )
        else:
            return

        print(repr(self))

    def first_click(self):
        Cell.randomize()
        while self.is_mine:
            for cell in Cell.all:
                cell.is_mine = False
            Cell.randomize()
            print("first mine")

        Cell.calculate_minecount()

        self.is_open = True
        self.cell_object.configure(
            bg="gray",
            text=self.mine_count,
            fg="black"
        )

    @staticmethod
    def lost():
        for cell in Cell.all:
            cell.cell_object.bind("<Button-1>")
            cell.cell_object.bind("<Button-3>")

    def auto_open(self):
        cells_to_check = []
        cells_to_check.append(self)

        surroundings_cells = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, +1], [1, -1], [1, 0], [1, 1]]

        def walk_around(cells):
            for i in cells:
                x = i.x
                y = i.y
                cells_to_check.pop(0)
                for n in range(8):
                    for cell in Cell.all:
                        if cell.x == x + surroundings_cells[n][0] and cell.y == y + surroundings_cells[n][1] and not cell.is_open:
                            cell.is_open = True
                            cell.cell_object.configure(
                                bg="gray",
                                text=cell.mine_count,
                                fg="black"
                            )
                            if cell.mine_count == 0:
                                cells_to_check.append(cell)

            if len(cells_to_check) > 0:
                walk_around(cells_to_check)
            else:
                return

        walk_around(cells_to_check)

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
            if cell.is_mine:
                pass
            else:
                x = cell.x
                y = cell.y
                Cell.surroundings_mines = 0

                print(str(x) + ", " + str(y), end=" : ")

                surroundings_cells = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
                for n in range(8):
                    Cell.cell_from_axis(x + surroundings_cells[n][0], y + surroundings_cells[n][1])

                cell.mine_count = Cell.surroundings_mines
                print(Cell.surroundings_mines)

    @staticmethod
    def randomize():
        Cell.choosen_mines = r.sample(Cell.all, s.total_mines)
        for item in Cell.choosen_mines:
            item.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y}, {self.is_open}, {self.is_flag}, {self.is_mark}, {self.is_mine}, {self.mine_count})"
