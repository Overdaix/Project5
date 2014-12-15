__author__ = 'Dean'

from scrapy.item import Item, Field
class Harddisk(Item):
    '''
    Class for the item retrieved by scrapy.
    '''
    # Here are the fields that will be crawled and stored
    Title = Field() # Game title
    Url = Field()  # Link to product page.
    Price = Field() #Product price.
    Date = Field()  # Release date
    Name = Field() # Name of the product.
    Sku = Field()# Stock keeping unit.
    Ean = Field()# European article number.
    Description= Field() #General info about product.
    SSD = Field()#Information if it is a SSD or not.
    Type  = Field()  #Type information, intern/extern.
    Capacity = Field() #Size information.
    Model = Field()   #Model information.
    Size = Field() #General size information (preferd width*dept*height).
    Type = Field() #Intern/Extern.
    Location = Field() #Inter/Extern.
    Cache = Field() #Cache size (in MB).
    Interface = Field() #Connection interface.
    ServiceInfo = Field() #Information about service and support.
    Transferspeed = Field() #Transferspeed
    ReadSpeed = Field() # Read speed in MB.
    WriteSpeed = Field() #Write speed in MB.
    Software = Field() #Info about software provided.
    Bay = Field() #Information about compatible bay (example: 1x intern - 2.5")