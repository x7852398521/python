#Google熱搜當日焦點新聞
def gn():
    import re
    import json
    import requests
    import pandas as pd
    #from bs4 import BeautifulSoup
    import datetime
    import tools.short_url
    
    headers = { 'User-Agent':'Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}          
    today = datetime.datetime.today()
    url = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=TW&ns=15'.format(datetime.datetime.strftime(today, '%Y%m%d'))
    proxies = {"http" : "60.251.40.84:1080"}
    
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        print("下載成功")
    except Exception as err:
        print("網頁下載失敗: %s" % err)
    resp.raise_for_status()
    
    today_news = []
    url_news = []
    news_total = '【今日焦點新聞】\n'
    ndf = pd.DataFrame(json.loads(re.sub(r'\)\]\}\',\n', '', resp.text))['default']['trendingSearchesDays'][0]['trendingSearches'])
    
    for i in ndf['articles']:
        today_news.append(i[0]['title'])                                #標題
        url_news.append(tools.short_url.short_url(i[0]['url']))         #網址
    for j in range(len(today_news)):
        if j == len(today_news)-1:
            news_temp = str(j+1)+'.'+today_news[j]+'\n'+url_news[j]
        else:
            news_temp = str(j+1)+'.'+today_news[j]+'\n'+url_news[j]+'\n\n'
        news_total = news_total+news_temp
    return news_total


def gnj():
    import re
    import json
    import requests
    import pandas as pd
    #from bs4 import BeautifulSoup
    import datetime
    import tools.short_url
    
    headers = { 'User-Agent':'Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}          
    today = datetime.datetime.today()
    url = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=JP&ns=15'.format(datetime.datetime.strftime(today, '%Y%m%d'))
    proxies = {"http" : "60.251.40.84:1080"}
    
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        print("下載成功")
    except Exception as err:
        print("網頁下載失敗: %s" % err)
    resp.raise_for_status()
    
    today_news = []
    url_news = []
    news_total = '【今日焦點新聞】\n'
    ndf = pd.DataFrame(json.loads(re.sub(r'\)\]\}\',\n', '', resp.text))['default']['trendingSearchesDays'][0]['trendingSearches'])
    
    for i in ndf['articles']:
        today_news.append(i[0]['title'])                                #標題
        url_news.append(tools.short_url.short_url(i[0]['url']))         #網址
    for j in range(len(today_news)):
        if j == len(today_news)-1:
            news_temp = str(j+1)+'.'+today_news[j]+'\n'+url_news[j]
        else:
            news_temp = str(j+1)+'.'+today_news[j]+'\n'+url_news[j]+'\n\n'
        news_total = news_total+news_temp
    return news_total
