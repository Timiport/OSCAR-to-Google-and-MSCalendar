import os

def crawlCourseJson():
    os.system('scrapy crawl -o result.json -t json oscar')

crawlCourseJson()