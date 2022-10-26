import tkinter as tk
import settings as s
from cell import Cell
from restart import Restart

root = tk.Tk()
root.geometry(s.geo)

upper_frame = tk.Frame(
    height=s.root_height/7,
    width=s.root_witdh,
    bg="gray"
)

lower_frame = tk.Frame(
    height=(s.root_height/7)*6,
    width=s.root_witdh,
    bg="white"
)

upper_frame.place(x=0, y=0)
lower_frame.place(x=0, y=s.root_height/7)


for x in range(10):
    for y in range(10):
        c = Cell(x=x, y=y, is_flag=False, is_mark=False, is_mine=False, is_open=False, mine_count=0)
        c.create_cell(
            frame_pos=lower_frame,
            txt=""
        )
        c.cell_object.grid(
            column=x, row=y,
        )

r = Restart()
r.create_restart_button(
    frame_pos=upper_frame
)
r.restart_object.place(
    x=s.root_witdh/2, y=(s.root_height/7)/2, anchor= "center"
)

root.mainloop()
