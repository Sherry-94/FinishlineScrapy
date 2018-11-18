# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

# class FinishlinePipeline(object):
#     def process_item(self, item, spider):
#         return item


class MyImagesPipeline(ImagesPipeline):

    main_image_url = ""

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            if "_fl.jpg" in image_url:
                self.main_image_url = image_url
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        image_urls = [x['url'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        if self.main_image_url != "":
            # item['main_image'] = self.main_image_url
            for url, path in zip(image_urls, image_paths):
                if "_fl.jpg" in url:
                    item['main_image'] = path

        if image_paths:
            item['image1'] = image_paths.pop(0)
        if image_paths:
            item['image2'] = image_paths.pop(0)
        if image_paths:
            item['image3'] = image_paths.pop(0)
        if image_paths:
            item['image4'] = image_paths.pop(0)
        if image_paths:
            item['image5'] = image_paths.pop(0)
        if image_paths:
            item['image6'] = image_paths.pop(0)
        if image_paths:
            item['image7'] = image_paths.pop(0)
        if image_paths:
            item['image8'] = image_paths.pop(0)
        if image_paths:
            item['image9'] = image_paths.pop(0)
        if image_paths:
            item['image10'] = image_paths.pop(0)
        # item['image_paths'] = image_paths
        return item