import json


class jsonParser:
  
    def __init__(self, courseNum, crn=0):
        self.courseNumber = courseNum
        self.crn = str(crn)

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
        courseInfo = list(filter(lambda x: x["identifier"] == self.courseNumber
                                 and semDate in x['semester'] , course))
        
        if len(courseInfo) == 0:
            raise ValueError("No information is available")

        classList = courseInfo[0]["sections"]
        semester = courseInfo[0]["semester"]

        if not self.crn == 0:
            for element in classList:
                if element["crn"] == self.crn:
                    return element, semester
                
            return classList, semester
        else:
            return classList, semester

    # print(courseInfo[0]["crn"])
    #print(json.dumps(courseInfo, indent = 4))


