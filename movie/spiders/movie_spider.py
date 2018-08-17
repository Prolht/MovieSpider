# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
import re
from movie.items import MovieItem

class movieSpider(CrawlSpider):
    name = 'movie_spider'
    allowed_domains = ["dytt8.net"]
    # 爬取最新电影栏目
    # list_23_1 1表示第几页（共177页）
    start_urls = ["http://www.dytt8.net"]
    rules = (
        # 定义是否进行深度爬取
        # Rule(LinkExtractor(allow=('',), deny=('subsection\.php',))),
        # 当符合/html/gndy/dyzz/\d+$/\d+$.html这个形式，则进行深度爬取，
        Rule(LinkExtractor(allow=(r'/html/gndy/dyzz/\d{8}/\d+.html',)), callback='parse_movie'),
    )

    def parse_movie(self, response):
        print('开始爬取%s'%response.url)
        #data = response.body.decode('gb2312')
        print('here')
        #a=response.xpath('//*[@id="Zoom"]/span/p[1]/br[4]/text()').extract()
        a=response.xpath('//*[@id="Zoom"]/span/p[1]/text()').extract()
        print(a)
        item = MovieItem()
        ''''
        item['name_chi'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[4]/text()').extract()[6:] # 译名
        item['name_eng'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[5]/text()').extract()[6:]  # 片名
        item['year'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[6]').re(r'\d+)')  # 年代
        item['locate'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[7]').extract()[6:]  # 产地
        item['category'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[8]').extract()[6:]  # 类别
        item['subtitle'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[9]').extract()[6:] # 字幕
        item['date_sreen'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[10]').extract()[6:]  # 上映日期
        item['IMDb_count'] = response.xpath('//*[@id="Zoom"]/span/p[1]br[11]').extract()[8:]  # imdb评分
        item['Douban_count'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[12]').extract()[6:] # 豆瓣评分
        item['movei_time'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[17]').re(r'(\d+)')  # 电影片长
        #item['role'] = response.xpath('//*[@id="Zoom"]').re(r'ID: (\d+)')  # 主演
        item['intro'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[33]').re(r'ID: (\d+)')  # 简介
        item['url_info'] = response.xpath('//*[@id="Zoom"]/span/table/tbody/tr/td/a').extract()  # 下载地址
        '''
        return item
    def closed(self, reason):
        self.logger.info('movie_stopped'+ reason)