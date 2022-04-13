# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter, JsonItemExporter


class MsappsourcepowerplatformPipeline:
    def open_spider(self, spider):
        self.file_csv = open('PowePlatformPublishers.csv', 'wb')
        self.file_json = open('PowePlatformPublishers.json', 'wb')

        self.exporter_csv = CsvItemExporter(self.file_csv)
        self.exporter_json = JsonItemExporter(self.file_json)

    def close_spider(self, spider):
        self.exporter_csv.finish_exporting()
        self.exporter_json.finish_exporting()

        self.file_csv.close()
        self.file_json.close()

    def process_item(self, item, spider):
        self.exporter_csv.export_item(item)
        self.exporter_json.export_item(item)

        
        spider.logger.debug(item['title'])


        return item
