# button that resizes dynamically

from tkinter import ttk
from tkinter import Button


class SmartButton(Button):

    def __init__(self, frame: ttk.Frame, function, pos: tuple, span=(1,1), **kwargs):
        super().__init__(frame, command=function, bd=0, **kwargs)
        self.gridsetup(pos, span)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
    
    def gridsetup(self, pos, span):
        self.grid(
            row=pos[0], 
            column=pos[1],
            rowspan=span[0],
            columnspan=span[1],
            padx=5,
            pady=5,
            sticky='WENS'
        )