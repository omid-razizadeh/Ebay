# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem
import re

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 3
    start_urls = [
        'https://ru.ebay.com/b/Iced-Teas/38181/bn_7115588208'
    ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('h3.s-item__title::text').extract()
        product_price1 = response.css('.s-item__price::text').extract()
        product_price = [re.sub('\xa0', '', fname) for fname in product_price1]


        items['product_name']=product_name
        items['product_price']=product_price


        yield items


        next_page = 'https://ru.ebay.com/b/Iced-Teas/38181/bn_7115588208?_pgn='+ str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number <= 8:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)
