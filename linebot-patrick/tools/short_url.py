# -*- coding: utf-8 -*-
#短網址生成
#tools.short_url.short_url(long_url)


import requests
import bs4
import re
import urllib.parse

def short_url(long_url):
    if len(long_url)<40 or 'famitsu.com' in long_url:
        short_url = long_url
    else:
        match_url_re = re.compile(r'^https?://(.*)(.)$')
        match_url = match_url_re.match(long_url)
        
        if  match_url and match_url.group(2)!='/':
            long_url = urllib.parse.quote(match_url.group(1)+match_url.group(2), safe='')
        elif match_url and match_url.group(2)=='/':
            long_url = urllib.parse.quote(match_url.group(1), safe='')
        
        url = 'https://tinyurl.com/create.php?source=indexpage&url=https%3A%2F%2F{}&alias='.format(long_url)
        
        
        """
        match_url_re_01 = re.compile(r'^https?://([a-zA-Z0-9_\-\.\/]+)(\%.*)(.)$')
        match_url_re_02 = re.compile(r'^https?://(.*)(.)$')
        match_url_01 = match_url_re_01.match(long_url)
        match_url_02 = match_url_re_02.match(long_url)
        
        if '%' in long_url:
            if match_url_01 and match_url_01.group(3)!='/':
                long_url = match_url_01.group(1)[:-1]+'%2F'+match_url_01.group(2).replace('%','%25')+match_url_01.group(3)
            elif match_url_01 and match_url_01.group(3)=='/':
                long_url = match_url_01.group(1)[:-1]+'%2F'+match_url_01.group(2).replace('%','%25')
            url = 'https://tinyurl.com/create.php?source=indexpage&url=https%3A%2F%2F{}&alias='.format(long_url)
            
        elif match_url_02:
            if match_url_02 and match_url_02.group(2)!='/':
                long_url = match_url_02.group(1)+match_url_02.group(2)
            if match_url_02 and match_url_02.group(2)=='/':
                long_url = match_url_02.group(1)
            url = 'https://tinyurl.com/create.php?source=indexpage&url=https%3A%2F%2F{}%2F&alias='.format(long_url)
        else:
            url = 'https://tinyurl.com/create.php?source=indexpage&url=https%3A%2F%2F{}%2F&alias='.format(long_url)
            
            """
    
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
        #short_url=objSoup.select('div.indent')
        #short_url = objSoup.find_all('div', attrs = {'class' : re.compile(r'^indent$')})
        short_div = objSoup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['indent'])
        short_txt = short_div[0].text
        #print(short_div[0].text)
        
        match_full_domain_regex = re.compile(r'^(https?://)([a-zA-Z0-9.]+)/([a-zA-Z0-9]+)')
        match_full_domain = match_full_domain_regex.match(short_txt)
        #print(match_full_domain.groups())
        short_url = match_full_domain[0]
        #print(short_url)
    
    return short_url


if __name__ == '__main__':
    long_url = input('請輸入原網址:\n')    #ex.'www.google.com'
    print(short_url(long_url))