import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

class Itmedia():
    def __init__(self, urls):
        self.urls = urls
        
    def geturl(self):
        all_text = []
        for url in self.urls:
            info = requests.get(url)
            # エラー確認
            # info.raise_for_status()
            # print(info.status_code)
            # ここまで
            soup = BeautifulSoup(info.text, 'lxml')
            article = soup.find_all('a' , limit=10)
            for title in article:
                mono_url = title.text
                link =  title.get('href')
                all_text.append([mono_url,link])
                sleep(0.5)
        return all_text
        
target = Itmedia(['https://www.itmedia.co.jp/'])
content = target.geturl()
print(content)