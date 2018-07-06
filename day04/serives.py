#coding=utf-8
import socket
bind_ip = "127.0.0.1"
bind_port = 7474

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)
try:
        while True:
                client,add = server.accept()
                while True:
                        data = client.recv(1024)
                        if not data:
                                break
                        print(data)
                        data = 'ok'
                        client.send(data)
#                       print data
                else:
                        client.close()
except Exception as e:
        print(e)
server.close()
