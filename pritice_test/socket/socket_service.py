import socket
# import threading
#
# ip_port = ('127.0.0.1', 8081)
# sk = socket.socket()  # 创建套接字
# sk.bind(ip_port)  # 绑定服务地址
# sk.listen(5)  # 监听连接请求
#
# print("启动socket服务，等待客户端连接···")
#
#
# def threading_service(conn, addr):
#     while True:
#
#         client_data = conn.recv(1024).decode()  # 接收客户端的数据
#         if client_data == "exit":  # 如果是exit，就关闭连接
#             exit("通信结束")
#         print(f"来自客户端{addr}的数据: {client_data}")
#         conn.sendall(f"服务端已经收到你的消息{addr}".encode())  # 相应客户端
#
#     conn.close()  # 关闭连接
#
#
# while True:
#     connection, address = sk.accept()  # 等待连接，此处自动阻塞
#     thread = threading.Thread(target=threading_service, args=(connection, address))
#     thread.start()


class ServiceSocket:

    def __init__(self, address):
        # 1.创建套接字
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2.绑定ip地址和端口号
        self.sock.bind(address)

        # 3.使用listen可变成被动链接
        self.sock.listen()

        # 4.等待连接
        self.conn, self.addr = self.sock.accept()

    # 5.接收客户端信息
    def recv_msg(self):
        data = self.conn.recv(1024)
        print("接收到的客户端{}，信息内容为{}".format(self.addr, data))

        # 6.响应客户端请求
        self.conn.send("我已经接收到你的消息了，靓仔".encode("utf-8"))

    # 7.关闭连接
    def __del__(self):
        self.sock.close()


if __name__ == '__main__':
    print("等待客户端连接···")
    address = ('127.0.0.1', 8081)

    s = ServiceSocket(address)
    s.recv_msg()
