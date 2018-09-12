#coding=utf-8
import socket
ip_port=('127.0.0.1',9999)

sk=socket.socket()
#连接address套接字，如果出错再说
sk.connect(ip_port) #我和哪个ip端口建立连接
sk.sendall(('server server im client!!!').encode())
server_reply=sk.recv(1024)
print(server_reply)
sk.close()
