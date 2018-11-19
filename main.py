from icrawler.builtin import GoogleImageCrawler
import sys

args = sys.argv

google_crawler = GoogleImageCrawler(storage={'root_dir': 'imgs'})
google_crawler.crawl(keyword = args[1], max_num = 100)
