# _*_ coding : utf-8 _*_
# @Time : 2023/8/4  03:13
# @Author : nancy_xieyy@icloud.com
# @File : 101 urllib的基本使用
# @Project : Python
# 使用urllib来获取百度首页的源码

import urllib.request

# 1. 定义一个url 就是你要访问的地址
url = 'http://www.baidu.com'

# 2. 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3. 获取响应中页面的源码
# read方法 返回的时字节形式的二进制数据
# 解码decode('编码格式')： 将二进制的数据转换成字符串
content = response.read().decode('utf-8')

# 4. 打印数据
print(content)
