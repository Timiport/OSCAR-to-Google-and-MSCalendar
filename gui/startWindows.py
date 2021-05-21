import sys
import os
from tkinter import font, ttk
sys.path.append(os.getcwd())
from tkinter import *
from gui.courseDescription import getCourseList

class GuiRunner:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+300+150")
        self.root.title("OSCAR To MSCalendar Converter")
        self.root.resizable(False, False)
        self.root.iconbitmap('tech-logo.ico')
        self.courseDescription = getCourseList()

        self.queryRow()

    def queryRow(self):
        
        courseName = StringVar()
        courseName.set(self.courseDescription[0])

        courseDropDown = OptionMenu(self.root, courseName, *self.courseDescription)
        courseDropDown = ttk.Combobox(self.root, textvariable=courseName, values=self.courseDescription, 
                                        width=15, height=15, font=("Arial", 13))
        courseNumLabel = Label(self.root, text="Course Number: ", font=("Arial", 13))
        defaultText = StringVar()
        defaultText.set("Ex: 1332")
        courseNumber = Entry(self.root, width=15, font=("Arial", 13), textvariable=defaultText)
        
        def on_click_delete(event):
            event.widget.delete(0, END)
        
        courseNumber.bind("<Button-1>", on_click_delete)

        crnText = Label(self.root, text="CRN: ", font=("Arial", 13))
        optionalText = StringVar()
        optionalText.set("Optional")
        crn = Entry(self.root, width=20, font=("Arial", 13), textvariable=optionalText, fg="grey")
        crn.bind("<Button-1>", on_click_delete)

        getCourse = Button(self.root, text="Get Course", font=("Arial", 13))

        sem = StringVar()
        sem.set("fall")
        fallSemester = Radiobutton(self.root, text="Fall", variable=sem, value="fall", font=("Arial", 13))
        SpringSemester = Radiobutton(self.root, text="Spring", variable=sem, value="spring", font=("Arial", 13))
        SummerSemester = Radiobutton(self.root, text="Summer", variable=sem, value="summer", font=("Arial", 13))
        
        line = ttk.Separator(self.root, orient='horizontal')

        #Add object to windows
        courseDropDown.grid(row=0, column=0, padx=20, pady=20)
        courseNumLabel.grid(row=0,column=1)
        courseNumber.grid(row=0,column=2)
        crnText.grid(row=0, column=3, padx=(20,0))
        crn.grid(row=0, column=4)
        fallSemester.grid(row=0,column=5, padx=(100,0))
        SpringSemester.grid(row=0, column=6)
        SummerSemester.grid(row=0, column=7)
        getCourse.grid(row=0, column=8, padx=(100,20))
        line.grid(row=1, columnspan=9, sticky="ew", padx=30)
    
        

window = Tk()
GuiRunner(window)
window.mainloop()