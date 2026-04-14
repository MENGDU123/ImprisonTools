from main import ipv4_test_1, ipv4_test_2, read_ip, s_content
import sys
from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip_list", action="append",help="指定要扫描的IP地址")
    parser.add_option("-p", "--port", dest="port", type="int",help="指定要扫描的端口号")
    (options, args) = parser.parse_args()

    if not options.ip_list:
        print("错误：请使用 -i 指定至少一个IP地址")
        parser.print_help()
        sys.exit(1)

    if not options.port:
        print("错误：请使用 -p 指定端口号")
        parser.print_help()
        sys.exit(1)

    valid_ips = []
    for ipaddr in options.ip_list:
        if ipv4_test_1(ipaddr) and ipv4_test_2(ipaddr):
            valid_ips.append(ipaddr)
            print(f"使用命令行参数中的 IP：{ipaddr}")
            print()

    for ipaddr in valid_ips:
        bander = s_content(2, ipaddr, options.port)
        print(ipaddr + "的扫描结果:")
        print(bander)