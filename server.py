import socket
host = '127.0.0.1'
port = 8080
web =socket.socket()
web.bind((host,port))
web.listen(5)
print("等待连接")
while True:
    conn,addr = web.accept()
    data = conn.recv(1024)
    print("接收到数据： ",data)
    #服务器发给请求方的数据。
    conn.sendall(b'http/1.1 200 OK \r\n\r\nhello world')
    conn.close()

