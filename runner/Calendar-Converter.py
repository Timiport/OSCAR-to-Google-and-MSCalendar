import sys
import os
sys.path.append(os.getcwd())
from tkinter import Tk
from gui.startWindows import GuiRunner

def main():   
   
    window = Tk()
    GuiRunner(window)
    
    window.mainloop()          

if __name__ == "__main__":
    main()
