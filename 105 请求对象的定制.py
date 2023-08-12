# _*_ coding : utf-8 _*_
# @Time : 2023/8/12  12:05
# @Author : nancy_xieyy@icloud.com
# @File : 105 请求对象的定制
# @Project : Python
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com'

# UA
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}

# 因为urlopen方法中不能存储字典 所以headers不能传递进去
# 请求对象的定制
# 参数顺序问题，不能直接写url和headers，中间还有一个data，所以需要关键字传参
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)