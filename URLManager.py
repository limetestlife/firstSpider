#coding:utf-8
class URLManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取URL集合
        self.old_urls = set()  # 已爬取URL集合

    #向urlManager中添加新的url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            return self.new_urls.add(url)

    # 向urlManager中添加新的url集合
    def add_new_urls(self,urls):
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)

    #再urlManager拿一个没有爬过的连接
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    #询问管理器是否还有未爬的连接
    def has_new_url(self):
        return self.new_url_size() !=0

    #询问管理器没有爬取的连接数
    def new_url_size(self):
        return len(self.new_urls)

    #询问管理器爬取过的连接数
    def old_url_size(self):
        return len(self.old_urls)

