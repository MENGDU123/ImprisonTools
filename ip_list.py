#按题目中示例的写法：
"""
for i in range(0,256):
    print("192.168.1."+str(i))
"""
#按个人喜好写法：

a = None
b = None
c = None
d = None

def check_ipv4(__part__):
    __part__ = int(__part__)
    if not 0 <= __part__ <= 255:
        print("错误！网络地址应为")
        raise ValueError

ipaddr = input("Input the IP address: ")
parts = ipaddr.split(".")
for part in parts:
    if not a:
        check_ipv4(part)
        a = part
        continue
    if not b:
        check_ipv4(part)
        b = part
        continue
    if not c:
        check_ipv4(part)
        c = part
        continue
    if not d:
        check_ipv4(part)
        d = part
        continue
print(a,b,c,d,sep=".")






# class IP:
#     def __init__(self,__network__,__mask__):
#         for i in range(0,2**(32-__mask__)):
#             print(network+str(i))
#
# network = str(input("Network: "))
# mask = int(input("Mask: "))
# ip = IP(network,mask)






