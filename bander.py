"""
此段代码用于扫描目标主机是否存在vsftp2.3.4。
当然，即便没有vsftp2.3.4也可以用于扫描端口。
"""
import socket
import time
from ping3 import ping

socket.setdefaulttimeout(2)
ipaddr = ""
bander = ""
ip_list = [] #用于写入IP地址
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

def ipv4_test_1(__ipaddr__):
    #检查地址是否为点分十进制
    parts = __ipaddr__.split(".")
    if len(parts) != 4:
        print("IP地址不合法，正确的形式应为‘x.x.x.x’!")
        return False
    return True

def ipv4_test_2(__ipaddr__):
    #检查地址是否符合IPv4范围
    parts = __ipaddr__.split(".")
    for part in parts:
        if not part.isdigit():
            print("IP地址不合法！正确的范围应为（0~255.0~255.0~255.0~255）")
            return False
        if int(part) > 255 or int(part) < 0:
            print("IP地址不合法！正确的范围应为（0~255.0~255.0~255.0~255）")
            return False
    return True


def read_ip():
    if input("需要使用配置文件吗？（Y）") == "Y":
        try:
            f = open("ip.txt", "r")
        except FileNotFoundError as __e:
            print(f"发生错误,ip.txt文件不存在！{__e}")
            exit(-1)
        for _ in f.readlines():
            addr= _.strip("\n")
            print()
            print(f"正在检查{addr}")
            if not ipv4_test_1(addr):
                print(f"忽略{addr}")
                continue
            if not ipv4_test_2(addr):
                print(f"忽略{addr}")
                continue
            print(f"已添加{addr}")
            ip_list.append(addr)
            print(f"即将被使用的地址：{ip_list}")
            time.sleep(0.5)
        return True
    else:
        return False


if __name__ == "__main__":
    if not read_ip():
        while True:
            ipaddr = str(input("IP:"))
            #用于检查IP是否合法。
            if not ipv4_test_1(ipaddr):
                continue
            if not ipv4_test_2(ipaddr):
                continue

            if ping(ipaddr,timeout=2) is not None:
                pass
            else:
                ack = input("尝试ping主机失败，如果要继续请输入Y：")
                if 'Y' in ack:
                    pass
                else:
                    print("已忽略当前输入的IP。")
                    print(f"当前已被添加的地址：{ip_list}")
                    continue

            ip_list.append(ipaddr)

            ack = input("需要继续添加IP地址吗？（Y）")
            if 'Y' in ack:
                print(f"当前已被添加的地址：{ip_list}")
                continue
            else:
                print(f"即将被使用的地址：{ip_list}")
                break

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

    for ipaddr in ip_list:
        i = 0
        for i in range(3):
            try:
                s = socket.socket()
                print(f"开始第{i + 1}次尝试。")
                bander = s_content(2,ipaddr,port)
                break

            except socket.timeout:
                print(f"连接{ipaddr}:{port}超时！")
                continue
            except Exception as e:
                print(f"连接{ipaddr}:{port}时发生错误:",e)
                continue

        print(f"{ipaddr}:{port}结束!")
        print()

    exit(0)

