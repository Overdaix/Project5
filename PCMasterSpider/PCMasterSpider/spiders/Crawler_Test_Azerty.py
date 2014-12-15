from scrapy.item import Item, Field
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from PCMasterSpider.items import Harddisk
from scrapy.contrib.linkextractors import LinkExtractor
import datetime
import json
"""
Crawler for Azerty.nl, crawls products, for links use other crawler.

To execute run: scrapy crawl Test_Azerty -o Azerty1.json -t json
"""

class Products_Azerty(CrawlSpider):

    # The unique name with wich the crawler is executed
    name = 'Test_Azerty'
    allowed_domains = ["azerty.nl"]

    # Crawler starts with this url.
    start_urls = [
        "http://azerty.nl/8-1990-678801/crucial-m550-solid-state-drive-128-gb-intern-2-5-sata-600.html",
        "http://azerty.nl/8/componenten.html",
    ]

    deny_domain =[
        "http://azerty.nl/36/randapparatuur.html",
        "http://azerty.nl/1/laptop-amp-pc.html",
        "http://azerty.nl/4/tablets-amp-telefoons.html",
        "http://azerty.nl/31/server.html",
        "http://azerty.nl/11/netwerk.html",
        "http://azerty.nl/7/software.html",
        "http://azerty.nl/2/beeld-amp-geluid.html",
        "http://azerty.nl/37/printing.html",
        "http://azerty.nl/42/industrieel.html",
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="knop_volgende"]')), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="menu"]/ul/li/ul/li[position()=4 or position()=5 or position()=7 or position()=8 or position()=9 or position()=11 or position()=13 or position()=14 or position()=16 or position()=17 or position()=20]/a', )),callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//li[@class="node open group"]/ul/li/a', )), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//li[@class="info"]/a', )), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        #for sel in response.xpath('//div[@id="artikel-kenmerken"]'):
        for sel in response.xpath('//div[@id="artikel-kenmerken"]'):

            listCategory = sel.xpath('//li[@class="node open group"]/a/text()').extract()
            listSubCategory = sel.xpath('//li[@class="leaf active"]/a/text()').extract()
            #if any("SSD's" in s for s in listCategory):

            if "SSD's" in listCategory:
                item = Harddisk()

                item['Category'] = listCategory
                item['SubCategory'] = listSubCategory
                item['Provider'] = "azerty.nl"
                now = datetime.datetime.now()
                item['Date'] = now.strftime("%d-%m-%Y %H:%M")

                item['Url'] = response.url
                item['Sku'] = sel.xpath('//ul[contains(li[1], "'+"Sku's"+'")]/li[2]/text()').extract()
                item['Price'] = sel.xpath('//*[@id="_producten_product_detail"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/text()').extract()

                item['Title'] = sel.xpath('//h1[@class="artikel"]/text()').extract()


                item['Url'] = response.url

                yield item
            if "Harddisk Intern" in listCategory:
                item = Harddisk()

                item['Category'] = listCategory
                item['SubCategory'] = listSubCategory
                item['Provider'] = "azerty.nl"
                now = datetime.datetime.now()
                item['Date'] = now.strftime("%d-%m-%Y %H:%M")

                item['Url'] = response.url
                item['Sku'] = sel.xpath('//ul[contains(li[1], "'+"Sku's"+'")]/li[2]/text()').extract()
                item['Price'] = sel.xpath('//*[@id="_producten_product_detail"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/text()').extract()

                item['Title'] = sel.xpath('//h1[@class="artikel"]/text()').extract()


                item['Url'] = response.url

                yield item