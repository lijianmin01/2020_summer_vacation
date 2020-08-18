import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}

url = "https://wenku.baidu.com/view/408c19d7a48da0116c175f0e7cd184254b351be1.html?fr=search"

# 获取页面
source_html = None
try:
    response = requests.get(url, headers=headers)
    source_html = response.content
except Exception as e:
        print(e)

# 解析源码
content = source_html.decode('UTF-8')
# print(content)
pattern = re.compile('<title>(.*?)</title>',re.S)
title = re.findall(pattern, content)
print(title[0])
