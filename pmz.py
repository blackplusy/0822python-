#!/usr/bin/env python
#需要提前安装
#sudo apt-get install python3-pip
#pip install bs4
#pip install lxml

import urllib.request
from bs4 import BeautifulSoup
 
def crawl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req, timeout=20)
    contents = page.read()
    soup = BeautifulSoup(contents)
    my_girl = soup.find_all('img')
    for girl in my_girl:
        link = girl.get('src')
        print(link)
        content2 = urllib.request.urlopen(link).read()
        with open(u'/home/heygor/test'+'/'+link[-11:],'wb') as code:
            code.write(content2)
page_start = 0
page_stop = 10
for page in range(page_start, page_stop):
    page += 1
    url = 'http://www.dbmeinv.com/?pager_offset=%s' % page
    crawl(url)
 
print("福利啊~~~像一颗海草海草~随风飘摇, MM图片下载完毕。！")
