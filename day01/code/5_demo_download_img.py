# _*_ coding:utf-8 _*_
import re
import os
import time
import urllib.request
import urllib.parse

list1 = ['猫','狗','汽车','飞机']


def download_img(keyword):
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&word=%s'%keyword

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    # print(response.read())
    html = response.read().decode('UTF-8')
    # print(html)
    img_urls = list(set(re.findall(r'"middleURL":"(.*?)"',html)))# 将list进行set在变回list就会去除掉重复的元素
    print(img_urls)
    print(len(img_urls))
    for img_url in img_urls:
        print(img_url)
        filename = '%s-%d.jpg'%(urllib.parse.unquote(keyword),img_urls.index(img_url))
        base_dir = r'./images'
        img_path = os.path.join(base_dir,filename)
        try:
            urllib.request.urlretrieve(img_url, img_path)
            time.sleep(0.5)
        except:
            continue

for kw in list1:
    new_kw = urllib.parse.quote(kw)
    # print(new_kw)
    # print('正在下载%s的图片')%str(kw)
    download_img(new_kw)