#coding:utf-8
import requests
class HtmlDownloader(object):

    def downloader(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url,headers)
        if r.status_code ==200:
            r.encoding='utf-8'
            return r.text
        return None


if __name__=='__main__':
    hd = HtmlDownloader()
    heml = hd.downloader('http://www.baidu.com')
    print heml
