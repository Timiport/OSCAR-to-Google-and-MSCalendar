import json


class jsonParser:
  
    def __init__(self, courseName, crn=0):
        self.courseName = courseName
        self.crn = str(crn)

    def getCourseInformation(self, semDate): 
        """ Method to return the course information for the user

        Returns:
            [type]: [description]
        """
        f = open('result.json')
        course = json.load(f)
        courseInfo = list(filter(lambda x: x["identifier"] == self.courseName
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


