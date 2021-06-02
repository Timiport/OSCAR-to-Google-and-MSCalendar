from datetime import datetime
import sys
import os
sys.path.append(os.getcwd())
from GoogleCalendarAPI.authenticate import getCalendarService

def createEvent(subject, location, time, semester, weekDays):

    service = getCalendarService()
    startTime = getTime(time[ : time.index("-")], semester)
    endTime = getTime(time[time.index("-")+2:], semester)
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
            'RRULE:FREQ=WEEKLY;UNTIL=20211010;BYDAY=' + str(weeks)
        ],
    }
    #print('RRULE:FREQ=WEEKLY;UNTIL=20211010;BYDATE=' + str(weeks))
    event = service.events().insert(calendarId='primary', body=event).execute()

def getTime(time, semester):
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
    return datetime(int(year), int(month), 15, hour, int(minute))

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
    