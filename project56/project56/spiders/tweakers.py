# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy import Selector
from project56.items import Memory, Motherboard, Processor
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import logging
class TweakersSpider(CrawlSpider):
    name = "tweakers" # Name of the spider, to be used when crawling
    allowed_domains = ["tweakers.net"] # Where the spider is allowed to go
    DOWNLOAD_DELAY = 3.0
    start_urls = [
        'http://tweakers.net/categorie/14/basiscomponenten/producten/',


        ]
    #cd C:\Project\Project5.git\trunk\Crawler
    #scrapy crawl tweakers -o tweakers.json -t json
    #extractor = SgmlLinkExtractor()
       # Extract links matching 'item.php' and parse them with the spider's method parse_item
    rules = (
      #  Rule(LinkExtractor(restrict_xpaths=('//a[@class="next"]',)), callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//td[@class="itemname"]/p/a', )), callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths =('//li[@id="tab_responseect_specificaties"]/a', )), callback='parse_item',follow=True),
    )




    def parse_item(self, response):

        items = []
        sel = Selector(response)
        print("FUCKING TERING ZOOI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        products = sel.xpath('//div[@id="tab:specificaties"]')
        category = sel.xpath('//li[@id="tweakbaseBreadcrumbCategory"]/a/text()').extract()
        print(category)
        for product in products:
            if 'Geheugen intern' in category:
                item = Memory()
                item['Category'] = category
                item['Name'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Brand'] = product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Quantity'] = product.xpath('//tr[contains(td[1], "Aantal")]/td[2]/text()').extract()
                item['Size'] = product.xpath('//tr[contains(td[1], "Modulegrootte")]/td[2]/text()').extract()
                item['PriceGB'] = product.xpath('//tr[contains(td[1], "Prijs per GB")]/td[2]/text()').extract()
                item['Type'] = product.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract()
                item['Specification'] = product.xpath('//tr[contains(td[1], "Geheugen Specificatie")]/td[2]/text()').extract()
                item['LowVoltage'] = product.xpath('//tr[contains(td[1], "Low Voltage DDR")]/td[2]/text()').extract()
                item['Voltage'] = product.xpath('//tr[contains(td[1], "Spanning")]/td[2]/text()').extract()
                item['Warranty'] = product.xpath('//tr[contains(td[1], "Fabrieksgarantie")]/td[2]/text()').extract()
                item['Ean'] = product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['Sku'] = product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                item["Picture"] = product.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[6]/td[2]/a/img/@src').extract()
                print("Geheugen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                items.append(item)

            elif 'Moederborden' in category:
                item = Motherboard()
                item['Category'] = category
                item['Name'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Brand'] = product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Socket'] = product.xpath('//tr[contains(td[1], "Socket")]/td[2]/text()').extract()
                item['Speed'] = product.xpath('//tr[contains(td[1], "Snelheid")]/td[2]/text()').extract()
                item['SocketAmount'] = product.xpath('//tr[contains(td[1], "Aantal sockets")]/td[2]/text()').extract()
                item['Type'] = product.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract()
                item['MaxMemory'] = product.xpath('//tr[contains(td[1], "Maximum geheugengrootte")]/td[2]/text()').extract()
                item['CardInter'] = product.xpath('//tr[contains(td[1], "Card Interface")]/td[2]/text()').extract()
                item['Interface'] = product.xpath('//tr[contains(td[1], "Link Interface")]/td[2]/text()').extract()
                item['Connection'] = product.xpath('//tr[contains(td[1], "Verbinding")]/td[2]/text()').extract()
                item['Ean'] = product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['Sku'] = product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                item["Picture"] = product.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[6]/td[2]/a/img/@src').extract()
                items.append(item)

            elif "Processors" in category:
                item = Processor()
                item["Picture"] = product.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[6]/td[2]/a/img/@src').extract()
                item['Name'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Category'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Brand'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['Sku'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['Ean'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['Socket'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['Speed'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['MaxFreq'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['Specs'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['BusSpeed'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['Power'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['Virtualisation'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                item['VirtualType'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract()
                items.append(item)

            elif "Videokaarten" in category:
                item = GraphicsCard()
                item["Picture"] = product.xpath('//*[@id="tab:specificaties"]/table/tbody/tr[6]/td[2]/a/img/@src').extract()
                item['Category'] = category
                item['Name'] = product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract()
                item['Brand'] = product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract()
                item['Socket'] = product.xpath('//tr[contains(td[1], "Socket")]/td[2]/text()').extract()
                item['MaxSpeed'] = product.xpath('//tr[contains(td[1], "Maximale turbo frequentie")]/td[2]/text()').extract()
                item['MinSpeed'] = product.xpath('//tr[contains(td[1], "Nominale snelheid videochip")]/td[2]/text()').extract()
                item['SocketAmount'] = product.xpath('//tr[contains(td[1], "Aantal sockets")]/td[2]/text()').extract()
                item['Type'] = product.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract()
                item['Memory'] = product.xpath('//tr[contains(td[1], "Geheugengrootte")]/td[2]/text()').extract()
                item['Chip'] = product.xpath('//tr[contains(td[1], "Videochip")]/td[2]/text()').extract()
                item['Generation'] = product.xpath('//tr[contains(td[1], "Chipset generatie")]/td[2]/text()').extract()
                item['Height'] = product.xpath('//tr[contains(td[1], "Hoogte")]/td[2]/text()').extract()
                item['Width'] = product.xpath('//tr[contains(td[1], "Breedte")]/td[2]/text()').extract()
                item['Length'] = product.xpath('//tr[contains(td[1], "Length")]/td[2]/text()').extract()
                item['Ean'] = product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract()
                item['Sku'] = product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract()
                items.append(item)

            elif "Behuizingen" in category:

            elif "Voedingen" in category:

            elif "Processorkoeling" in category:


        return items

