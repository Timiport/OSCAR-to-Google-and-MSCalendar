from inspect import Traceback
import sys
import os
sys.path.append(os.getcwd())
import time
import logging
import traceback
from multiprocessing import Process
from threading import Thread, Timer
from tkinter import font, ttk, messagebox
from string import ascii_uppercase
import subprocess

from GoogleCalendarAPI.authenticate import getCalendarService
from GoogleCalendarAPI.createEvent import createEvent
from MSCalendarAPI.calendarCreater import MSCalendar
import grouch.spiders.oscar_spider as osp
from multiprocessing import Process
from tkinter import *
from gui.courseDescription import getCourseList

from runner.jsonParser import jsonParser
from grouch import settings
from grouch.settingsReader import *
from PIL import Image, ImageTk

class GuiRunner:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x730+300+150")
        self.root.title("OSCAR To GMSCalendar Converter")
        self.root.resizable(False, False)
        self.root.iconbitmap('gui/icon/tech-logo.ico')
        self.courseDescription = getCourseList()
        self.treeTable = None
        self.bottomLeftLabel = Label(self.root, text='', font=('Arial', 13))
        self.GoogleCalendarService = None
        self.MSCalendarService = None
        self.isMCalendarService = False
        
        self.loginWindow()
        self.queryRow()
        self.table()

    def queryRow(self):

        # Set each element in gui
        initFrame = LabelFrame(self.root, text="Course Information", width=200)
        courseName = StringVar()
        courseName.set(self.courseDescription[0])

        # courseDropDown = OptionMenu(initFrame, courseName, *self.courseDescription)
        courseDropDown = ttk.Combobox(initFrame, textvariable=courseName, values=self.courseDescription, 
                                        width=20, height=15, font=("Arial", 13))
        # self.courseDropDown.bind("<Key>", self.findCourseInDropDown)
        def on_click_delete(event):
            event.widget.delete(0, END)

        # courseDropDown = AutocompleteCombobox(initFrame)
        # courseDropDown.set_completion_list(self.courseDescription)
        # courseDropDown.bind("<Button-1>", on_click_delete)

        courseNumLabel = Label(initFrame, text="Course Number: ", font=("Arial", 13))
        defaultText = StringVar()
        defaultText.set("Ex: 1332")
        courseNumber = Entry(initFrame, width=15, font=("Arial", 13), textvariable=defaultText)     
              
        courseNumber.bind("<Button-1>", on_click_delete)

        optionalText = StringVar()
        optionalText.set("Optional")
        crn = Entry(initFrame, width=15, font=("Arial", 13), textvariable=optionalText, fg="grey")
        crn.bind("<Button-1>", on_click_delete)

        sem = StringVar()
        sem.set("08")
        fallSemester = Radiobutton(initFrame, text="Fall", variable=sem, value="08", font=("Arial", 13), command=lambda: sem.set("08"))
        SpringSemester = Radiobutton(initFrame, text="Spring", variable=sem, value="02", font=("Arial", 13), command=lambda: sem.set("02"))
        SummerSemester = Radiobutton(initFrame, text="Summer", variable=sem, value="05", font=("Arial", 13), command=lambda: sem.set("05"))
        
        progress = ttk.Progressbar(self.root, orient=HORIZONTAL, length=300, mode='indeterminate')
        progress['maximum'] = 100

        getCourse = Button(self.root, text="Get Course", font=("Arial", 13), 
                    command=lambda: Thread(target=self.fetchCourse, args=(courseName.get(), sem.get(), courseNumber.get(), progress, getCourse)).start())
        #command=lambda: self.fetchCourse(courseName.get(), crn.get(), sem.get(), courseNumber.get(), progress)
        line1 = ttk.Separator(self.root, orient='horizontal')

        convert = Button(self.root, text="Convert to Calendar", font=("Arial", 13), bg="silver", command=self.selectToEvent)

        line2 = ttk.Separator(self.root, orient='horizontal') 

        #Add object to windows
        initFrame.grid(row=0, column=0, padx=(20,0), pady=20)
        courseDropDown.grid(row=0, column=0, padx=20, pady=20)
        courseNumLabel.grid(row=0,column=1, padx=(50,0))
        courseNumber.grid(row=0,column=2)
 
        fallSemester.grid(row=0,column=5, padx=(50,0))
        SpringSemester.grid(row=0, column=6)
        SummerSemester.grid(row=0, column=7, padx=(0, 20))
        getCourse.grid(row=0, column=1, padx=(5,20))
        line1.grid(row=1, columnspan=3, sticky="ew", padx=30)
        convert.grid(row=3, columnspan=3)
        line2.grid(row=4, columnspan=3, sticky="ew", padx=30, pady=(20,10))
        self.bottomLeftLabel.grid(row=5, column=0, sticky='w', padx=30)
        progress.grid(row=5, columnspan=3, sticky='e', padx=30)
        

    def table(self):
        style = ttk.Style()
        style.theme_use('default')

        style.configure("Treeview", 
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=45,
                    fielldbackground="#D3D3D3")
        
        style.map('Treeview', 
                    background=[('selected', "#347083")])
        treeFrame = Frame(self.root)
        treeFrame.grid(row=2, columnspan=3, pady=20, padx=40)

        treeScrollBar = Scrollbar(treeFrame)
        treeScrollBar.pack(side=RIGHT, fill=Y)

        #Create Tree view
        self.treeTable = ttk.Treeview(treeFrame, yscrollcommand=treeScrollBar.set, selectmode="extended")
        self.treeTable.pack()

        treeScrollBar.config(command=self.treeTable.yview)

        #Define Columns
        self.treeTable['columns'] = ("Section ID", "CRN", "Professor", "Dates", "Weeks", "Start Time", "Location")
        self.treeTable.column("#0", width=0, stretch=NO)
        self.treeTable.column("Section ID", anchor=CENTER, width=100)
        self.treeTable.column("CRN", anchor=CENTER, width=100)
        self.treeTable.column("Professor", anchor=CENTER, width=200)
        self.treeTable.column("Dates", anchor=CENTER, width=150)
        self.treeTable.column("Weeks", anchor=CENTER, width=100)
        self.treeTable.column("Start Time", anchor=CENTER, width=150)
        self.treeTable.column("Location", anchor=CENTER, width=200)

        # Set headings
        self.treeTable.heading("#0", text="", anchor=W)
        self.treeTable.heading("Section ID", text="Section ID", anchor=CENTER)
        self.treeTable.heading("CRN", text="CRN", anchor=CENTER)
        self.treeTable.heading("Professor", text="Professor", anchor=CENTER)
        self.treeTable.heading("Dates", text="Dates", anchor=CENTER)
        self.treeTable.heading("Weeks", text="Weeks", anchor=CENTER)
        self.treeTable.heading("Start Time", text="Start Time", anchor=CENTER)
        self.treeTable.heading("Location", text="Location", anchor=CENTER)

        # Create Rows
        self.treeTable.tag_configure('oddrow', background="white")
        self.treeTable.tag_configure('evenrow', background='silver')

    def findCourseInDropDown(self, event):
        keyPress = event.char.upper()

        if keyPress in ascii_uppercase:
            for index, course in enumerate(self.courseDescription):
                if course[0] >= keyPress:
                    self.courseDropDown.current(index)
                    break


    def fillTable(self, courseList):
        """Fill the treeview table in the gui

        Args:
            courseList (list): the list of course informations
        """
        # clear old table content
        self.treeTable.delete(*self.treeTable.get_children())
        
        # Fill table
        count=0
        for course in courseList:
            for sections in course:
                meet = sections['meetings'][0]
                if count%2 == 0:
                    self.treeTable.insert(parent='', index='end', iid=count, text='', 
                                    value=(sections['section_id'], sections['crn'], ' ,'.join(meet['instructor']), 
                                            meet['dateRange'], meet['days'], meet['time'], meet['location']), tags=('evenrow',))
                else:
                    self.treeTable.insert(parent='', index='end', iid=count, text='', 
                                    value=(sections['section_id'], sections['crn'], ' ,'.join(meet['instructor']), 
                                            meet['dateRange'], meet['days'], meet['time'], meet['location']), tags=('oddrow',))
                count+=1

    def selectToEvent(self):
        # Grab selected numbers
        selected = self.treeTable.focus()
        # Grab selected values
        values = self.treeTable.item(selected, 'values')

        #If nothing is selected
        if len(values) == 0:
            messagebox.showerror("Error", "No course selected")
            return
        # pass everything to create event
        courseSubject = getCourseName()
        
        logging.basicConfig(filename='log.txt', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
        
        try:
            if (self.isMCalendarService):
                self.MSCalendarService.createEvent(courseSubject, values[6], values[5], values[3], values[4])
            else:
                createEvent(courseSubject, values[6], values[5], values[3], values[4])
        except Exception as e:
            messagebox.showinfo('Status', 'Error, please look into log.txt file')
            logging.error(traceback.format_exc())
            return

        messagebox.showinfo('Status', 'Done, course added to calendar')
        

    def fetchCourse(self, courseName, semDate, courseNumber, progress, getCourseButton):
        # crawlCourseJson()
        self.bottomLeftLabel.config(text='Fetching Course Information ...')
        
        Stop_Thread = False
        progressThread = Thread(target=self.bar, args=(progress, lambda: Stop_Thread))
        progressThread.daemon = True
        progressThread.start()

        # set settings
        # if semDate == '05':
        #     setParseLimit(2)
        # else:
        #     setParseLimit(2)
        courseIndetifier = courseName[:courseName.index(":")] + " " + courseNumber        
        setCourseName(courseName[:courseName.index(":")])      
        setCourseIdentifier(courseNumber)
    
        crawlerThread = Thread(target=self.crawl_course_json)
             
        getCourseButton.config(state='disabled')   
            
        crawlerThread.start() 
        crawlerThread.join()
        

        getCourseButton.config(state='normal')
        Stop_Thread = True
        progressThread.join()
        
        self.bottomLeftLabel.config(text='')
        
        # Fill table with the course
        
        parser = jsonParser(courseIndetifier)
        
        
        try:
            courseElement = parser.getCourseInformation(semDate)
        except:
            messagebox.showerror("Error", "No course match the information you entered")
            return
            
        self.fillTable(courseElement)
        #self.treeTable.update()

    def bar(self, progress, stop):
        """Method that moves the progress bar and finishes when scrapy finished crawling courses

        Args:
            progress (ProgressBar): an object of progress bar
            stop (boolean): whether progress bar should be stopped. i.e. crawler has finished
        """
        while True:
        
            for i in range(100):
                progress['value']+=1
                self.root.update_idletasks()
                time.sleep(0.2)
                if stop():
                    break
                
            for i in range(100):
                progress['value']-=1
                self.root.update_idletasks()
                time.sleep(0.2)
                if stop():
                    break
            if stop():
                progress['value'] = 0
                break
    
    def loginWindow(self):
        login_Window = Toplevel(self.root)
        login_Window.geometry("400x210+500+350")
        login_Window.title("Login Calendar")
        login_Window.resizable(False, False)
        login_Window.iconbitmap('gui/icon/tech-logo.ico')
        login_Window.configure(background='silver')
        self.loginCalendar(login_Window)

    def loginCalendar(self, window):

        global msPhotoImage, msImage, googleImage, googlePhotoImage
        googleImage = Image.open('gui/icon/google.png')
        googleImage = googleImage.resize((100, 100), Image.ANTIALIAS)
        googlePhotoImage = ImageTk.PhotoImage(googleImage)

        msImage = Image.open('gui/icon/microsoft.png')
        msImage = msImage.resize((100,100), Image.ANTIALIAS)
        msPhotoImage = ImageTk.PhotoImage(msImage)

        upperButton = Button(window, text= 'Google Calendar', image=googlePhotoImage, compound='left', 
                                font=('Arial', 13), width=400, height=90, padx=100, command=lambda: self.launchGoogleCalendar(window))

        lowerButton = Button(window, text= 'Microsoft Calendar', image=msPhotoImage, compound='left', 
                                font=('Arial', 13), width=400, height=90, padx=100, command=lambda: self.launchMSCalendar(window))


        upperButton.pack(pady=(5,5), padx=5)
        lowerButton.pack(padx=5)
    
    def launchGoogleCalendar(self, topWindow):
        self.isMCalendarService = False
        
        self.GoogleCalendarService = getCalendarService()
        topWindow.destroy()
        if self.GoogleCalendarService != None:
            messagebox.showinfo('Status', "Log in Successful.")
        else:
            self.restartWindow()

    def launchMSCalendar(self, topWindow):
        """Method to launch login screen in browser for Microsoft calendar

        Args:
            topWindow (TopLevel): the previous window that will trigger this method
        """

        self.MSCalendarService = MSCalendar()
        self.isMCalendarService = True
        topWindow.destroy()
        if (self.MSCalendarService.userAuthentication()):
            messagebox.showinfo('Status', "Log in Successful.")
        else:
            # Create url window
            auth_Window = Toplevel()
            auth_Window.geometry("500x70+500+350")
            auth_Window.title("Authorization URL")
            auth_Window.resizable(False, False)
            auth_Window.iconbitmap('gui/icon/tech-logo.ico')

            text = Label(auth_Window, text="Please paste the auto generated url here after you logged in", font=("Arial", 13))
            auth_URL = StringVar()
            auth_Entry = Entry(auth_Window, textvariable=auth_URL, width=45, font=("Arial", 13))
            verifyButton = Button(auth_Window, text='Verify', font=("Arial", 13), command=lambda: verify(auth_URL.get()))

            text.grid(row=0, columnspan=2, sticky='w', pady=(5,0), padx=10)
            auth_Entry.grid(row=1, column=0, padx=5, pady=5)
            verifyButton.grid(row=1, column=1, padx=5)
            def verify(verifiedURL):
                self.MSCalendarService.connect.request_token(verifiedURL)
                auth_Window.destroy()
                if self.MSCalendarService.account.is_authenticated:
                    messagebox.showinfo('Status', 'Log in Succeessful')
                else:
                    self.restartWindow()
            # print(self.connect.request_token(authURl))

    def restartWindow(self):
        """Method that will prompt up failure note and restart login process
        """
        restart_window = Toplevel()
        restart_window.geometry("200x80+500+350")
        restart_window.title("Status")
        restart_window.resizable(False, False)
        restart_window.iconbitmap('gui/icon/tech-logo.ico')

        def restart():
            self.loginWindow()
            restart_window.destroy()
        
        message = Label(restart_window, text='Log in Unccessful', font=('Arial', 13))
        button = Button(restart_window, text='OK', font=("Arial", 13), command=restart)

        message.pack(pady=(5,10))
        button.pack(pady=(0,5))

    def crawl_course_json(self):
        subprocess.call(['crawlerRunner.exe'])

        