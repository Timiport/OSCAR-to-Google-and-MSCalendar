import sys
import os
sys.path.append(os.getcwd())
from GoogleCalendarAPI import createEvent
from runner.jsonParser import jsonParser

def main():
    
    parser = jsonParser('s','s')
    courseElement, semester = parser.getCourseInformation()
    #print(courseElement)
    print(semester)
    time = courseElement['meetings'][0]['time']
    location = courseElement['meetings'][0]['location']
    weekDays = courseElement['meetings'][0]['days']
    instructor = courseElement['meetings'][0]['instructor']
    createEvent.createEvent("CS 1334", location, time, semester)
    

if __name__ == "__main__":
    main()
