import sys
import os
sys.path.append(os.getcwd())
from tkinter import Tk
from GoogleCalendarAPI import createEvent
from runner.jsonParser import jsonParser
from gui.startWindows import GuiRunner
from gui.loginScreen import loginScreen

def main():
    
    # parser = jsonParser('s','s')
    # courseElement, semester = parser.getCourseInformation("08")
    #print(courseElement)
    window = Tk()
    GuiRunner(window)
    # gui = GuiRunner(window)
    # gui.fillTable(courseElement)
    window.mainloop()   
    
    

if __name__ == "__main__":
    main()
