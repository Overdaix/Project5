from _cffi_backend import callback
from scrapy.item import Item, Field
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from PCMasterSpider.items import Harddisk
from scrapy.contrib.linkextractors import LinkExtractor
import datetime
from scrapy import cmdline
"""
Crawler for Azerty.nl, crawls products, for links use other crawler.

To execute run: scrapy crawl Links_Azerty -o Azerty_Links.json -t json
"""

class Products_Azerty(CrawlSpider):

    # The name is the unique identifier for this spider.
    name = 'Links_Azerty'
    allowed_domains = ["azerty.nl"]

    # These URLs are the initial requests performed by the spider.
    start_urls = [
        'http://azerty.nl/8/componenten.html'
    ]

    rules = (
        #Rule(LinkExtractor(restrict_xpaths =('//*[@id="_producten_zoek_"]/div[5]/div/ul/li/ul/li[position()=4 or position()=5 or (position()>=7 and position()<=9) or position()=11 or position()=13 or position()=14 or position()=16 or position()=17 or position()=20]/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths =('//li[@class="node open group"]/ul/li/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths =('//li[@class="info"]/a', )),callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="menu"]/ul/li/ul/li/a')),callback='parse_item',follow=True),

    )

    def parse_item(self, response):
        items = []
        item = Harddisk()

        for sel in response.xpath('//li[@class="node open group"][1]'):
            #item['Provider'] = ["Link"]
            #item['Category'] = sel.xpath("a/text()").extract()
           # item['Name'] = response.url

            link = sel.xpath("a/@href").extract()
            link.append("http://azerty.nl")
            item['Url'] = [link[1] + link[0]]

            #cmdline.execute("scrapy crawl Products_Azerty -o Azerty.json -t json".split())
            items += item['Url']
            # Finally return the scraped item.

            yield item
            #Get the sub-category links of each category
            for sub in response.xpath('//li[@class="node open group"][1]/ul/li'):
                #item['Provider'] = ["Sub-Link"]
                #item['Category'] = sel.xpath("a/text()").extract()
                #item['SubCategory'] = sub.xpath("a/text()").extract()
               # item['Provider'] = ["Sub-Category"]
               # item['Name'] = response.url
                link = sub.xpath("a/@href").extract()
                link.append("http://azerty.nl")
                item['Url'] = [link[1] + link[0]]
                yield item