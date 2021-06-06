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
    #print(semester)
    # time = courseElement['meetings'][0]['time']
    # location = courseElement['meetings'][0]['location']
    # weekDays = courseElement['meetings'][0]['days']
    # instructor = courseElement['meetings'][0]['instructor']
    #createEvent.createEvent("CS 1334", location, time, semester, weekDays)
    

if __name__ == "__main__":
    main()
