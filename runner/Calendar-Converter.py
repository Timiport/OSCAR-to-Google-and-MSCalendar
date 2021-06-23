import sys
import os
sys.path.append(os.getcwd())
from tkinter import Tk
from GoogleCalendarAPI import createEvent
from runner.jsonParser import jsonParser
from gui.startWindows import GuiRunner
from gui.loginScreen import loginScreen

def main():
    
   
    window = Tk()
    GuiRunner(window)
    
    window.mainloop()   
    
    

if __name__ == "__main__":
    main()
