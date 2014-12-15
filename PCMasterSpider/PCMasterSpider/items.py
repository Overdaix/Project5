# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
class AlternateItems(Item):
    '''
    Class for the item retrieved by scrapy.
    '''
    # Here are the fields that will be crawled and stored
    title = Field() # Game title
    link = Field()  # Link to individual game page
    cscore = Field() # Critic score
    uscore = Field()   # User score
    date = Field()  # Release date
    desc = Field()  # Description of game

class Harddisk(Item):
    '''
    Class for the item retrieved by scrapy.
    '''
    # Here are the fields that will be crawled and stored
    Category = Field() #Category like SSD, or Motherboard
    SubCategory = Field() #Sub Selection from category (example: SSD 2.5"/Server SSD/Accesoires)
    Provider = Field() #Simply said, store name.
    Title = Field() # product title
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description = Field() #General info about product.
    Model = Field()   #Model information.
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")
    ServiceInfo = Field() #Information about service and support.
    Warranty = Field () #Information about waranty period.

    #Harddisk specific info
    SSD = Field()#Information if it is a SSD or not.
    Capacity = Field() #Size information.
    Size = Field() #General size information (preferd width*dept*height).
    Cache = Field() #Cache size (in MB).
    Interface = Field() #Connection interface.
    Transferspeed = Field() #Transferspeed
    ReadSpeed = Field() # Read speed in MB.
    WriteSpeed = Field() #Write speed in MB.

class PcmasterspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
