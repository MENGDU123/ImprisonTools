#该段代码作用是生成C类地址192.168.1.0/24段的IP地址列表。
#按题目中示例的写法：
"""
for i in range(0,256):
    print("192.168.1."+str(i))
"""
#按个人喜好写法：
def showip():
    print("192.168.1." + str(d))
print("Network Address:192.168.1.0")
print("Broadcast Address:192.168.1.255")
for d in range(1,255):
    if d==1:
        print("Start IP:",end="")
        showip()
        print("End IP:", end="")
        print("192.168.1." + str(d + 254))
        print("Ip Address List:")
        showip()
    else:
        showip()

