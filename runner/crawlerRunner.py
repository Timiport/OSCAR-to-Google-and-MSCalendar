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


    os.system('scrapy crawl -o result.json -t json oscar')
    # try:
    #     os.remove('result.json')
    # except OSError:
    #     pass
    # process = CrawlerProcess({
    #     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    #     'FEED_FORMAT': 'json',
    #     'FEED_URI': 'result.json'
    #     })
        
    # process.crawl(OscarSpider)
    # process.start()

crawlCourseJson()
