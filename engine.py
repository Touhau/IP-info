import tkinter as tk
from gui import iug


class engine(iug):
    def __init__(self, window):
        super().__init__(window)



if __name__ == "__main__":
    window = tk.Tk()
    a = engine(window)
    a.mainloop()