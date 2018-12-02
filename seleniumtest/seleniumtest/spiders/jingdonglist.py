# -*- coding: utf-8 -*-
import scrapy
from seleniumtest.items import ProductItem


class JingdonglistSpider(scrapy.Spider):
    name = 'jingdonglist'
    allowed_domains = ['list.jd.com']
    url = 'https://list.jd.com/list.html?cat=670,671,672'

    def start_requests(self):
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            yield scrapy.Request(url=self.url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        print('=============================================')
        productlist = response.xpath("//li[@class='gl-item']")
        for item in productlist:
            product = ProductItem()
            product['name'] = item.xpath('.//div[@class="p-name"]//em//text()').extract_first()
            product['comment'] = item.xpath('.//div[@class="p-commit-n"]//strong//a[@class="comment"]//text()').extract_first()
            product['price'] = item.xpath('.//div[@class="p-price"]//strong[@class="J_price"]//i//text()').extract_first()
            print(product)
            yield product
