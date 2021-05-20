import os

def crawlCourseJson():
    try:
        os.remove('result.json')
    except OSError:
        pass

    os.system('scrapy crawl -o result.json -t json oscar')

crawlCourseJson()