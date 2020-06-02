"""
tcp_client
1. 创建套接字 socket
2. 建立连接 connect
3. 收发消息 send/recv 必须是字节串
4. 关闭套接字 close
"""
import socket
# 1. 创建套接字
sockfd = socket.socket()
# 2. 建立连接
server_addr = ("127.0.0.1", 12306)
sockfd.connect(server_addr)
while True:
    # 3. 收发消息
    data = input("data>>>")
    if data == "":
        break
    sockfd.send(data.encode())
    rev_data = sockfd.recv(1024)
    print("服务器说：", rev_data.decode())
# 4. 关闭套接字
sockfd.close()