# _*_ coding:utf-8 _*_
import re
import os
import time
import urllib.request
import urllib.parse

list1 = ['猫','狗','汽车','飞机']


def download_img(keyword):
    #d定义URL
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&word=%s'%keyword
    #定义请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    #构造情求
    request = urllib.request.Request(url=url, headers=headers)
    #发送情求
    response = urllib.request.urlopen(request)
    #拿到响应的HTML数据
    # print(response.read())
    html = response.read().decode('UTF-8')
    # print(html)
    #使用正则表达式提取图片url，得到的是list
    res = re.findall(r'"middleURL":"(.*?)"',html)
    # 将list进行set在变回list就会去除掉重复的元素
    img_urls = list(set(res))
    print(img_urls)
    print(len(img_urls))
    #遍历图片url的list
    for img_url in img_urls:
        print(img_url)
        #构造图片文件名
        filename = '%s-%d.jpg'%(urllib.parse.unquote(keyword),img_urls.index(img_url))
        # 指定图片存放路径
        base_dir = r'./images'
        # 将路径与文件名拼接
        img_path = os.path.join(base_dir,filename)
        # try-except语句：当执行的try下的语句报错时，程序不会终止而会执行except下的语句
        try:
            # 下载图片
            urllib.request.urlretrieve(img_url, img_path)
            # 添加下载图片的延时（0.5秒）
            time.sleep(0.5)
        except:
            #continue跳出本次循环执行下一次
            continue
# 遍历关键字
for kw in list1:
    # 对关键字进行url编码
    new_kw = urllib.parse.quote(kw)
    # 调用图片下载的函数，传参为url编码后的关键字
    download_img(new_kw)