from tkinter import *

class GuiRunner:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1280x720+300+150")
        self.window.title("OSCAR To MSCalendar Converter")
        self.window.resizable(False, False)
        

window = Tk()
GuiRunner(window)
window.mainloop()