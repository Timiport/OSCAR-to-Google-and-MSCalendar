import os
import sys
sys.path.append(os.getcwd())
from scrapy.crawler import CrawlerRunner, CrawlerProcess, Crawler
from grouch.spiders.oscar_spider import OscarSpider
from scrapy.utils.project import get_project_settings as Settings

def crawlCourseJson():
    try:
        open('result.json', 'w').close()
    except:
        pass


    os.system('scrapy crawl -o result.json oscar')

crawlCourseJson()
