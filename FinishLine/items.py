# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class stockItem(Item):
    Model = Field()
    Availability = Field()
    Price = Field()

class FinishlineItem(Item):
    # define the fields for your item here like:
    name = Field()
    Price = Field()
    BreadCrumbs = Field()
    Description = Field()
    image_urls = Field()
    images = Field()
    ShoeColor = Field()
    Brand = Field()
    model = Field()
    image1 = Field()
    image2 = Field()
    image3 = Field()
    image4 = Field()
    image5 = Field()
    image6 = Field()
    image7 = Field()
    image8 = Field()
    image9 = Field()
    image10 = Field()
    main_image = Field()
    Pictures = Field()


