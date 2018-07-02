import urllib.parse as up

url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E9%A3%8E%E6%99%AF'
#url编码
print(up.quote('风景'))
#URL解码
print(up.unquote('%E9%A3%8E%E6%99%AF'))
print(up.unquote(url))