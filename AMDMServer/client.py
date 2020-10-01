from socket import * 

ip = "127.0.0.1"
port = 12345

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((ip,port))

print("서버 연결완료")

clientSocket.send("I am client".encode("utf-8"))
print("전송완료")

data = clientSocket.recv(1024)

print("받은 데이터 : ",data.decode("utf-8"))

clientSocket.close();
