from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import FormRequest, Request
import re
import math
import sys
import base64
import time


reload(sys)
sys.setdefaultencoding("utf_8")
sys.getdefaultencoding()

from FinishLine.items import stockItem

class mySpider(BaseSpider):
    name = "stockSpidey"

    allowed_domains = ["finishline.com"]

    start_urls = ['http://www.finishline.com/store/shop/men/shoes/_/N-33id6?categoryId=cat301564&mnid=men_shoes',
                  'http://www.finishline.com/store/shop/kids/girls-shoes/_/N-33iev?categoryId=cat301672&mnid=kids_girlsshoes',
                  'http://www.finishline.com/store/shop/kids/boys-shoes/_/N-33iei?categoryId=cat301666&mnid=kids_boysshoes',
                  'http://www.finishline.com/store/shop/women/shoes/_/N-33idu?categoryId=cat301620&mnid=women_shoes']

    def shoePage(self, response):

        print "reached"

        items = []

        shoesSizesPath = '//div[@id="productSizes"]/div[@class="size"]/text()'
        shoesSizes = response.selector.xpath(shoesSizesPath).extract()


        shoesSizesUnPath = '//div[@id="productSizes"]/div[@class="size unavailable"]/text()'
        shoesSizesUn = response.selector.xpath(shoesSizesUnPath).extract()
        #print (len(shoesSizesUn))
        #for shoesSizeUn in shoesSizesUn:
            #print shoesSizeUn

       # shoesTypePath='//div[@id="productStyleColor"]/div[3]/a/@href'
        shoesModelPath = '//div[@id="styleColors"]/span[@class="styleColorIds"]/text()'
        shoesModel = response.selector.xpath(shoesModelPath).extract()
        #shoesType = Selector(text=shoesType).xpath('//span/text()').extract()

        for shoeModel in shoesModel:

                for shoesSize in shoesSizes:
                    item = stockItem()
                    shoescheckPath = '//div[@id="productPrice"]/div/span'
                    shoescheck = response.selector.xpath(shoescheckPath).extract()
                    if "fullPrice" in str(shoescheck):
                        shoesPricePath = '//div[@id="productPrice"]/div/span/text()'
                        shoesPrice = response.selector.xpath(shoesPricePath).extract()
                        item['Price'] = shoesPrice
                    elif "nowPrice" in str(shoescheck):
                        shoesPricePath = '//div[@id="productPrice"]/div/span[1]/text()'
                        shoesPrice = response.selector.xpath(shoesPricePath).extract()
                        item['Price'] = shoesPrice

                    #print len(shoesSizes)
                    if len(shoeModel)== 13:
                        item['Model'] = shoeModel[0:9] + " " + shoeModel[10:] + "-" +shoesSize
                        item['Availability'] = "Available"
                        items.append(item)

                    elif len(shoeModel)== 12:
                        item['Model'] = shoeModel[0:8] + " " + shoeModel[9:] + "-" +shoesSize
                        item['Availability'] = "Available"
                        items.append(item)


                    elif len(shoeModel)== 11:
                        item['Model'] = shoeModel[0:7] + " " + shoeModel[8:] + "-" +shoesSize
                        item['Availability'] = "Available"
                        items.append(item)

                    elif len(shoeModel)== 10:
                        item['Model'] = shoeModel[0:6] + " " + shoeModel[7:] + "-" +shoesSize
                        item['Availability'] = "Available"
                        items.append(item)


                    elif len(shoeModel)== 9:
                        item['Model'] = shoeModel[0:5] + " " + shoeModel[6:] + "-" +shoesSize
                        item['Availability'] = "Available"
                        items.append(item)

                    elif len(shoeModel)== 8:
                        item['Model'] = shoeModel[0:4] + " " + shoeModel[5:] + "-" +shoesSize
                        item['Availability'] = "Available"
                        items.append(item)

                    elif len(shoeModel)== 7:
                        item['Model'] = shoeModel[0:3] + " " + shoeModel[4:] + "-" +shoesSize
                        item['Availability'] = "Available"
                        items.append(item)



                        items.append(item)

        for shoeModel in shoesModel:

                for shoesSizeUn in shoesSizesUn:
                    item = stockItem()
                    shoescheckPath = '//div[@id="productPrice"]/div/span'
                    shoescheck = response.selector.xpath(shoescheckPath).extract()
                    if "fullPrice" in str(shoescheck):
                        shoesPricePath = '//div[@id="productPrice"]/div/span/text()'
                        shoesPrice = response.selector.xpath(shoesPricePath).extract()
                        item['Price'] = shoesPrice
                    elif "nowPrice" in str(shoescheck):
                        shoesPricePath = '//div[@id="productPrice"]/div/span[1]/text()'
                        shoesPrice = response.selector.xpath(shoesPricePath).extract()
                        item['Price'] = shoesPrice


                    #print len(shoesSizes)
                    if len(shoeModel)== 13:
                        item['Model'] = shoeModel[0:9] + " " + shoeModel[10:] + "-" +shoesSizeUn
                        item['Availability'] = "UnAvailable"
                        items.append(item)

                    elif len(shoeModel)== 12:
                        item['Model'] = shoeModel[0:8] + " " + shoeModel[9:] + "-" +shoesSizeUn
                        item['Availability'] = "UnAvailable"
                        items.append(item)

                    elif len(shoeModel)== 11:
                        item['Model'] = shoeModel[0:7] + " " + shoeModel[8:] + "-" +shoesSizeUn
                        item['Availability'] = "UnAvailable"
                        items.append(item)

                    elif len(shoeModel)== 10:

                        item['Model'] = shoeModel[0:6] + " " + shoeModel[7:] + "-" +shoesSizeUn
                        item['Availability'] = "unAvailable"

                        items.append(item)

                    elif len(shoeModel)== 9:
                        item['Model'] = shoeModel[0:5] + " " + shoeModel[6:] + "-" +shoesSizeUn
                        item['Availability'] = "unAvailable"
                        items.append(item)

                    elif len(shoeModel)== 8:
                        item['Model'] = shoeModel[0:4] + " " + shoeModel[5:] + "-" +shoesSizeUn
                        item['Availability'] = "unAvailable"
                        items.append(item)

                    elif len(shoeModel)== 7:
                        item['Model'] = shoeModel[0:3] + " " + shoeModel[4:] + "-" +shoesSizeUn
                        item['Availability'] = "unAvailable"
                        items.append(item)

        return items

    def nextPage(self, response):

        shoesPath = '//div[@class="product-container"]/a/@href'
        shoes = response.selector.xpath(shoesPath).extract()
     
        for shoe in shoes:
            myRequest = Request("http://www.finishline.com" + shoes.pop(0), callback=self.shoePage)

            yield myRequest



    def parse(self, response):

        #response.selector.xpath('//span/text()').extract()
        pagesPath = "//a[@class='paginationLink']/@href"
        pagesUrl = response.selector.xpath(pagesPath).extract()

        for url in pagesUrl:
            print url
            if "finishline" not in url:
                myRequest = Request("http://www.finishline.com"+url, callback=self.nextPage)
            else:
                myRequest = Request(url, callback=self.nextPage)
            yield myRequest
