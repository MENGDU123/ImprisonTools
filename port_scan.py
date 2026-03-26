import socket
ipaddr = str(input("请输入目标IP地址："))
while True:
    try:
        port = int(input("请输入目标IP端口："))
        if port < 1 or port > 65535:
            print("非法的端口号")
            continue
        break
    except ValueError:
        print("类型错误!")

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect((ipaddr,port))
result = s.recv(1024)
s.close()
print(result)

