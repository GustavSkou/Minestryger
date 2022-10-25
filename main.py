import tkinter as tk
import settings as s
from cell import Cell

root = tk.Tk()
root.geometry(s.geo)

upper_frame = tk.Frame(
    height=s.root_height/10,
    width=s.root_witdh,
    bg="gray"
)

lower_frame = tk.Frame(
    height=(s.root_height/10)*9,
    width=s.root_witdh,
    bg="white"
)

upper_frame.place(x=0, y=0)
lower_frame.place(x=0, y=s.root_height/10)


for x in range(10):
    for y in range(10):
        c = Cell(x=x, y=y, is_flag=False, is_mine=False, is_open=False, mine_count=0)
        c.create_cell(
            frame_pos=lower_frame,
            txt=""
        )
        c.cell_object.grid(
            column=x, row=y,
        )

Cell.randomize()
Cell.calculate_minecount()
#Cell.show_all_minecount()

root.mainloop()
