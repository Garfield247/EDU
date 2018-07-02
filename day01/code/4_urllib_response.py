#导包
import urllib.request
# 定义URL，情求的页面的URL,数据类型为String
url = 'https://baike.baidu.com/item/python'
# 定义一个Header数据类型为Dict
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
# 构造情求
request = urllib.request.Request(url=url, headers=headers)
# 发送情求
response = urllib.request.urlopen(request)

print(response)
#响应二进制数据
print(response.read())
#相应的状态码
print(response.getcode())
#响应的头信息
print(response.getheaders())
#响应的URL
print(response.geturl())