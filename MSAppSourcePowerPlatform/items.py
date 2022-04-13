# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PublisherItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    publisher = scrapy.Field()
    overview = scrapy.Field()
    pricing = scrapy.Field()
    gold_competences = scrapy.Field()
    # products = scrapy.Field()
    service_type = scrapy.Field()
    country_region = scrapy.Field()
    # states_provinces = scrapy.Field()
    learn_more_links = scrapy.Field()
    url = scrapy.Field()

    power_apps = scrapy.Field()
    power_bi = scrapy.Field()
    power_automate = scrapy.Field()
    power_virtual_agents = scrapy.Field()

    # pass
