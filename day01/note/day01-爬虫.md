# day01-爬虫

## 1、爬虫概念
### 什么是爬虫

```
生活角度：
	爬虫，蜘蛛（spider），网
互联网
	网：互联网，上面的节点就是很多的url（统一资源定位符）
互联网爬虫：
	就是写一个程序，就是根据url用来爬取网页，然后将网页中的你所需要的数据提取出来都有哪些语言可以实现爬虫
```
### 用什么爬虫

```
php：号称是世界最优美的语言，但是他不是很擅长这个，对多进程多线程支持的不好
java：做起来也非常的不错，是python爬虫最主要的对手，代码太臃肿，代码量很大，重构成本非常的大，而我们爬虫需要根据需求经常修改，所以它不好
c、c++：学习成本比较高，性能和效率非常高，没这么做的，仅仅是一个能力的体现
python：好，语法优美、代码简单，学习成本低，支持的模块多，有一个非常强大的爬虫框架，scrapy
```
### 通用爬虫和聚焦爬虫概念

```
通用爬虫：百度、360、谷歌、搜狗、必应等搜索引擎
搜索引擎使用的爬虫就是通用爬虫
	（1）抓取网页
	（2）抓取数据
	（3）数据存储
	（4）数据处理
	（5）给你提供了检索服务
	抓取流程：
	（1）给一些起始的url，放入待爬取url队列
	（2）从队列中取出url，开始爬取
	（3）分析内容，获取网页中所有的url，继续执行第二步，直到结束
	搜索引擎如何获取一个新的网站的链接
	（1）主动给搜索引擎提交url
	（2）在其它网站中设置友情链接
	（3）百度和DNS服务商进行合作，加速收录新网站
	robots协议
	淘宝就不让百度抓取
	可以限制通用爬虫的抓取，哪些可以抓，哪些不能抓
	仅仅是一个协议，一般情况只有大型搜索引擎遵从这个协议，你自己写的小爬虫，就算了，你可以随便抓取
	网站排名（SEO）
	（1）根据pagerank值排名，根据流量、点击率等等进行综合的计算进行排名，值越高，排名越靠前
	（2）百度竞价排名，谁给的钱多，谁在最前面
	缺点：
	（1）抓取的很多数据都是无用的
	（2）不能根据用户的需求来抓取对应的数据
聚焦爬虫
	根据自己的需求，去写一个网络爬虫程序，抓取对应的数据即可
```
爬虫如何抓取网页数据

