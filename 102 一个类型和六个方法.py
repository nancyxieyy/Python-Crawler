# _*_ coding : utf-8 _*_
# @Time : 2023/8/4  03:23
# @Author : nancy_xieyy@icloud.com
# @File : 102 一个类型和六个方法
# @Project : Python

import urllib.request

# 1. 定义一个url 就是你要访问的地址
url = 'http://www.baidu.com'

# 2. 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

# 1. read() 一字节一字节去读
# content = response.read().decode('utf-8')

# 2. readline() 只能读取一行
# content = response.readline().decode('utf-8')

# 3. readlines() 读取行 直到结束
# content = response.readlines().decode('utf-8')

# 4. 返回状态码，如果是200则没错
# print(response.getcode())

# 5. 返回url地址
# print(response.geturl())

# 6. 返回状态信息
# print(response.getheaders())