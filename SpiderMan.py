#coding:utf-8
from URLManager import URLManager
from HtmlDownloader import HtmlDownloader
from DataOutput import DataOutput
from HtmlParser import HtmlParser
class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downoloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                print '开始爬取'
                new_url = self.manager.get_new_url()#向url管理器获取连接
                html = self.downoloader.downloader(new_url)#下载页面

                print "已经抓取%s个链接" % self.manager.old_url_size()
            except Exception,e:
                print "爬取失败"










if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
