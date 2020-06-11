#獲取本機ip
#輸入get_host_ip()即可

######################################方法一
"""
import socket
hostname = socket.gethostname()
# 獲取本機ip
ip = socket.gethostbyname(hostname)
print(ip)
"""

######################################方法二
import socket

def get_host_ip():
    """
    查詢本機ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

    #print(get_host_ip())


if __name__ == '__main__':
    print(get_host_ip())