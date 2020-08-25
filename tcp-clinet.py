import socket
host = '127.0.0.1'
port = 8080
s =socket.socket()
s.connect((host,port))
send_data= input("请输入要发送的数据")
s.send(send_data.encode())
recv_data = s.recv(1024).decode()
print("接收到数据： ",recv_data)
s.close()

