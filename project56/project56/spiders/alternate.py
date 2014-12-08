from scrapy.http import Request
from scrapy import Selector
from project56.items import Memory, Motherboard, Processor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import logging
class AlternateSpider(CrawlSpider):
    name = "alternate" # Name of the spider, to be used when crawling
    allowed_domains = ["alternate.nl"] # Where the spider is allowed to go
    DOWNLOAD_DELAY = 2.0
    start_urls = [
        'http://www.alternate.nl/html/product/listing.html?navId=20678&tk=7&lk=13472',


        ]
    #scrapy crawl alternate -o alternate.json -t json
    #extractor = SgmlLinkExtractor()
       # Extract links matching 'item.php' and parse them with the spider's method parse_item
    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="listingResult"]/div[50]/a[4]',)), callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="productLink"]', )), callback='parse_item',follow=True),
       # Rule(LinkExtractor(restrict_xpaths =('//li[@id="tab_responseect_specificaties"]/a', )), callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        items = []
        sel = Selector(response)
        print("test1")
        products = sel.xpath('//*[@id="coreProductInfos"]/div[2]')
       # breadcrumbs = sel.xpath('//div[@id ="contentWrapper"]')\
        table = sel.xpath('//tr[contains(td, "techDataCol")]')
        category = sel.xpath('//*[@id="contentWrapper"]/div[1]/span[2]/a/span/text()').extract()
        print(category)
        for product in products:
            if 'Geheugen' in category:
                item = Memory()
                print (table.xpath('//td/text()').extract())
                item['Category'] = category
                item['Name'] = product.xpath('//td[contains(td[1], "Modelnaam")]/td[2]/table/tbody/tr/td/text()').extract()
                item['Brand'] = product.xpath('//*[@id="details"]/div[4]/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td/text()').extract()
                item['Quantity'] = product.xpath('//tr[contains(td[1], "Aantal")]/td[2]/text()').extract()
                item['Size'] = product.xpath('//tr[contains(td[1], "Modulegrootte")]/td[2]/text()').extract()
                item['PriceGB'] = product.xpath('//tr[contains(td[1], "Prijs per GB")]/td[2]/text()').extract()
                item['Type'] = product.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract()
                item['Specification'] = product.xpath('//tr[contains(td[1], "Geheugen Specificatie")]/td[2]/text()').extract()
                item['LowVoltage'] = product.xpath('//tr[contains(td[1], "Low Voltage DDR")]/td[2]/text()').extract()
                item['Voltage'] = product.xpath('//tr[contains(td[1], "Spanning")]/td[2]/text()'). extract()
                item['Warranty'] = product.xpath('//tr[contains(td[1], "Fabrieksgarantie")]/td[2]/text()').extract()
                item['Ean'] = product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['Sku'] = product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                print("Geheugen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                items.append(item)
            return items