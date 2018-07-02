#导包
import urllib.request
#定义URL，情求的页面的URL,数据类型为String
url = 'https://www.baidu.com/'
#定义一个Header数据类型为Dict
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
#构建情求
r0 = urllib.request.urlopen(url=url)

#添加Headers的方式有两种
#第一种
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
#第二种
# r2 = urllib.request.Request(url)
# r2.add_header(headers)
# r3 = urllib.request.urlopen(r2)


#获取相应
print(response.read())

# #将相应的内容写到文件
with open('baidu.html','wb') as fp:
    fp.write(response.read())