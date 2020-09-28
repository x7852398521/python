# -*- coding: utf-8 -*-
import re, requests, bs4

#輸入座標轉地址(僅限台灣)，不須透過Google Map API免費實行座標轉地址功能
def address_TW(address_x,address_y):
    url_head = 'https://www.map.com.tw/map_engine/search.ashx?searchType=latLng'
    #address_x = '&x='+ ip_info['longitude']
    #address_y = '&y='+ ip_info['latitude']
    
    #address_x = '&x='+ '121.51987'
    #address_y = '&y='+ '25.04214'
    
    address_x = '&x='+ address_x
    address_y = '&y='+ address_y
    
    url = url_head + address_x + address_y
    headers = { 'User-Agent':'Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}
    proxies = {"http" : "60.251.40.84:1080"}
    
    try:
        htmlfile = requests.get(url, headers=headers, proxies=proxies)
        print("短網址下載成功")
    except Exception as err:
        print("短網址下載失敗: %s" % err)
    htmlfile.raise_for_status()
    
    objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
    address_a = eval(objSoup.text)['address']
    
    return address_a

if __name__ == '__main__':
    address_x = input('請輸入經度:\n')    #ex. 121.51987
    address_y = input('請輸入緯度:\n')    #ex. 25.04214 
    address = address_TW(address_x,address_y)
    print(address)