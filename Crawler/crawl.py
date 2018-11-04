import random
import requests
import time
from logzero import logger
from collections import defaultdict
from util import random_agent
from bs4 import BeautifulSoup
import time
import random
import urllib
import json

SEARCH_ENGINE = {
    "google": "https://www.google.com/search?q={0}&start={1}",
    "baidu": "https://www.baidu.com/s?wd={0}&pn={1}&rsv_spt=1&rsv_iqid=0xd85735a30002d596&issp=1&f=8&rsv_bp=0&rsv_idx"
             "=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&inputT=3786"
             "&rsv_sug4=3786",
    "so": "https://www.so.com/s?q={0}&PN={1}"
}


class Crawl(object):

    def crawl(self, keywords, max_result=None):

        result = defaultdict(list)

        if max_result is None:
            max_result = 20

        max_search = int(max_result / 10)

        for key, val in SEARCH_ENGINE.items():
            for index in range(max_search):
                # 360 start with 1, not 10
                if key == "so":
                    url = val.format(keywords, index * 1)
                else:
                    url = val.format(keywords, index * 10)
                logger.info(url)

                user_agents = {
                    "user-agent": random_agent()
                }
                response = requests.get(url, headers=user_agents)

                # take a break after a request
                time.sleep(random.uniform(0, 3))

                if key == "google":
                    logger.info(response.content)
                    result[key] += self.parse_google_search(response.content)
                elif key == "baidu":
                    result[key] += self.parse_baidu_search(response.content)
                elif key == "so":
                    result[key] += self.parse_so_com_search(response.content)

        return self.data_converter(dict(result))

    # google search
    def parse_google_search(self, html_doc):
        data = []
        soup = BeautifulSoup(html_doc, 'html.parser')

        for page in soup.find_all('div', attrs={'id': 'res'}):
            items = page.find_all('a')
            for item in items:
                title = item.find_all('h3', attrs={'class': 'LC20lb'})
                if title:
                    title = title[0].get_text().strip()
                    url = item['href']
                    data.append({"title": title, "url": urllib.parse.unquote(url)})

        return data

    # baidu search
    def parse_baidu_search(self, html_doc):
        data = []
        soup = BeautifulSoup(html_doc, 'html.parser')

        for page in soup.select('div.result.c-container'):
            url = requests.head(page.find('a')['href']).headers['location']
            title = page.find('a').get_text()
            data.append({"title": title, "url": urllib.parse.unquote(url)})

        return data

    # 360 search
    def parse_so_com_search(self, html_doc):
        data = []
        soup = BeautifulSoup(html_doc, 'html.parser')

        for page in soup.select('li.res-list'):
            item = page.find('a')
            if 'www.so.com/link?' not in item['href']:
                url = item['href']
            elif item.get('data-url') is not None and 'www.so.com/link?' not in item['data-url']:
                url = item['data-url']
            elif item.get('data-cache'):
                url = item['data-cache']
            else:
                url = urllib.parse.unquote(item['href'][27:])
            title = item.get_text()
            data.append({"title": title, "url": urllib.parse.unquote(url)})

        return data

    def data_converter(self, data):
        result_list = []

        for key, val in data.items():
            for data in val:
                item = []
                item.append(data['title'])
                item.append(data['url'])
                item.append(key)
                result_list.append(item)

        return {"data": result_list}

if __name__ == '__main__':
    crawl = Crawl()
    print(crawl.crawl('虎扑'))
    
