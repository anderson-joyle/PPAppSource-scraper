import scrapy
from MSAppSourcePowerPlatform.items import PublisherItem


class PublisherSpider(scrapy.Spider):
    name = 'Publisher'
    allowed_domains = ['appsource.microsoft.com']
    start_urls = ['https://appsource.microsoft.com/en-GB/marketplace/consulting-services?product=powerapps%3Bpower-automate%3Bpower-bi%3Bpower-virtual-agents&src=pa-m&page=1']
    base_pagination_url = 'https://appsource.microsoft.com/en-GB/marketplace/consulting-services?product=powerapps%3Bpower-automate%3Bpower-bi%3Bpower-virtual-agents&src=pa-m&page='
    base_publisher_url = 'https://appsource.microsoft.com/en-GB/marketplace/consulting-services/'
    current_page = 1

    def parse(self, response): 
        found = False    
        # for container in response.xpath("//div[@class='tileMobileContainer']"):
        for data_bi_name in response.xpath("//@data-bi-name"):
            publisher_url = self.base_publisher_url + data_bi_name.get() + "?tab=DetailsAndSupport"
            yield scrapy.Request(publisher_url, callback=self.parse_publisher)
            found = True
            
        if found:
            self.current_page = self.current_page + 1
            next_url = self.base_pagination_url + str(self.current_page)

            yield scrapy.Request(next_url, callback=self.parse)


    def parse_publisher(self, response):
        item = PublisherItem()
        item['title'] = response.xpath("//h1[@class='ms-fontSize-28 ms-fontWeight-semibold title'][1]/text()[1]").get()
        item['publisher'] = response.xpath("//div[@itemprop='publisher']/span[@class='cellLabel'][1]/text()[1]").get()
        item['pricing'] = response.xpath("//div[@itemprop='Pricing']/span[@class='cellLabel'][1]/text()[1]").get()
        item['gold_competences'] = response.xpath("//div[@itemprop='GoldCompetencies']/span[@class='cellLabel']/text()").getall()        
        item['service_type'] = response.xpath("//div[@itemprop='serviceTypes']/a/text()").getall()
        item['country_region'] = response.xpath("//div[@itemprop='Country']/span[@class='cellLabel']/text()").getall()
        # item['states_provinces'] = response.xpath("//div[@itemprop='Region']/span[@class='cellLabel']/text()").getall()
        item['learn_more_links'] = response.xpath("//div[@itemprop='App_LearnMoreTitle']/a/@href").getall()
        item['url'] = response.url

        products = response.xpath("//div[@itemprop='FilterType_Products']/a/text()").getall()

        try:
            void = products.index('Power Apps')
            item['power_apps'] = 1
        except ValueError:
            item['power_apps'] = 0

        try:
            void = products.index('Power BI')
            item['power_bi'] = 1
        except ValueError:
            item['power_bi'] = 0

        try:
            void = products.index('Power Automate')
            item['power_automate'] = 1
        except ValueError:
            item['power_automate'] = 0

        try:
            void = products.index('Power Virtual Agents')
            item['power_virtual_agents'] = 1
        except ValueError:
            item['power_virtual_agents'] = 0
        
        yield item
