# _*_ coding : utf-8 _*_
# @Time : 2023/8/12  12:29
# @Author : nancy_xieyy@icloud.com
# @File : 106 get请求的quote方法
# @Project : Python

# http://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# 需求 获取 https://www.baidu.com/s?wd=周杰伦 的网页源码
import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?wd='

# 请求对象的定制是为了解决反爬的第一种手段
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# 将周杰伦变成unicode编码的格式
# 需要依赖urllib.parse
name = urllib.parse.quote('周杰伦')
url = url + name

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的内容
content = response.read().decode('utf-8')

# 打印数据
print(content)