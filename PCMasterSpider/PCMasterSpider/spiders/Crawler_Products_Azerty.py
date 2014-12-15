from scrapy.item import Item, Field
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from PCMasterSpider.items import Harddisk
from scrapy.contrib.linkextractors import LinkExtractor
import datetime
import json
"""
Crawler for Azerty.nl, crawls products, for links use other crawler.

To execute run: scrapy crawl Products_Azerty -o Azerty.json -t json
"""

class Products_Azerty(CrawlSpider):

    # The name is the unique identifier for this spider.
    name = 'Products_Azerty'
    allowed_domains = ["azerty.nl"]

    # These URLs are the initial requests performed by the spider.
    start_urls = [
        "http://azerty.nl/8/componenten.html",
        "http://azerty.nl/8-1156/-koopjeshoek.html" ,
         "http://azerty.nl/8-3495/-2-euro.html" ,
         "http://azerty.nl/8-3497/5-euro.html" ,
         "http://azerty.nl/8-3785/10-euro.html" ,
         "http://azerty.nl/8-5696/cadeaubonnen.html" ,
         "http://azerty.nl/8-930/overige-accessoires.html" ,
         "http://azerty.nl/8-600/wizards.html" ,
         "http://azerty.nl/8-2634/xtra-categorie-n.html" ,
         "http://azerty.nl/8-969/videokaarten.html" ,
         "http://azerty.nl/8-5884/amd.html" ,
         "http://azerty.nl/8-1597/matrox.html" ,
         "http://azerty.nl/8-1596/nvidia.html" ,
         "http://azerty.nl/8-6291/extern.html" ,
         "http://azerty.nl/8-910/processoren.html" ,
         "http://azerty.nl/8-1600/amd.html" ,
         "http://azerty.nl/8-1601/intel.html" ,
         "http://azerty.nl/8-1445/server.html" ,
         "http://azerty.nl/8-61/koelers.html" ,
         "http://azerty.nl/8-1094/accessoires.html" ,
         "http://azerty.nl/8-1086/chipset.html" ,
         "http://azerty.nl/8-1087/fan-control.html" ,
         "http://azerty.nl/8-1088/fans.html" ,
         "http://azerty.nl/8-1089/geheugen.html" ,
         "http://azerty.nl/8-1090/geluidsdemping.html" ,
         "http://azerty.nl/8-1091/grafische-kaart.html" ,
         "http://azerty.nl/8-1092/harddisk.html" ,
         "http://azerty.nl/8-1167/kabels.html" ,
         "http://azerty.nl/8-83/koel-accessoires.html" ,
         "http://azerty.nl/8-1093/koelpasta-amp-lijm.html" ,
         "http://azerty.nl/8-976/processor-.html" ,
         "http://azerty.nl/8-223/waterkoeling.html" ,
         "http://azerty.nl/8-1988/ssd-s.html" ,
         "http://azerty.nl/8-1990/2-5-inch.html" ,
         "http://azerty.nl/8-902/1-8-inch.html" ,
         "http://azerty.nl/8-3280/-msata.html" ,
         "http://azerty.nl/8-5931/-m-2.html" ,
         "http://azerty.nl/8-1989/pci-express.html" ,
         "http://azerty.nl/8-1991/server-ssd.html" ,
         "http://azerty.nl/8-5728/flash-module.html" ,
         "http://azerty.nl/8-5743/accessoires.html" ,
         "http://azerty.nl/8-853/harddisk-intern.html" ,
         "http://azerty.nl/8-855/-sata-2-5-inch.html" ,
         "http://azerty.nl/8-857/-sata-3-5-inch.html" ,
         "http://azerty.nl/8-2302/-server-hdd.html" ,
         "http://azerty.nl/8-1649/accessoires.html" ,
         "http://azerty.nl/8-826/overig.html" ,
         "http://azerty.nl/8-4731/reserve-onderdelen.html" ,
         "http://azerty.nl/8-842/moederborden.html" ,
         "http://azerty.nl/8-2651/-amd.html" ,
         "http://azerty.nl/8-2652/-intel.html" ,
         "http://azerty.nl/8-4221/-server.html" ,
         "http://azerty.nl/8-843/met-cpu.html" ,
         "http://azerty.nl/8-839/overige-moederborden.html" ,
         "http://azerty.nl/8-1216/riser-kaart.html" ,
         "http://azerty.nl/8-674/voedingen.html" ,
         "http://azerty.nl/8-1073/-atx-voedingen.html" ,
         "http://azerty.nl/8-5131/-sfx-voedingen.html" ,
         "http://azerty.nl/8-5381/flexatx.html" ,
         "http://azerty.nl/8-3478/overige-voedingen.html" ,
         "http://azerty.nl/8-5170/picopsu.html" ,
         "http://azerty.nl/8-69/geluidskaarten.html" ,
         "http://azerty.nl/8-3603/extern.html" ,
         "http://azerty.nl/8-129/intern.html" ,
         "http://azerty.nl/8-761/overig.html" ,
         "http://azerty.nl/8-1026/controllers.html" ,
         "http://azerty.nl/8-3344/io-controllers.html" ,
         "http://azerty.nl/8-1993/non-raid.html" ,
         "http://azerty.nl/8-1637/raid.html" ,
         "http://azerty.nl/8-859/dvd-blu-ray.html" ,
         "http://azerty.nl/8-5161/bd-combo.html" ,
         "http://azerty.nl/8-860/blu-ray-branders.html" ,
         "http://azerty.nl/8-861/blu-ray-drives.html" ,
         "http://azerty.nl/8-4986/dvd-branders.html" ,
         "http://azerty.nl/8-4988/dvd-drives.html" ,
         "http://azerty.nl/8-62/geheugen-pc-server.html" ,
         "http://azerty.nl/8-178/-sdr.html" ,
         "http://azerty.nl/8-735/-ddr1.html" ,
         "http://azerty.nl/8-1603/-ddr2.html" ,
         "http://azerty.nl/8-1604/-ddr3.html" ,
         "http://azerty.nl/8-6116/ddr4.html" ,
         "http://azerty.nl/8-5886/overig-geheugen.html" ,
         "http://azerty.nl/8-1463/server-geheugen.html" ,
         "http://azerty.nl/8-1925/systeemspecifiek.html" ,
         "http://azerty.nl/8-4774/assemblage-service.html" ,
         "http://azerty.nl/8-255/assemblage.html" ,
         "http://azerty.nl/8-4777/assemblage-installatie.html" ,
         "http://azerty.nl/8-4775/installatie.html" ,
         "http://azerty.nl/8-4776/service-on-site.html" ,
         "http://azerty.nl/8-1969/nas.html" ,
         "http://azerty.nl/8-1219/-1-bay.html" ,
         "http://azerty.nl/8-1970/-2-bay.html" ,
         "http://azerty.nl/8-2948/-4-bay.html" ,
         "http://azerty.nl/8-1973/-5-bay.html" ,
         "http://azerty.nl/8-1974/-6-bay.html" ,
         "http://azerty.nl/8-1975/-7-bay.html" ,
         "http://azerty.nl/8-1976/-8-bay.html" ,
         "http://azerty.nl/8-2969/10-bay.html" ,
         "http://azerty.nl/8-1977/12-bay.html" ,
         "http://azerty.nl/8-2970/16-bay.html" ,
         "http://azerty.nl/8-5157/accessoires.html" ,
         "http://azerty.nl/8-827/netwerk-storage.html" ,
         "http://azerty.nl/8-1095/kabels-en-adapters.html" ,
         "http://azerty.nl/8-1533/adapters.html" ,
         "http://azerty.nl/8-3210/antennemateriaal.html" ,
         "http://azerty.nl/8-1528/audio-.html" ,
         "http://azerty.nl/8-5002/bevestiging.html" ,
         "http://azerty.nl/8-1531/computer-extern.html" ,
         "http://azerty.nl/8-2330/computer-intern.html" ,
         "http://azerty.nl/8-3213/draadloze-a-v.html" ,
         "http://azerty.nl/8-4769/kabelterminals.html" ,
         "http://azerty.nl/8-1530/netwerk-.html" ,
         "http://azerty.nl/8-246/overig.html" ,
         "http://azerty.nl/8-3816/schakelaars-splitters.html" ,
         "http://azerty.nl/8-3053/telefoon.html" ,
         "http://azerty.nl/8-1529/video-.html" ,
         "http://azerty.nl/8-72/backup.html" ,
         "http://azerty.nl/8-1655/-tapedrives.html" ,
         "http://azerty.nl/8-1661/-tapes.html" ,
         "http://azerty.nl/8-833/overige-media.html" ,
         "http://azerty.nl/8-2395/barebone.html" ,
         "http://azerty.nl/8-5824/-met-cpu.html" ,
         "http://azerty.nl/8-5823/-zonder-cpu.html" ,
         "http://azerty.nl/8-80/accessoires.html" ,
         "http://azerty.nl/8-1605/geheugen-laptop.html" ,
         "http://azerty.nl/8-736/so-dimm-ddr.html" ,
         "http://azerty.nl/8-739/so-dimm-ddr2.html" ,
         "http://azerty.nl/8-5888/so-dimm-ddr3.html" ,
         "http://azerty.nl/8-758/so-dimm-ddr3l.html" ,
         "http://azerty.nl/8-1931/systeemspecifiek.html" ,
         "http://azerty.nl/8-1042/behuizingen.html" ,
         "http://azerty.nl/8-1046/-bureaumodel.html" ,
         "http://azerty.nl/8-1048/-fulltowermodel.html" ,
         "http://azerty.nl/8-1045/-htpc.html" ,
         "http://azerty.nl/8-1049/-microtowermodel.html" ,
         "http://azerty.nl/8-1044/-midtowermodel.html" ,
         "http://azerty.nl/8-1831/-mini-itx.html" ,
         "http://azerty.nl/8-1047/-minitowermodel.html" ,
         "http://azerty.nl/8-1043/-towermodel.html" ,
         "http://azerty.nl/8-5122/casemods-accessoires.html" ,
         "http://azerty.nl/8-5895/intel-nuc.html" ,
         "http://azerty.nl/8-4840/overig.html" ,
         "http://azerty.nl/8-2297/server-behuizingen.html"
    ]

    rules = (
        #Rule(LinkExtractor(restrict_xpaths =('//*[@id="_producten_zoek_"]/div[5]/div/ul/li/ul/li[position()=4 or position()=5 or (position()>=7 and position()<=9) or position()=11 or position()=13 or position()=14 or position()=16 or position()=17 or position()=20]/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths =('//li[@class="node open group"]/ul/li/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths =('//li[@class="info"]/a', )),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//div[@class="menu"]/ul/li/ul/li/a')),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//div[@class="menu"]/ul/li/ul/li/ul/li/a')),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//div[@id="_producten_zoek"]/div/div/a[@class="titel"]')),callback='parse_item',follow=True),
        #Rule(LinkExtractor(restrict_xpaths=('//td[@class="product"]/a')),callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//a[@class="knop_volgende"]')),callback='parse_item',follow=True),
    )


    def parse_item(self, response):
        for sel in response.xpath('//div[@id="artikel-informatie"]'):
            #for sel in response.xpath('//div[@id="artikel-informatie"]'):
            #sel = Selector(response)

            # Define product type TODO: make dynamic (Different components).
            item = Harddisk()

            item['Provider'] = "azerty.nl"
            now = datetime.datetime.now()
            item['Date'] = now.strftime("%d-%m-%Y %H:%M")

            item['Url'] = response.url
            item['Category'] = sel.xpath('//li[@class="node open group"]/a/text()').extract()
            item['SubCategory'] = sel.xpath('//li[@class="leaf active"]/a/text()').extract()

            item['Title'] = sel.xpath('//h1[@class="artikel"]/text()').extract()
            item['Ean'] = sel.xpath('//ul[contains(li[1], "'+"Ean's"+'")]/li[2]/text()').extract()
            item['Sku'] = sel.xpath('//ul[contains(li[1], "'+"Sku's"+'")]/li[2]/text()').extract()
            item['Price'] = sel.xpath('//*[@id="_producten_product_detail"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/text()').extract()

            item['Description'] = sel.xpath('//*[@id="_producten_product_detail"]/div[1]/div[1]/div[1]/div/h2/text()').extract()
            item['Model'] = sel.xpath('//ul[contains(li[1], "'+"Model"+'")]/li[2]/text()').extract()
            item['ServiceInfo'] = sel.xpath('//ul[contains(li[1], "'+"Service & Support"+'")]/li[2]/text()').extract()
            item['Warranty'] = sel.xpath('//ul[contains(li[1], "'+"Garantie van de fabrikant"+'")]/li[2]/text()').extract()

            item['Type'] = sel.xpath('//ul[contains(li[1], "'+"Type"+'")]/li[2]/text()').extract()
            item['Capacity'] = sel.xpath('//ul[contains(li[1], "'+"Capaciteit"+'")]/li[2]/text()').extract()[0]
            item['Size'] = sel.xpath('//ul[contains(li[1], "'+"Afmetingen "+'")]/li[2]/text()').extract()

            # Finally return the scraped item.
            yield item