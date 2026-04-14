"""
对一组IP地址的特点端口进行扫描。
"""
import os
import socket
import time
import sys
import threading
from ping3 import ping


socket.setdefaulttimeout(2)
ipaddr = ""
bander = ""
ip_list = [] #用于写入IP地址
port = 0
mode = 0 #判断是否为命令行模式。
filepath = None

def s_content(overtime,__ipaddr__,__port__):
    """socket连接"""
    try:
        s = socket.socket()
        s.settimeout(overtime)
        s.connect((__ipaddr__, __port__))
        result = s.recv(1024)
        s.close()
        banner = str(result.decode())
        print(__ipaddr__,banner,sep=':')
        return banner
    except Exception as e:
        return None

def ipv4_test_1(__ipaddr__):
    #检查地址是否为点分十进制
    parts = __ipaddr__.split(".")
    if len(parts) != 4:
        print("IP地址不合法，正确的形式应为‘x.x.x.x’!")
        return False
    return True

def ipv4_test_2(__ipaddr__):
    #检查地址是否符合IPv4范围（非网络地址或者广播）
    parts = __ipaddr__.split(".")
    for part in parts:
        if not part.isdigit():
            print("IP地址不合法！正确的范围应为（1~254.1~254.1~254.1~254）")
            return False
        if int(part) > 254 or int(part) < 0:
            print("IP地址不合法！正确的范围应为（0~254.0~254.0~254.0~254）")
            return False
    return True


def read_ip(__filepath__):
        if not os.path.exists(__filepath__):
            print(__filepath__,"没有这个文件或者文件无法打开!")
            sys.exit(-1)
        else:
            f = open(__filepath__, "r")

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



if __name__ == "__main__":
    if len(sys.argv) == 2:
        mode = 1
        ipaddr = sys.argv[1]
        if ipv4_test_1(ipaddr) and ipv4_test_2(ipaddr):
            ip_list.append(ipaddr)
            print(f"使用命令行参数中的 IP：{ipaddr}")
        else:
            read_ip(sys.argv[1])



    if mode != 1:    #如果不是命令行模式，再按照下面流程走。
        if input("需要使用配置文件吗？（Y）") == "Y":
            filepath = input("请输入列表路径:")
            read_ip(filepath)
        else:
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

    threads = []

    for ipaddr in ip_list:
        try:
            print(f"开始尝试连接{ipaddr}:{port}。")
            thread = threading.Thread(target=s_content, args=(2, ipaddr, port))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        except Exception as e:
            print(f"连接{ipaddr}:{port}时发生错误:",e)

    for thread in threads:
        thread.join(timeout=3)

    for ipaddr in ip_list:
        print(f"{ipaddr}:{port}结束!")
        print()


    sys.exit(0)
