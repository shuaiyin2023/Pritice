# import socket
#
# ip_port = ('127.0.0.1', 8081)
#
# s = socket.socket()     # 创建套接字
#
# s.connect(ip_port)      # 连接服务器
#
# while True:     # 通过一个死循环不断接收用户输入，并发送给服务器
#     inp = input("请输入要发送的信息： ").strip()
#     if not inp:     # 防止输入空信息，导致异常退出
#         continue
#     s.sendall(inp.encode())
#
#     if inp == "exit":   # 如果输入的是‘exit’，表示断开连接
#         print("结束通信！")
#         break
#
#     server_reply = s.recv(1024).decode()
#     print(server_reply)
#
# s.close()       # 关闭连接


""" 套接字--socket """

import socket
# 客户端
class ClientSocket:

    def __init__(self, address):
        # 1.创建套接字
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.连接服务器
        self.socket.connect(address)

    # 3.发送消息
    def send_msg(self, msg):
        self.socket.send(msg.encode('utf-8'))

    def recv_msg(self):
        print("接收来自服务端的响应: ", self.socket.recv(1024).decode('utf-8'))
        return self.socket.recv(1024).decode('utf-8')

    def __del__(self):
        self.socket.close()


if __name__ == '__main__':
    print("正在连接服务端···")
    address = ('127.0.0.1', 8081)
    client = ClientSocket(address)

    client.send_msg('hello')
    client.recv_msg()


