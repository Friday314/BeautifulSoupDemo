# 导入库
import requests
from bs4 import BeautifulSoup

_headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

r = requests.get("http://bj.xiaozhu.com/", headers=_headers)

soup = BeautifulSoup(r.text, "html.parser")

price = soup.select("#page_list > ul > li:nth-of-type(1) > div.result_btm_con.lodgeunitname > span.result_price > i")

print(price)
