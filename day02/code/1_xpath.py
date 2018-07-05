from lxml import  etree

#读取html文件
fp = open('zhilian.html','r',encoding='utf-8')
html = fp.read()
fp.close()
xpath_obj = etree.HTML(html)

zwmcs = xpath_obj.xpath('//td[@class="zwmc"]')
print(zwmcs)
print(type(zwmcs))
for zwmc in zwmcs:
    print(zwmc)
    data = zwmc.xpath('.//div/a/text()')
    url = zwmc.xpath('.//div/a/@href')
    print(data)
    print(url)