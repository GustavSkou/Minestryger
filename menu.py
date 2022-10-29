import tkinter as tk
from tkinter import *

class Menu:
    def __init__(self):
        self.menu_object = self

    def create_menu_button(self, frame_pos):
        menu = tk.Button(
            frame_pos,
            text="M"
        )

        menu.bind("<Button-1>", self.left_click)
        self.menu_object = menu

    def left_click(self, event):
        clearFrame()
