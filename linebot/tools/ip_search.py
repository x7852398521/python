#ip查詢
import re, requests, bs4
from urllib import parse

def ip_search(raw_address):
  
    def get_ip_or_url(ip_or_url):
        #nonlocal addr   #不再將addr視為內部變數
        #ip_or_url = 'www.yahoo.com.tw'  #TMP
        pattern_ip = r'\d+.\d+.\d+.\d+'
        pattern_url = r'(https?|ftp|file)?(://)?([-A-Za-z0-9+&@#/%?=~_|!:,.;]+)([-A-Za-z0-9+&@#/%=~_|])'
        addr_ip = re.search(pattern_ip, ip_or_url)
        addr_url = re.search(pattern_url, ip_or_url)
        if addr_ip:
            addr = addr_ip.group()
        elif addr_url and addr_url.group(1):
            addr_tmp = addr_url.group()
            urp = parse.urlparse(addr_tmp)
            addr = urp.netloc
        elif addr_url:
            addr_tmp = 'https://' + addr_url.group()
            urp = parse.urlparse(addr_tmp)
            addr = urp.netloc
        return addr
        
    #raw_address = 'www.yahoo.com.tw'
    raw_address = raw_address.strip()
    
    url_head = 'http://api.ipstack.com/'
    url_tail = '?access_key=7095a914391b41d02a89c24fcb5d815e'
    ip_or_url = get_ip_or_url(raw_address)
    url = (url_head + ip_or_url.strip() + url_tail).strip()
    
    urlfile = requests.get(url)
    ip_info = urlfile.json()
    return ip_info


if __name__ == '__main__':
    raw_address = input('請輸入網址或ip:\n')    #ex.'www.google.com' or '223.200.80.137'
    ip_info = ip_search(raw_address)
    print(ip_info,'\n')
    print('ip：',ip_info['ip'])
    print('洲名：',ip_info['continent_name'])
    print('國名：',ip_info['country_name'])
    print('城市名：',ip_info['city'])
    print('緯度：',ip_info['latitude'])
    print('經度：',ip_info['longitude'])