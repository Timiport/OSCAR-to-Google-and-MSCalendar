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
    # process = CrawlerRunner({
    #     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    #     'FEED_FORMAT': 'json',
    #     'FEED_URI': 'result.json'
    #     })
    # process.crawl(OscarSpider)
    # process.start()

    

#crawlCourseJson()
