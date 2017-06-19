#coding:utf-8
import re

from bs4 import BeautifulSoup
class HtmlParser(object):
    def parser(self,page_url,html_cont):
        if page_url is None:
            return
        soup = BeautifulSoup(page_url,'html.parser',from_encoding='utf-8')
        new_urls = soup._get_new_url()

    def _get_new_urls(self,page_url,soup):
        new_urls =set()
        links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']

    def _get_new_data(self,page_url,soup):

        return

