# requests库导入
import requests
# BeautifulSoup库导入，这个导入比较奇怪
from bs4 import BeautifulSoup

"""
Requests库请求返回的网页源码，但通过BeautifulSoup库解析得到的Soup文档按照标准缩进格式输出，为结构化的数据，
为数据的过滤提取做好准备
"""

"""
BeautifulSoup库解析器

                                                            Python的内置标准             Python2.7.3 or
Python标准库       BeautifulSoup(markup, "html.parser")      库执行速度适中，文            Python3.2.2前的版本中
                                                            档空错能力强                  文档容错能力差
                                                        
lxml HTML解析器    BeautifulSoup(markup, "lxml")             速度快                      需要安装C语言库
                                                            容错能力强
                                                        
"""


# 头文件
_headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# 请求访问
r = requests.get("http://bj.xiaozhu.com/", headers=_headers)

# 对返回的结果进行解析
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())