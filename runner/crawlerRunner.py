import os
from multiprocessing import Process

def crawlCourseJson():
    try:
        os.remove('result.json')
    except OSError:
        pass

    os.system('scrapy crawl -o result.json -t json oscar')
