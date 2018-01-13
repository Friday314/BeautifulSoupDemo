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
                                        
  解 析 器                 使 用 方 法                          优  点                       缺   点

                                                            Python的内置标准             Python2.7.3 or
Python标准库       BeautifulSoup(markup, "html.parser")      库执行速度适中，文            Python3.2.2前的版本中
                                                            档空错能力强                  文档容错能力差
                                                        
lxml HTML解析器    BeautifulSoup(markup, "lxml")             速度快                      需要安装C语言库
                                                            容错能力强
                                                            
                                                            速度快
lxml XML解析器     BeautifulSoup(markup, ["lxml", "xml"])    唯一支持XML的                西药安装C语言库
                  BeautifulSoup(markup, "xml")              解析器
                                                        
                                                            最好的容错性
                                                            以浏览器的方式解              速度慢
html5lib          BeautifulSoup(markup, "html5lib")         析文档                       不依赖外部扩展
                                                            生成HTML5格式的
                                                            文档

"""


# 头文件
_headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# 请求访问
r = requests.get("http://bj.xiaozhu.com/", headers=_headers)

# 对返回的结果进行解析
# soup = BeautifulSoup(r.text, 'html.parser')     # Python标准库
soup = BeautifulSoup(r.text, 'lxml')        # BeautifulSoup库官方推荐使用lxml作为解析器，因为效率更高

print(soup.prettify())


""""

解析得到的soup文档可以使用find()和find_all()方法及selector()方法定位需要的元素了

语法：
    find_all(tag, attibutes, recursive, text, limit, keywords)
    find(tag, attibutes, recursive, text, keywords)
    
    soup.find_all('div', "item")    查找div标签，class="item"
    soup.find_all('div', class='item')
    soup.find_all('div', attrs={"class":"item"})    # attrs 参数定义一个字典参数来搜索包含特殊属性的tag
    
    find()方法与find_all()方法类似，只是find_all()方法返回的是文档中符合条件的所有tag，
    是一个集合(class 'bs4.element.ResultSet'),find()方法返回的一个Tag(class 'bs4.element.Tag')
    
    
    selector()方法
    
    soup.selector(#con_one_1 > span:nth-child(1) > a)   # 括号内容通过Chrome复制得到
    
    该方法类似与 中国 > 湖南省 > 长沙市，从大到小，提取需要的信息

"""