```
网页都有特点：
	（1）网页都有自己的唯一的统一资源定位符（url）
	（2）网页都是有html组成的
	（3）传输协议使用的都是http、https协议
爬虫设计的思路是：
	（1）给我一个url
	（2）模拟浏览器通过http协议访问url，获取到这个url的html代码
	（3）解析字符串（根据一定规则提取你所需要的数据）
开发环境：
	windows   后续会涉及到linux里面  CentOS  Ubuntu
	python3.6
	sublime   pycharm
整体内容：
	1、python语法
	2、如何抓取页面，使用到python库
		urllib.reqeust  urllib.parse  requests
	3、解析内容
		正则表达式、xpath、bs4、jsonpath
	4、采集动态html
		selenium+phantomjs
	5、scrapy
		高性能异步网络框架
	6、分布式，scrapy-redis组件
		在scrapy的基础上增了一套组件，结合redis进行存储等功能
	7、爬虫-反爬虫-反反爬虫之间的博弈过程
		其实爬虫到最后，让你头疼的不是复杂的界面，不是数据的提取，而是和对面相互博弈的过程
		反爬虫的一般手段：
			User-Agent、代理、验证码、动态数据加载、数据加密
		最终肯定能获取数据，公司值不值得，因为只要浏览器能够正常访问，那么数据就能拿到
```
## 2、http协议

	http就是应用层的协议，https
	http：明文传输   80
	https：加密传输  443 
	ftp：21
	ssh：22
	mysql：3306
	redis：6379
	MongoDB：27017
	http工作原理：
		url详解：
		http://www.taobao.com:80/index.html?username=goudan&password=123#anchor
		协议   主机           端口号  路径  query-string（参数）         锚点
		一张网页的程序有至少10-20个请求，每一个css、js、图片都是一个http请求
		浏览器就会将html、css、js、img翻译成图文并茂的形式
	http请求和响应
		请求行、请求头、请求体
			get、post
		响应行、响应头、响应体
	请求头
		发送请求的时候，告诉服务器可以接受那些内容，MIME
		Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
	
		客户端可以接受的编码类型
		Accept-Encoding:gzip, deflate, br
	
		接受的语言类型
		Accept-Language:zh-CN,zh;q=0.9
	
		和缓存相关
		Cache-Control:max-age=0
	
		连接方式，保持长连接
		Connection:keep-alive
	
		会话相关
		Cookie:BIDUPSID=9F5816DD3088F4291EA4C12FFC2ABCDE; BAIDUID=78AF1CE91C8F84BD601F6E2778C618DA:FG=1; PSTM=1513827071; BD_UPN=12314353; H_PS_PSSID=1454_21125_18559_25177; BD_CK_SAM=1; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=769396736; pgv_si=s5038345216; BD_HOME=0; H_PS_645EC=3ff96rRFDTjHDZ%2BqFcj5%2FYOP6KISjZyhvnS1a%2B1q4A19NgE%2FSjllKIn8ejA
	
		主机
		Host:www.baidu.com
	
		是否升级为https请求
		Upgrade-Insecure-Requests:1
	
		客户端浏览器类型
		User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
	
		如果是ajax请求，一般都带这个
		X-Requested-With: XMLHttpRequest
	
		上一个页面，你从哪个页面过来的
		Referer: https://www.baidu.com/?tn=57095150_6_oem_dg
	
	​``` 响应头信息 ```
		Connection:Keep-Alive
	
		内容编码格式
		Content-Encoding:gzip
		内容类型
		Content-Type:text/html; charset=utf-8
	
		时间
		Date:Sun, 24 Dec 2017 04:21:28 GMT
		过期时间
		Expires:Sun, 24 Dec 2017 04:20:29 GMT
		服务器版本
		Server:BWS/1.1
		给客户端保存的cookie值
		Set-Cookie:BDSVRTM=0; path=/
		Set-Cookie:BD_HOME=0; path=/
		Set-Cookie:H_PS_PSSID=1454_21125_18559_25177; path=/; domain=.baidu.com
	
		内容是否分块传输
		Transfer-Encoding:chunked
	常见的http状态码
		看文档
## 3、环境准备

	windows  python3.6  Pycharm
## 4、fiddler

	fiddler就是一个抓包工具
	谷歌浏览器开发者工具：抓包工具
## 5、urllib

	是一个库，是一个模块，python为我们提供的操作url的模块
	2系列的有urllib和urllib2
	3系列的只有urllib，
		urllib.request:发送请求和获取响应
			urllib.request.urlopen(url, data)
				友情提醒1：py程序爬取网页时，首先将fiddler关闭
				友情提醒2：网址要写全，http://www.baidu.com/,最后一个斜线不要忘记
			如果有data，那么说明这个请求是post请求，需要带data过去，如果没有data，就是get请求，需要将参数拼接到url的后面
			urllib.request.urlretrieve(url, filename)
				下载网页或者图片
		urllib.parse：处理url的
			urllib.parse.urlencode()  下面将post请求再来说这个函数
			urllib.parse.quote() 
				url编码 ，在url中只能出现-_.a-z  中文
				http://www.baidu.com?username=小明&password=123
	
				url编解码查看网页
				http://tool.chinaz.com/tools/urlencode.aspx
			urllib.parse.unquote() 
				url解码
		response对象
			read():读取的是二进制数据
			字符串类型和字节类型
				字符串-》字节：编码  encode()
				字节-》字符串：解码  decode()
			readline():读取一行
			readlines()：读取全部，返回一个列表
			getcode()：状态码
			geturl()：获取url
			getheaders():响应头信息，列表里面有元组
## 6、构建请求对象

	高级的请求，可以定制请求头信息，比如User-Agent
	在线解析本地浏览器的UA
	http://www.atool.org/useragent.php
	
	request = urllib.request.Request(url=url, headers=headers, data=data)
	response = urllib.request.urlopen(request)
	另外一种方式
	add_header(key, val)

## 7.DEMO(爬取百度图片)

```
见代码
```

## 8.练习

```
仿照爬百度图片案例爬取天堂图片网
http://www.ivsky.com/
```




​	