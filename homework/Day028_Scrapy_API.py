import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1581178413.A.9BE.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1581178416.A.14A.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1581178419.A.BA1.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1581178466.A.EBA.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1581178478.A.FB0.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler', start_urls=target_urls, filename='gossiping.json')
    process.start()

if __name__ == '__main__':
    main()
