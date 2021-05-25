from pathlib import Path

folder = Path('grouch')
settingsFile = folder / 'settings.py'

def setCourseName(courseName):
        fil = open(settingsFile, 'r')
        fileLines = fil.readlines()
        
        fileLines[20] = f"SUBJECTS = [\'{courseName}\']\n" 
        print(fileLines[20])
        fil = open(settingsFile, 'w')
        fil.writelines(fileLines)
        fil.close()


def isSameCourse(courseName):
    fil = open(settingsFile, 'r')
    fileLines = fil.readlines()
    oldCourse = fileLines[20][fileLines[20].index("'")+1: len(fileLines[20])-3]
    
    if (oldCourse == courseName):
        return True
    else:
        return False