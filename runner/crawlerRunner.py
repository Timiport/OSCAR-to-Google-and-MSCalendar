import os
import sys
sys.path.append(os.getcwd())
from scrapy.crawler import CrawlerRunner
from grouch.spiders.oscar_spider import OscarSpider

def crawlCourseJson():
    try:
        open('result.json', 'w').close()
    except:
        pass


    os.system('scrapy crawl -o result.json -t json oscar')
