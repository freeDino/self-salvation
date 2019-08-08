import json
import requests
from requests.exceptions import RequestException
import re
import time


def get_one_page(url):
    try:
        headers = {
            'Host': 'cuiqingcai.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None

def parse_one_page(html):
    pattern = re.compile(r'<a target="_blank" href="(.*)" title="\[Python3网络爬虫开发实战\](.*)".*</a></h2>')
    #print('pattern = ' + str(pattern))
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'href': item[0],
            'title': item[1]
        }

        
def write_to_file(content):
    with open(r'D:\work\WeChat\pythonStudy\result1.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')	
	
def main(offset):
    url = 'https://cuiqingcai.com/category/technique/python/page/' + str(offset)
    html = get_one_page(url)
    #print(html)
    parse_one_page(html)
    for item in parse_one_page(html):
        write_to_file(item)
        #print(item)
	
if __name__ == '__main__':
    for i in range(16):
        main(offset=i)
        time.sleep(1)
