# _*_encoding=utf-8_*_
from lxml import  etree
#读取html文件
fp = open('test.html','r',encoding='utf-8')
html = fp.read()
fp.close()
xpath_obj = etree.HTML(html)

# res = xpath_obj.xpath('.//div[@id="a"]/div[@class="b"]/a[2]/text()')

# res = xpath_obj.xpath('.//div[@class="c" and @id="d"]/text()')


res1 = xpath_obj.xpath('.//div[contains(@class,"he")]/text()')
res2 = xpath_obj.xpath('.//div[starts-with(@class,"he")]/text()')
res3 = xpath_obj.xpath('.//div[ends-with(@class,"he")]/text()')

print(res1)