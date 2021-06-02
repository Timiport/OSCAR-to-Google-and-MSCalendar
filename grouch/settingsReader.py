from pathlib import Path
from grouch import settings
folder = Path('grouch')
settingsFile = folder / 'settings.py'

def setCourseName(courseName):
    """
    Change the subject line in settings.py to user's course subject

    Args:
        courseName (string): the name of the course
    """
    
    fil = open(settingsFile, 'r')
    fileLines = fil.readlines()
    
    fileLines[20] = f"SUBJECTS = [\'{courseName}\']\n" 
    fil = open(settingsFile, 'w')
    fil.writelines(fileLines)
    fil.close()


def isSameCourse(courseName):
    """
    Check if the courseName user enters is the same as the courseName 
    originally in the file 'settings.py'

    Args:
        courseName (string): name of the course

    Returns:
        boolean: whether the course is same or not
    """

    # fil = open(settingsFile, 'r')
    # fileLines = fil.readlines()
    # oldCourse = fileLines[22]
    # fil.close()
    oldCourse = settings.SUBJECTS[0] + " " + settings.COURSE_IDENTIFIER
   
    if (oldCourse == courseName):
        return True
    else:
        return False

def setParseLimit(limit):
    """Method that set the parse term limit in 'settings.py'

    Args:
        limit (int): semester limit of crawler
    """
    fil = open(settingsFile, 'r')
    fileLines = fil.readlines()
    fileLines[17] = f'SEMESTER_STOP = {limit}\n'
    fil = open(settingsFile, 'w')
    fil.writelines(fileLines)
    fil.close()

def setCourseIdentifier(identifier):
    """Set course identifier to allow for faster processing

    Args:
        identifier (string): course identifier. ie. 'CS 1332'
    """
    fil = open(settingsFile, 'r')
    fileLines = fil.readlines()
    fileLines[22] = f'COURSE_IDENTIFIER = \'{identifier}\'\n'
    fil = open(settingsFile, 'w')
    fil.writelines(fileLines)
    fil.close()
