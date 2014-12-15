__author__ = 'Dean'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from PCMasterSpider.items import AlternateItems
class Alternate(BaseSpider):
    print("Starting to collect urls...")
    name = "Tweakers" # Name of the spider, to be used when crawling
    allowed_domains = ["tweakers.net"] # Where the spider is allowed to go
    start_urls = [
        "http://tweakers.net/pricewatch/394885/intel-core-i7-4790k-boxed/specificaties/"
    ]
    #scrapy crawl metacritic -o Computerstore.json -t json
    i = 0
    def parse(self, response):
        i = 0
        print("test1")
        hxs = HtmlXPathSelector(response) # The XPath selector
        # sites = hxs.select('//li[contains(@class, "contentArea")]/div[@class="contentArea"]')
        sites = hxs.select('//table[contains(@class, "listing useVisitedState")]')
        #sites = hxs.select('//div[contains(@class, "contentArea")]/div[@id, "layout"] ]')
        items = []
#itemprop="url"
        for site in sites:
            i += 1
            item = AlternateItems()
            item['title'] = site.select('//td[@class="itemname"]/text()').extract()
            item['link'] = site.select('//a[@itemprop="url"]/a/@href').extract()
            item['cscore'] = site.select('//div[@class="basic_stat product_score brief_metascore"]/div/div/span[contains(@class, "data metascore score")]/text()').extract()
            item['uscore'] = site.select('//div[@class="more_stats condensed_stats"]/ul/li/span[contains(@class, "data textscore textscore")]/text()').extract()
            item['date'] = site.select('//div[@class="more_stats condensed_stats"]/ul/li/span[@class="data"]/text()').extract()

            items.append(item)
        return items

    print("Aantal gevonden resultaten: ")
    print(i)