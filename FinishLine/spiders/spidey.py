from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest, Request
import re
import math
import sys
reload(sys)
sys.setdefaultencoding("utf_8")
sys.getdefaultencoding()

from FinishLine.items import FinishlineItem

class mySpider(BaseSpider):
    name = 'spidey'

    allowed_domains = ["finishline.com"]

    start_urls = ['http://www.finishline.com/store/shop/men/shoes/_/N-33id6?categoryId=cat301564&mnid=men_shoes#SignUp']
                  #'http://www.finishline.com/store/product/men-s-nike-hyperdunk-2015-basketball-shoes?categoryId=cat304231&productId=prod776492']

    def itemPage(self, response):
        hxs = HtmlXPathSelector(response)
        item = FinishlineItem()

        namePath = "//h1[@itemprop='name']"
        name = hxs.select(namePath).select('text()').extract()
        item['name'] = name

        fullPricePath = "//div[@id='productPrice']/div/span[1]"
        price = hxs.select(fullPricePath).select('text()').extract()
        item['Price'] = price

        breadCrumbsPath = "//ul[@class='breadcrumbs']/li/a"
        breadCrumbs = hxs.select(breadCrumbsPath).select('text()').extract()
        item['BreadCrumbs'] = breadCrumbs

        ShoeColorPath = "//div[@id='styleColors']/span[2]"
        ShoeColor = hxs.select(ShoeColorPath).select('text()').extract()
        item['ShoeColor'] = ShoeColor

        modelPath = "//div[@id='styleColors']/span[@class='styleColorIds']"
        model = hxs.select(modelPath).select('text()').extract()
        if model!=[]:
            model = model.pop(0).replace(u'\xa0', u' ')

        item['model'] = model

        descriptionPath = "//div[@id='productDescription']/p"
        description = hxs.select(descriptionPath).select('text()').extract()

        if description != []:
            description = description.pop(0)
            description += " FEATURES: "
            featuresPath = "//div[@id='productDescription']/ul/li"
            features = hxs.select(featuresPath).select('text()').extract()
            for f in features:
                description += f + " "

        item['Description'] = description

        completePagePath = "//*"
        completePage = str(hxs.select(completePagePath).extract())
        imagesURLS = []

        while '"zoom"' in completePage:
            index = completePage.index('"zoom"')
            completePage = completePage[index+len('"zoom"')+1:]
            index2 = completePage.index(".jpg")
            iURL = completePage[:index2].strip().translate(None, '\\"')
            iURL += ".jpg"
            iURL = "http://www.finishline.com" + iURL
            imagesURLS.append(iURL)

        imagesURLS = list(set(imagesURLS))
        item['image_urls'] = imagesURLS

        brandsString = str(hxs.select("//*").extract())
        if "product_brand" in brandsString:
            index = brandsString.index('product_brand')
            brandsString = brandsString[index:]
            index = brandsString.index("[")
            brandsString = brandsString[index+1:]
            index2 = brandsString.index("]")
            brand = brandsString[:index2]
            item['Brand'] = brand.replace('"',"")

        return item

    def nextPage(self, response):
        hxs = HtmlXPathSelector(response)
        urlPaths = "//div[@class='product-container']/a/@href"
        #urls = hxs.select(urlPaths).extract()
        urls = response.xpath(urlPaths).extract()

        for url in urls:
            if "finishline" not in url:
                myRequest = Request("http://www.finishline.com"+url, callback=self.itemPage)
            else:
                myRequest = Request(url, callback=self.itemPage)
            yield myRequest

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        pagesPath = "//a[@class='paginationLink']/@href"
        pagesUrl = hxs.select(pagesPath).extract()

        for url in pagesUrl:
            if "finishline" not in url:
                myRequest = Request("http://www.finishline.com"+url, callback=self.nextPage)
            else:
                myRequest = Request(url, callback=self.nextPage)
            yield myRequest
