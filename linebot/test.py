
import random
from pypinyin import lazy_pinyin, Style  #中文轉拼音
import pypinyin                          #中文轉拼音
import tools.test
import tools.google_news
import tools.tw_pm
import tools.ip_search
import tools.address
import time





def isset(v):
    try : 
        type (eval(v)) 
    except :
        return  0  
    else : 
        return  1  
    
 
def handle_message(msg):
    msglist = msg.split()
    if msglist[0] == '.ip':
        n = tools.ip_search.ip_search(msglist[1])
        address_x = str(n['longitude'])
        address_y = str(n['latitude'])
        try :
            address = tools.address.address_TW(address_x,address_y)
        except :
            text = 'ip： '+n['ip']+'\n'+'國名： '+n['country_name']+'\n'+'城市名： '+n['city']+'\n'+'緯度： '+str(round(n['latitude'],7))+'\n'+'經度： '+str(round(n['longitude'],7))
        else :
            text = 'ip： '+n['ip']+'\n'+'國名： '+n['country_name']+'\n'+'城市名： '+n['city']+'\n'+'緯度： '+str(round(n['latitude'],7))+'\n'+'經度： '+str(round(n['longitude'],7))+'\n'+'地址： '+ address             
        print('回應：\n'+text)
        #message = TextSendMessage(text=text)
        #line_bot_api.reply_message(event.reply_token, message)
        
msg = input('輸入的訊息：')   
handle_message(msg)
