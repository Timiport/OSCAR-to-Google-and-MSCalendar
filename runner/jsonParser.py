import json


class jsonParser:
  
    def __init__(self, courseName, crn):
        self.courseName = courseName
        self.crn = str(crn)

    def getCourseInformation(self): 
        """ Method aims to 

        Returns:
            [type]: [description]
        """
        f = open('result.json')
        course = json.load(f)
        courseInfo = list(filter(lambda x: x["identifier"] == "CS 1332", course))
                                 #and x["restrictions"]["Campuses"]["requirements"][0] == "Georgia Tech-Atlanta *", course))

        classList = courseInfo[0]["sections"]
        semester = courseInfo[0]["semester"]

        for element in classList:
            if element["crn"] == "90770":
                return element, semester

    # print(courseInfo[0]["crn"])
    #print(json.dumps(courseInfo, indent = 4))

