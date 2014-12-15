from scrapy.item import Item, Field
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from PCMasterSpider.items import Harddisk
from scrapy.contrib.linkextractors import LinkExtractor
import datetime

"""
Crawler for Azerty.nl, crawls products, for links use other crawler.

To execute run: scrapy crawl Products_Links_Azerty -o Azerty.json -t json
"""

class Products_Azerty(CrawlSpider):

    # The name is the unique identifier for this spider.
    name = 'Products_Links_Azerty'
    allowed_domains = ["azerty.nl"]

    # These URLs are the initial requests performed by the spider.
    start_urls = [
        "http://azerty.nl/8-5888/so-dimm-ddr3.html",

    ]

    rules = (
        #Rule(LinkExtractor(restrict_xpaths =('//*[@id="_producten_zoek_"]/div[5]/div/ul/li/ul/li[position()=4 or position()=5 or (position()>=7 and position()<=9) or position()=11 or position()=13 or position()=14 or position()=16 or position()=17 or position()=20]/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths =('//li[@class="node open group"]/ul/li/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths =('//li[@class="info"]/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//div[@class="menu"]/ul/li/ul/li/a')),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//div[@class="menu"]/ul/li/ul/li/ul/li/ul/li/a')),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//div[@id="_producten_zoek"]/div/div/a[@class="titel"]')),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//td[@class="product"]/a')),callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="knop_volgende"]')),callback='parse_item',follow=True),
    )


    def parse_item(self, response):
        """
                "http://azerty.nl/8/componenten.html",
        "http://azerty.nl/8-910/processoren.html" ,
        "http://azerty.nl/8-1600/amd.html" ,
        "http://azerty.nl/8-674/voedingen.html",
        "http://azerty.nl/8-1988/ssd-s.html",
        for sel in response.xpath('//td[@class="product"]'):
            #for sel in response.xpath('//div[@id="artikel-informatie"]'):

            # Define product type TODO: make dynamic (Different components).
            item = Harddisk()

            item['Provider'] = "azerty.nl"
            now = datetime.datetime.now()
            item['Date'] = now.strftime("%d-%m-%Y %H:%M")

            item['Location'] = response.url
            item['Name'] = sel.xpath('a/text()').extract()
            item['Url'] = sel.xpath('a/@href').extract()
            item['Type'] = "Type 1"

            # Finally return the scraped item.
            if len(item['Url']) == 0: continue
            yield item
        """
        print("test:")
        print(response.xpath('//div[@id="_producten_zoek"]/div[@class="detail-lijst"]/table/tbody/tr/td[@class="product"]'))
        for sel in response.xpath('//div[@id="_producten_zoek"]/div[@class="detail-lijst"]/table/tbody/tr/td[@class="product"]'):
                                  #'//table[@id="product-lijst"]/tbody/tr/td[@class="product"]
            #for sel in response.xpath('//div[@id="artikel-informatie"]'):
            item = Harddisk()

            item['Location'] = response.url
            #item['Name'] = sel.xpath('/a/text()').extract()
            #item['Url'] = sel.xpath('/a/@href').extract()
            item['Provider'] = "Type 2"

            # Finally return the scraped item.
            #if len(item['Url']) == 0: continue
            yield item

    """ /table[@id="product-lijst"]/tbody/tr/
        for sel in response.xpath('//div[@id="_producten_zoek"]/div/div/a[@class="titel"]'):
            #for sel in response.xpath('//div[@id="artikel-informatie"]'):

            # Define product type TODO: make dynamic (Different components).
            item = Harddisk()
            item['Provider'] = "Type 3"

            item['Name'] = sel.xpath('h4').extract()

            item['Url'] = sel.xpath('@href').extract()
            item['Location'] = response.url

            # Finally return the scraped item.
            #if len(item['Url']) == 0: continue
            yield item
    """