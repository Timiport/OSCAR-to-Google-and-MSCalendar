from datetime import date, datetime
import sys
import os
from types import ModuleType
from webbrowser import get
sys.path.append(os.getcwd())
from GoogleCalendarAPI.authenticate import getCalendarService

def createEvent(subject, location, time, semester, weekDays):
    """Method to create recurring event in Google Calendar

    Args:
        subject (string): subject of the event
        location (string): location of the event
        time (string): time of the event
        semester (string): date range of the event
        weekDays (string): weekdays the event occurs
    """
    if time == "None":
        raise ValueError("Can not create event with insufficient course information")

    service = getCalendarService()
    startDate, endDate = getDate(semester)
    startTime = getTime(time[ : time.index("-")], startDate)
    endTime = getTime(time[time.index("-")+2:], startDate)
    weeksList = getWeek(weekDays)
    weeks = ','.join(weeksList)
    event = {
        'summary': subject,
        'location': location,
        'start': {
            'dateTime': startTime.isoformat(),
            'timeZone': "America/New_York",
        },
        'end': {
            'dateTime': endTime.isoformat(),
            'timeZone': "America/New_York",
        },
        'recurrence': [
            'RRULE:FREQ=WEEKLY;UNTIL=' + endDate + ';BYDAY=' + str(weeks)
        ],
    }
    #print('RRULE:FREQ=WEEKLY;UNTIL=20211010;BYDATE=' + str(weeks))
    event = service.events().insert(calendarId='primary', body=event).execute()

def getDate(dateRange):
    start_Year = dateRange[dateRange.index(',')+2:dateRange.index(',')+6]
    end_Year = dateRange[dateRange.index(',', 12)+2:dateRange.index(',', 12)+6]
    start_Month = getMonth(dateRange[:3])
    end_Month = getMonth(dateRange[dateRange.index('-')+2:dateRange.index('-')+5])
    start_Date = dateRange[dateRange.index(',')-2:dateRange.index(',')]
    end_Date = dateRange[dateRange.index(',', 12)-2:dateRange.index(',', 12)]

    startSem = start_Year + start_Month + start_Date
    endSem = end_Year + end_Month + end_Date

    return startSem, endSem


def getTime(time, semester):
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
    return datetime(int(year), int(month), int(date), hour, int(minute))


def getWeek(weekdays):
    weeks = []
    for element in weekdays:
        if element == "M":
            weeks.append("MO")
        elif element == "T":
            weeks.append("TU")
        elif element == "W":
            weeks.append("WE")
        elif element == "R":
            weeks.append("TH")
        else:
            weeks.append("FR")
    return weeks
    
def getMonth(month):
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
