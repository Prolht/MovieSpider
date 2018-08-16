# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_chi = scrapy.Field() #译名
    name_eng = scrapy.Field() #片名
    year = scrapy.Field()  #年代
    locate = scrapy.Field() #产地
    category = scrapy.Field() #类别
    subtitle = scrapy.Field()  #字幕
    date_sreen = scrapy.Field() #上映日期
    IMDb_count = scrapy.Field() #imdb评分
    Douban_count = scrapy.Field() #豆瓣评分
    movei_time = scrapy.Field() #电影片长
    #role = scrapy.Field() #主演
    intro = scrapy.Field() #简介
    url_info = scrapy.Field() #下载地址
    pass
