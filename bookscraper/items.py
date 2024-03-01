# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = Field()
    category = Field()
    description = Field()
    price = Field()
    pass
