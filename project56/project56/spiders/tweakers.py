# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy import Selector
from project56.items import Memory, Motherboard, Processor, GraphicsCard, Power, Case, Cooler
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import logging
class TweakersSpider(CrawlSpider):
    name = "tweakers" # Name of the spider, to be used when crawling
    allowed_domains = ["tweakers.net"] # Where the spider is allowed to go
    DOWNLOAD_DELAY = 2.0
    start_urls = [
        'http://tweakers.net/categorie/545/geheugen-intern/producten/',
        'http://tweakers.net/categorie/49/videokaarten/producten/',
        'http://tweakers.net/categorie/47/moederborden/producten/',
        'http://tweakers.net/categorie/61/behuizingen/producten/',
        'http://tweakers.net/categorie/46/processors/producten/',
        'http://tweakers.net/categorie/664/voedingen/producten/',
        'http://tweakers.net/categorie/488/processorkoeling/producten/',


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
                item['Name'] = ''.join(product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract())
                item['Brand'] = ''.join(product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract())
                item['Quantity'] = ''.join(product.xpath('//tr[contains(td[1], "Aantal")]/td[2]/text()').extract())
                item['Size'] = ''.join(product.xpath('//tr[contains(td[1], "Modulegrootte")]/td[2]/text()').extract())
                item['PriceGB'] = ''.join(product.xpath('//tr[contains(td[1], "Prijs per GB (geheugen)")]/td[2]/text()').extract())
                item['Type'] = ''.join(product.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract())
                item['Specification'] = ''.join(product.xpath('//tr[contains(td[1], "Geheugen Specificatie")]/td[2]/text()').extract())
                item['LowVoltage'] = ''.join(product.xpath('//tr[contains(td[1], "Low Voltage DDR")]/td[2]/text()').extract())
                item['Voltage'] = ''.join(product.xpath('//tr[contains(td[1], "Spanning")]/td[2]/text()').extract())
                item['Warranty'] = ''.join(product.xpath('//tr[contains(td[1], "Fabrieksgarantie")]/td[2]/text()').extract())
                item['Ean'] = ''.join(product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract())
                item['Sku'] = ''.join(product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract())
                item["Picture"] = ''.join(product.xpath('//tr[contains(td[1], "Afbeelding")]/td[2]/a/@src').extract())
                print("Geheugen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                items.append(item)

            elif 'Moederborden' in category:
                item = Motherboard()
                item['Category'] = category
                item['Name'] = ''.join(product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract())
                item['Brand'] = ''.join(product.xpath('//[@id="tab:specificaties"]/table/tbody/tr[3]/td[2]/a/text()').extract())
                item['Socket'] = ''.join(product.xpath('//tr[contains(td[1], "Socket")]/td[2]/text()').extract())
                item['Speed'] = ''.join(product.xpath('//tr[contains(td[1], "Snelheid")]/td[2]/text()').extract())
                item['SocketAmount'] = ''.join(product.xpath('//tr[contains(td[1], "Aantal sockets")]/td[2]/text()').extract())
                item['Type'] = ''.join(product.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract())
                item['MaxMemory'] = ''.join(product.xpath('//tr[contains(td[1], "Maximum geheugengrootte")]/td[2]/text()').extract())
                item['CardInter'] = ''.join(product.xpath('//tr[contains(td[1], "Card Interface")]/td[2]/text()').extract())
                item['Interface'] = ''.join(product.xpath('//tr[contains(td[1], "Link Interface")]/td[2]/text()').extract())
                item['Connection'] = ''.join(product.xpath('//tr[contains(td[1], "Verbinding")]/td[2]/text()').extract())
                item['Ean'] = ''.join(product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract())
                item['Sku'] = ''.join(product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract())
                item["Picture"] = ''.join(product.xpath('//tr[contains(td[1], "Afbeelding")]/td[2]/a/@src').extract())
                items.append(item)

            elif "Processors" in category:
                item = Processor()
                item["Picture"] = ''.join(product.xpath('//tr[contains(td[1], "Afbeelding")]/td[2]/a/@src').extract())
                item['Name'] = ''.join(product.xpath('//tr[contains(td[1], "Product")]/td[2]/a/text()').extract())
                item['Category'] = ''.join(product.xpath('//tr[contains(td[1], "Categorie")]/td[2]/a/text()').extract())
                item['Brand'] = ''.join(product.xpath('//tr[contains(td[1], "Merk")]/td[2]/text()').extract())
                item['Sku'] = ''.join(product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract())
                item['Ean'] = ''.join(product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract())
                item['Socket'] = ''.join(product.xpath('//tr[contains(td[1], "Socket")]/td[2]/text()').extract())
                item['Speed'] = ''.join(product.xpath('//tr[contains(td[1], "Snelheid")]/td[2]/text()').extract())
                item['CoreAmount'] = ''.join(product.xpath('//tr[contains(td[1], "Aantal cores")]/td[2]/text()').extract())
                item['Specs'] = ''.join(product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/text()').extract())
                items.append(item)

            elif "Videokaarten" in category:
                item = GraphicsCard()
                item["Picture"] = ''.join(product.xpath('//tr[contains(td[1], "Afbeelding")]/td[2]/a/@src').extract())
                item['Category'] = ''.join(category)
                item['Name'] = ''.join(product.xpath('//*[@id="entity"]/div/div[2]/header/h1/a/text()').extract())
                item['Brand'] = ''.join(product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract())
                item['MaxSpeed'] = ''.join(product.xpath('//tr[contains(td[1], "Maximale turbo frequentie")]/td[2]/text()').extract())
                item['MinSpeed'] = ''.join(product.xpath('//tr[contains(td[1], "Nominale snelheid videochip")]/td[2]/text()').extract())
                item['Type'] =''.join(product.xpath('//tr[contains(td[1], "Geheugentype")]/td[2]/text()').extract())
                item['Memory'] = ''.join(product.xpath('//tr[contains(td[1], "Geheugengrootte")]/td[2]/text()').extract())
                item['Chip'] = ''.join(product.xpath('//tr[contains(td[1], "Videochip")]/td[2]/text()').extract())
                item['Generation'] = ''.join(product.xpath('//tr[contains(td[1], "Chipset generatie")]/td[2]/text()').extract())
                item['Height'] = ''.join(product.xpath('//tr[contains(td[1], "Hoogte")]/td[2]/text()').extract())
                item['Width'] = ''.join(product.xpath('//tr[contains(td[1], "Breedte")]/td[2]/text()').extract())
                item['Length'] = ''.join(product.xpath('//tr[contains(td[1], "Length")]/td[2]/text()').extract())
                item['Ean'] = ''.join(product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract())
                item['Sku'] = ''.join(product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract())
                items.append(item)

            elif "Behuizingen" in category:
                item = Case()
                item["Picture"] = ''.join(product.xpath('//tr[contains(td[1], "Afbeeldingen")]/td[2]/a/@src').extract())
                item['Category'] = category
                item['Name'] = ''.join(product.xpath('//tr[contains(td[1], "Product")]/td[2]/a/text()').extract())
                item['Brand'] = ''.join(product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract())
                item['Type'] = ''.join(product.xpath('//tr[contains(td[1], "Behuizingtype")]/td[2]/text()').extract())
                item['FormFactor'] = ''.join(product.xpath('//tr[contains(td[1], "Form Factor")]/td[2]/text()').extract())
                item['Width'] = ''.join(product.xpath('//tr[contains(td[1], "Breedte")]/td[2]/text()').extract())
                item['Height'] = ''.join(product.xpath('//tr[contains(td[1], "Hoogte")]/td[2]/text()').extract())
                item['Depth'] = ''.join(product.xpath('//tr[contains(td[1], "Diepte")]/td[2]/text()').extract())
                items.append(item)

            elif "Voedingen" in category:
                item = Power()
                item["Picture"] = ''.join(product.xpath('//tr[contains(td[1], "Afbeeldingen")]/td[2]/a/@src').extract())
                item['Category'] = ''.join(category)
                item['Name'] = ''.join(product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract())
                item['Brand'] = ''.join(product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract())
                item['Power'] = ''.join(product.xpath('//tr[contains(td[1], "Vermogen")]/td[2]/text()').extract())
                item['Capacity'] = ''.join(product.xpath('//tr[contains(td[1], "Capaciteit 12V1 rail")]/td[2]/text()').extract())
                item['Width'] = ''.join(product.xpath('//tr[contains(td[1], "Breedte")]/td[2]/text()').extract())
                item['Height'] = ''.join(product.xpath('//tr[contains(td[1], "Hoogte")]/td[2]/text()').extract())
                item['Depth'] = ''.join(product.xpath('//tr[contains(td[1], "Diepte")]/td[2]/text()').extract())
                item['Ean'] = ''.join(product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract())
                item['Sku'] = ''.join(product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract())
                items.append(item)

            elif "Processorkoeling" in category:
                item = Cooler()
                item["Picture"] = ''.join(product.xpath('//tr[contains(td[1], "Afbeeldingen")]/td[2]/a/@src').extract())
                item['Category'] = ''.join(category)
                item['Name'] = ''.join(product.xpath('//tr[contains(td[1], "Uitvoering")]/td[2]/a/text()').extract())
                item['Brand'] = ''.join(product.xpath('//tr[contains(td[1], "Merk")]/td[2]/a/text()').extract())
                item['Socket'] = ''.join(product.xpath('//tr[contains(td[1], "Socket")]/td[2]/text()').extract())
                item['Heatpipes'] = ''.join(product.xpath('//tr[contains(td[1], "Heatpipes")]/td[2]/text()').extract())
                item['RotationSpeedMin'] = ''.join(product.xpath('//tr[contains(td[1], "Rotatiesnelheid (min)")]/td[2]/text()').extract())
                item['RotationSpeedMax'] = ''.join(product.xpath('//tr[contains(td[1], "Rotatiesnelheid (max)")]/td[2]/text()').extract())
                item['Ean'] = ''.join(product.xpath('//tr[contains(td[1], "EAN")]/td[2]/text()').extract())
                item['Sku'] = ''.join(product.xpath('//tr[contains(td[1], "SKU")]/td[2]/text()').extract())
                items.append(item)

        return items

