# 导入库
import requests
from bs4 import BeautifulSoup

# 请求头文件
_headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# 请求网页
r = requests.get("http://bj.xiaozhu.com/", headers=_headers)

# 解析数据
# soup = BeautifulSoup(r.text, "html.parser")
soup = BeautifulSoup(r.text, "lxml")

# 定位元素位置并通过selector()方法提取
price = soup.select("#page_list > ul > li:nth-of-type(1) > div.result_btm_con.lodgeunitname > span.result_price > i")

print(price)

# 提取全部短租房的价格，此时prices是一个列表
prices = soup.select("#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i")

# 遍历 prices
for p in prices:
    print(p.get_text())     # get.text() 方法获取文字信息，去除HTML标签
