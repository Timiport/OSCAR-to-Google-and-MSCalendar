import os
from multiprocessing import Process

def crawlCourseJson():
    try:
        open('result.json', 'w').close()
    except:
        pass


    os.system('scrapy crawl -o result.json -t json oscar')

