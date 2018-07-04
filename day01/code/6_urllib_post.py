# _*_ coding:utf-8 _*_
#导包
import urllib.request
import urllib.parse
# 发送post情求的地址
url  = 'https://fanyi.baidu.com/v2transapi'
# 定义请求头
headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Content-Length': '119',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=B87A6EEFA29B7707B3C2524F563A191B; BAIDUID=DFD1ECA69799AE7AD46BC8C2EDE44726:FG=1; PSTM=1528289735; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1465_21105_18560_26350_20718; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1530517279,1530517303,1530518102; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1530518102; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
data = {
    'from': 'zh',
    'to': 'en',
    'query': '飞机',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '365372.94221',
    'token': '3bf1789b2f25fe6920fd0365fd9ae617',
}

data = urllib.parse.urlencode(data).encode('utf-8')
# 构造情求
request = urllib.request.Request(url=url, headers=headers,data=data)
# 发送情求
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))