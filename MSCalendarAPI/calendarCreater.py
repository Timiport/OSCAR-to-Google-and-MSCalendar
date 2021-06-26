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
        """Authenticate user and launch a sign in page

        Returns:
            bool: true if the user is already authenticated false otherwise
        """
        
        # authenticate account
        # if (account.authenticate(scopes=['calendar_all'])):
        #      print("Authenticated")

        if not self.account.is_authenticated:    
            authURL = self.connect.get_authorization_url(self.protocal.get_scopes_for(['calendar_all']))
            webbrowser.open(authURL[0], new=0)
            
            return False
        else:
            return True

    def createEvent(self, subject, location, time, semester, weekday):
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
        
        # create calendar event and set its parameters
        newEvent = calendar.new_event()
        startDate, endDate = self.getDate(semester)
        startTime = self.getTime(time[ : time.index("-")], startDate)
        endTime = self.getTime(time[time.index("-")+2:], startDate)

        newEvent.remind_before_minutes = 15
        print(startTime.isoformat())
        newEvent.subject = subject
        newEvent.location = location
        newEvent.start = startTime
        newEvent.end = endTime
        week = self.getWeek(weekday)
        dateStart = dt.datetime(int(startDate[:4]), int(startDate[4:6]), int(startDate[6:]))
        dateEnd = dt.datetime(int(endDate[:4]), int(endDate[4:6]), int(endDate[6:]))
        newEvent.recurrence.set_weekly(1, days_of_week=week, first_day_of_week=week[0], end=dateEnd, start=dateStart)
        newEvent.save()

    def isAuthenticated(self):
        return self.account.is_authenticated

    def getTime(self, time, semester):
        """Method to generate the time based on course time and semester

        Args:
            time (string): time of the course
            semester (string): semester string of the course, include year and month and date

        Returns:
            datetime object: an object used to initialize event time
        """
        if "pm" in time and "12" not in time:
            hour = int(time[:time.index(":")]) + 12
        else:
            hour = int(time[:time.index(":")])

        minute = time[time.index(":") + 1:time.index(":") + 3]
        year = semester[:4]
        month = semester[4:6]
        date = semester[6:]
        return dt.datetime(int(year), int(month), int(date), hour, int(minute))

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

    def getMonth(self, month):
        """Method to return the month in a number format

        Args:
            month (string): the month in a string format

        Returns:
            string: month in the number format
        """

        if month == 'Jan':
            return '01'
        elif month == 'May':
            return '05'
        elif month == 'Jun':
            return '06'
        elif month == 'Jul':
            return '07'
        elif month == 'Aug':
            return '08'
        elif month == 'Dec':
            return '12'
        else:
            return None

    def getDate(self, dateRange):
        start_Year = dateRange[dateRange.index(',')+2:dateRange.index(',')+6]
        end_Year = dateRange[dateRange.index(',', 12)+2:dateRange.index(',', 12)+6]
        start_Month = self.getMonth(dateRange[:3])
        end_Month = self.getMonth(dateRange[dateRange.index('-')+2:dateRange.index('-')+5])
        start_Date = dateRange[dateRange.index(',')-2:dateRange.index(',')]
        end_Date = dateRange[dateRange.index(',', 12)-2:dateRange.index(',', 12)]

        startSem = start_Year + start_Month + start_Date
        endSem = end_Year + end_Month + end_Date

        return startSem, endSem


        

