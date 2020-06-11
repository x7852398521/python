# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:09:09 2020

@author: Jason
"""
def tw_pm():
    
    import requests
    import json
    import pandas as pd
    
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}
    proxies = {"https" : "59.124.224.180:3128"}   
    url = 'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json'
    
    try:
        aqijsons = requests.get(url, headers=headers, proxies=proxies)  #proxies=proxies
    except Exception as err:
        print('下載失敗：{}'.format(err))
    #print(aqijsons.text)
    aqijson = aqijsons.json()
    #data.to_csv('bbb.csv', encoding='utf_8_sig')     #輸出csv
    
    for i in aqijson:
        if i['County'] == '基隆市':
            i['sort'] = 1
        elif i['County'] == '臺北市':
            i['sort'] = 2
        elif i['County'] == '新北市':
            i['sort'] = 3
        elif i['County'] == '桃園市':
            i['sort'] = 4
        elif i['County'] == '新竹市':
            i['sort'] = 5
        elif i['County'] == '新竹縣':
            i['sort'] = 6
        elif i['County'] == '宜蘭縣':
            i['sort'] = 7
        elif i['County'] == '苗栗縣':
            i['sort'] = 8
        elif i['County'] == '臺中市':
            i['sort'] = 9
        elif i['County'] == '彰化縣':
            i['sort'] = 10
        elif i['County'] == '雲林縣':
            i['sort'] = 11
        elif i['County'] == '嘉義市':
            i['sort'] = 12
        elif i['County'] == '嘉義縣':
            i['sort'] = 13
        elif i['County'] == '南投縣':
            i['sort'] = 14
        elif i['County'] == '花蓮縣':
            i['sort'] = 15
        elif i['County'] == '臺南市':
            i['sort'] = 16
        elif i['County'] == '高雄市':
            i['sort'] = 17
        elif i['County'] == '臺東縣':
            i['sort'] = 18
        elif i['County'] == '屏東縣':
            i['sort'] = 19
        elif i['County'] == '澎湖縣':
            i['sort'] = 20
        elif i['County'] == '金門縣':
            i['sort'] = 21
        elif i['County'] == '連江縣':
            i['sort'] = 22
    
    pd.set_option('display.unicode.ambiguous_as_wide', True)   #DataFrame排版環境設定
    pd.set_option('display.unicode.east_asian_width', True)    #DataFrame排版環境設定
    
    data = pd.DataFrame(aqijson)
    data = data.sort_values(by='sort', ascending=True)
    rank = range(1,len(data['County'])+1)
    data['sort'] = rank
    data_rn = data[['County','SiteName','AQI','PM2.5','sort']].rename(columns={'County':'縣市','SiteName':'測站名稱'})
    #print(data[['County','SiteName','AQI','PM2.5']].rename(columns={'County':'縣市','SiteName':'測站名稱'}))
    #data_tmp = data[['County','SiteName','AQI','PM2.5']].rename(columns={'County':'縣市','SiteName':'測站名稱'}).to_string(index=False)  #先試試看 
     
    col = "{0:^4} {1:>5}  {2:^3} {3:^5}".format(data_rn.columns[0],data_rn.columns[1].strip().replace(u'\u3000', u' '),data_rn.columns[2],data_rn.columns[3])
    string = col+'\n'
    
    for j in range(1,len(data_rn['縣市'])+1):
        data_county = data_rn.loc[data_rn['sort']==j]['縣市'].to_string(index=False).strip()
        data_name = data_rn.loc[data_rn['sort']==j]['測站名稱'].to_string(index=False).strip()
        data_aqi = data_rn.loc[data_rn['sort']==j]['AQI'].to_string(index=False).strip()
        data_pm = data_rn.loc[data_rn['sort']==j]['PM2.5'].to_string(index=False).strip()
        #data_name = chinese_format(data_name)
        data_iter = "{0:^3} {1:{4}^5} {2:>3} {3:>5}".format(data_county,data_name,data_aqi,data_pm,chr(12288))
        if j == len(data_rn['縣市']):
            string = string + data_iter
        else:
            string = string + data_iter+'\n'
    return string
    #return data_tmp
    
if __name__ == '__main__':
    print(tw_pm())