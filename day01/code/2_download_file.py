# _*_ coding:utf-8 _*_
import urllib.request
#图片的url
img_url  = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1530514853459&di=6ec34b92fb03f9e3a83e601920869c69&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Fbf096b63f6246b60553a62a0e1f81a4c510fa22a.jpg'
# 指定文件名
filename = '风景.jpg'
#下载图片
urllib.request.urlretrieve(img_url, filename)