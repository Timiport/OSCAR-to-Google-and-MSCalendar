import sys
import os
sys.path.append(os.getcwd())
from MSCalendarAPI.calendarCreater import MSCalendar
from runner.jsonParser import jsonParser

def main():
    calendar = MSCalendar()
    calendar.userAuthentication()

    parser = jsonParser('s','s')
    courseElement, semester = parser.getCourseInformation()
    #print(courseElement)
    print(semester)
    time = courseElement['meetings'][0]['time']
    location = courseElement['meetings'][0]['location']
    weekDays = courseElement['meetings'][0]['days']
    instructor = courseElement['meetings'][0]['instructor']

    print (time[ : time.index("-")])
    print (time[time.index("-") + 2: ])
    calendar.createEvent('CS 1332', location, semester, time, weekDays)

if __name__ == "__main__":
    main()
