#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return FTChinese

class FTChinese(BaseFeedBook):
    title                 = u'FT中文网'
    description           = u'英国《金融时报》集团旗下唯一的中文商业财经网站。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_ftchinese.gif"
    coverfile             = "cv_ftchinese.jpg"
    oldest_article        = 1
    
    feeds = [
            (u'马丁 沃尔夫', 'http://www.ftchinese.com/rss/column/007000012'),
            (u'十大热门文章', 'http://www.ftchinese.com/rss/hotstoryby7day'),
            (u'今日焦点', 'http://www.ftchinese.com/rss/news'),
            ]
    
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
