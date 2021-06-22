import sys
import os
sys.path.append(os.getcwd())
import tkinter as tk
from PIL import Image, ImageTk
from GoogleCalendarAPI.authenticate import getCalendarService
from gui.startWindows import GuiRunner


class loginScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("400x210+500+350")
        self.root.title("Login Calendar")
        self.root.resizable(False, False)
        self.root.iconbitmap('gui/icon/tech-logo.ico')
        self.root.configure(background='grey')
        self.loginCalendar()
        
    def loginCalendar(self):

        global msPhotoImage, msImage, googleImage, googlePhotoImage
        googleImage = Image.open('gui/icon/google.jpg')
        googleImage = googleImage.resize((100, 100), Image.ANTIALIAS)
        googlePhotoImage = ImageTk.PhotoImage(googleImage)

        msImage = Image.open('gui/icon/microsoft.png')
        msImage = msImage.resize((100,100), Image.ANTIALIAS)
        msPhotoImage = ImageTk.PhotoImage(msImage)

        lowerButton = tk.Button(self.root, text= 'Microsoft Calendar', image=msPhotoImage, compound='left', font=('Arial', 13), width=400, height=90, padx=100)
        upperButton = tk.Button(self.root, text= 'Google Calendar', image=googlePhotoImage, compound='left', 
                                font=('Arial', 13), width=400, height=90, padx=100, command=self.launchGoogleCalendar)

        upperButton.pack(pady=(5,5))
        lowerButton.pack()
    
    def launchGoogleCalendar(self):
        # service = getCalendarService()
        # if service != None:
        GuiRunner(self.root)