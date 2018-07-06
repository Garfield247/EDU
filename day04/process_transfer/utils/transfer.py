import os
import socket
from datetime import datetime
from utils.config import FLUME_HOST,FLUME_PORT

class Transfer(object):
    def __init__(self):
        self.host = FLUME_HOST
        self.port = FLUME_PORT

    # 与Flume服务器建立连接
    def gen_connect(self):
        conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn.connect((self.host,self.port))
        return conn

    # 发送数据
    def send_item(self,conn,item):
        send_data = str(item + '\n')
        conn.sendall(bytes(send_data, encoding="utf8"))
        conn.recv(1024*1024)



