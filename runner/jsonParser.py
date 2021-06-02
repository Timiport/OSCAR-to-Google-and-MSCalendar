import json


class jsonParser:
  
    def __init__(self, courseNum):
        self.courseNumber = courseNum

    def getCourseInformation(self, semDate): 
        """Return Course Information that user requests

        Args:
            semDate (string): which semester of the course, 
                               should be '08', '05', '02'

        Raises:
            ValueError: [error when user enters incorrect course information that didn't match any course in the database]

        Returns:
            [string, string]: [a tuple: the list of class sections which all the information and the semester of the class]
        """
        
        f = open('result.json')
        course = json.load(f)
        courseInfo = list(filter(lambda x: semDate == x['semester'][4:] , course))
        # allClassInfo = list(filter(lambda x: self.courseNumber[0] in x["identifier"], course))
        
        if len(courseInfo) == 0:
            raise ValueError("No information is available")

        classList = []
        for course in courseInfo:
            classList.append(course['sections'])
        # classList = courseInfo[0]["sections"]
        # If user input the wrong information, it will display all possible options for user to choose
        # allClassList = allClassInfo[0]["sections"]
        #semester = courseInfo[0]["semester"]
        
        return classList

    # print(courseInfo[0]["crn"])
    #print(json.dumps(courseInfo, indent = 4))


