# _*_ coding : utf-8 _*_
# @Time : 2023/8/12  13:03
# @Author : nancy_xieyy@icloud.com
# @File : 107 get请求方式urlencode方法
# @Project : Python

# urlencode应用场景：多个参数的时候
# https://www.baidu.com/s?wd=周杰伦&sex=男
import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取网页源码
base_url = 'https://www.baidu.com/s?'

headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + new_data

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的内容
content = response.read().decode('utf-8')

# 打印数据
print(content)