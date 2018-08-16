# -*- coding:utf-8 -*-
import scrapy
from scrapy.spider import Rule
from scrapy.linkextractors import LinkExtractor
import re
from movie.items import MovieItem

class movieSpider(scrapy.Spider):
    name = 'movie_spider'
    allowed_domains = ["dytt8.net"]
    rules =(
        #定义是否进行深度爬取
        #Rule(LinkExtractor(allow=('',), deny=('subsection\.php',))),
        # 当符合/html/gndy/dyzz/\d+$/\d+$.html这个形式，则进行深度爬取，
        Rule(LinkExtractor(allow=('/html/gndy/dyzz/\d+$/\d+$.html',)), callback='parse_movie'),
    )
    urls = []
    # 爬取最新电影栏目
    # list_23_1 1表示第几页（共177页）
    init_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_%s.html"
    for i in range(1, 7):  #178
        urls.append(init_url % str(i))
    start_urls = urls

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

    def parse_movie(self, response):
        item = MovieItem()
        item['name_chi'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[4]').extract()[6:] # 译名
        item['name_eng'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[5]').extract()[6:]  # 片名
        item['year'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[6]').re(r'\d+)')  # 年代
        item['locate'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[7]').extract()[6:]  # 产地
        item['category'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[8]').extract()[6:]  # 类别
        item['subtitle'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[9]').extract()[6:] # 字幕
        item['date_sreen'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[10]').extract()[6:]  # 上映日期
        item['IMDb_count'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[11]').extract()[8:]  # imdb评分
        item['Douban_count'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[12]').extract()[6:] # 豆瓣评分
        item['movei_time'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[17]').re(r'(\d+)')  # 电影片长
        #item['role'] = response.xpath('//*[@id="Zoom"]').re(r'ID: (\d+)')  # 主演
        item['intro'] = response.xpath('//*[@id="Zoom"]/span/p[1]/br[33]').re(r'ID: (\d+)')  # 简介
        item['url_info'] = response.xpath('//*[@id="Zoom"]/span/table/tbody/tr/td/a').extract()  # 下载地址
        return item
    def closed(self, reason):
        self.logger.info('movie_stopped'+ reason)