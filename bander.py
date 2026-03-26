"""
此段代码用于扫描目标主机是否存在vsftp2.3.4。
当然，即便没有vsftp2.3.4也可以用于扫描端口。
"""
import socket
from ping3 import ping

socket.setdefaulttimeout(2)
ipaddr = ""
bander = ""
port = 0

def s_content(overtime,__ipaddr__,__port__):
    """socket连接"""
    s.settimeout(overtime)
    s.connect((__ipaddr__, __port__))
    result = s.recv(1024)
    s.close()
    banner = str(result.decode())
    print(banner)
    return banner

def bander_test(__bander__):
    if str("2.3.4") in __bander__:
        print(ipaddr,"存在vsftp漏洞！")
    else:
        print(ipaddr,"未扫描到漏洞！")

if __name__ == "__main__":
    while True:
        ipaddr = str(input("IP:"))
        #用于检查IP是否合法。
        parts = ipaddr.split(".")
        if len(parts) != 4:
            print("IP地址不合法，正确的形式应为‘x.x.x.x’!")
            continue

        valid = True
        for part in parts:
            if not part.isdigit():
                valid = False
                break
            if int(part) > 255 or int(part) < 0:
                valid = False
                break
        if valid:
            break
        else:
            print("IP地址不合法！请输入正确的地址（0~255.0~255.0~255.0~255）")
            continue

    if ping(ipaddr,timeout=2) is not None:
        pass
    else:
        ack = input("尝试ping主机失败，如果要继续请输入Y：")
        if 'Y' in ack:
            pass
        else:
            print("程序终止。")
            exit(-1)

    while True:
        try:
            port = int(input("PORT:"))
            if port < 0 or port > 65535:
                print("非法的端口号！")
                continue
            else:
                break
        except ValueError:
            print("请输入正确的端口号！")
            continue

    for i in range(4):
        try:
            s = socket.socket()
            if i + 1 == 4:
                print("已达最大尝试次数,程序终止!")
                exit(-1)
            print(f"开始第{i + 1}次尝试。")
            bander = s_content(2,ipaddr,port)
            break

        except socket.timeout:
            print(f"连接{ipaddr}:{port}超时！")
            continue
        except Exception as e:
            print(f"连接{ipaddr}:{port}时发生错误:",e)
            continue

    bander_test(bander)
    exit(0)

