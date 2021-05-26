from pathlib import Path

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
    print(fileLines[20])
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

    fil = open(settingsFile, 'r')
    fileLines = fil.readlines()
    oldCourse = fileLines[20][fileLines[20].index("'")+1: len(fileLines[20])-3]
    
    if (oldCourse == courseName):
        return True
    else:
        return False