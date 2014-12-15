__author__ = 'Dean'

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
    categorie = Field()