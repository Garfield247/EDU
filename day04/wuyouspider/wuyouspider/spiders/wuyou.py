# -*- coding: utf-8 -*-
import redis
import scrapy
from scrapy_redis.spiders import RedisSpider
from wuyouspider.items import WuyouspiderItem

class WuyouSpider(RedisSpider):
    name = 'wuyou'
    # allowed_domains = ['www.51job.com']
    def start_requests(self):
        start_urls = 'https://search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        yield scrapy.Request(url=start_urls,callback=self.parse)

    def parse(self, response):
        item = WuyouspiderItem()
        # print(response.text)
        job_divs = response.xpath('.//div[@id="resultList"]/div[@class="el"]')
        for job_div in job_divs:
            item['job_name'] = job_div.xpath('./p[starts-with(@class,"t1")]/span/a/text()').extract_first()
            item['comp_name'] = job_div.xpath('./span[@class="t2"]/a/text()').extract_first()
            item['location'] = job_div.xpath('./span[@class="t3"]/text()').extract_first()
            item['salary'] = job_div.xpath('./span[@class="t4"]/text()').extract_first()
            item['pub_date'] = job_div.xpath('./span[@class="t5"]/text()').extract_first()
            info_url = job_div.xpath('./p[starts-with(@class,"t1")]/span/a/@href').extract_first()
            print(info_url)
            yield scrapy.Request(url=info_url,callback=self.parse_info,meta={'item':item})
        next_url = response.xpath('.//div[@class="p_in"]/ul/li[@class="bk"][2]/a/@href').extract_first()
        if next_url:
            yield scrapy.Request(url=next_url,callback=self.parse)

    def parse_info(self,response):
        item = response.meta['item']
        item['exp'] = response.xpath('.//div[@class="t1"]/span[@class="sp4"][1]/text()').extract_first()
        item['edu'] = response.xpath('.//div[@class="t1"]/span[@class="sp4"][2]/text()').extract_first()
        item['num'] = response.xpath('.//div[@class="t1"]/span[@class="sp4"][3]/text()').extract_first()
        item['info'] = response.xpath('string(.//div[@class="bmsg job_msg inbox"])').extract_first()
        yield item