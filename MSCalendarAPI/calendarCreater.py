from re import sub
from O365.connection import MSGraphProtocol, Protocol
from O365 import Account, account
from O365 import Connection
from O365 import calendar
import webbrowser
import datetime as dt

class MSCalendar:

    def __init__(self):
        """
        Initialize Microsoft 365's account details
        """
        credentials = ('68769906-610b-4c87-9cf2-b9d76168f5f8', 'mjfF2PnH~c2u8j9klD--71E11Y-uA0oRgG')
        self.account = Account(credentials)
        self.connect = Connection(credentials)
        self.protocal = MSGraphProtocol()

    def userAuthentication(self):
        
        # authenticate account
        # if (account.authenticate(scopes=['calendar_all'])):
        #      print("Authenticated")

        if not self.account.is_authenticated:    
            authURL = self.connect.get_authorization_url(self.protocal.get_scopes_for(['calendar_all']))
            webbrowser.open(authURL[0], new=1)
            authrized = input("Authorization URL: ")
            print(self.connect.request_token(authrized))

    def createEvent(self, subject, location, semester, time, weekday, reminderTime = 0):
        """
        Method to create event in MS Calendar

        Args:
            subject (string): description of the event
            location (string): location of the course
            semester (string): string of the semester, include year and month
            time (string): time span of the course (ex: 1:00 pm - 2:00 pm)
            weekday (string): string describing the which weekday the course occurs (ex: MWF)
            reminderTime (int): how long to remind user the event, default is disabled
        """
        schedule = self.account.schedule()
        calendar = schedule.get_default_calendar()
        print(calendar.owner)
        # create calendar event and set its parameters
        newEvent = calendar.new_event()
        newEvent.subject = "CS 1334"
        newEvent.start = dt.datetime(2021, 5, 22, 15, 45)
        list = calendar.get_events(limit=15,include_recurring=False)
        for i in list:
            print(i)
        # newEvent.location = "US"
        # newEvent.recurrence.set_daily(1, end=dt.datetime(2021, 5, 29))
        # newEvent.remind_before_minutes = 15

        # newEvent.subject = subject
        # newEvent.location = location
        # newEvent.start = self.getTime(time[ : time.index("-")], semester)
        # newEvent.end = self.getTime(time[time.index("-") + 2:], semester)
        # week = self.getWeek(weekday)
        # if not reminderTime == 0:
        #     newEvent.remind_before_minutes = reminderTime

        # newEvent.recurrence.set_weekly(len(weekday), days_of_week=week[0], first_day_of_week=week, end=dt.datetime(int(semester[:4]), 10, 10))
        print(newEvent.save())

    def getTime(self, time, semester):
        """Method to generate the time based on course time and semester

        Args:
            time (string): time of the course
            semester (string): semester string of the course, include year and month

        Returns:
            datetime object: an object used to initialize event time
        """
        if "pm" in time:
            hour = int(time[:time.index(":")]) + 12
        else:
            hour = int(time[:time.index(":")])
        
        minute = time[time.index(":") + 1:time.index(":") + 3]
        year = semester[:4]
        month = semester[4:]
        return dt.datetime(int(year), int(month), 15, hour, int(minute))

    def getWeek(self, weekdays):
        weeks = []
        for element in weekdays:
            if element == "M":
                weeks.append("Monday")
            elif element == "T":
                weeks.append("Tuesday")
            elif element == "W":
                weeks.append("Wednesday")
            elif element == "R":
                weeks.append("Thursday")
            else:
                weeks.append("Friday")
        return weeks



        

