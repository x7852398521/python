from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======呼叫python內建函式======
import random
from pypinyin import lazy_pinyin, Style  #中文轉拼音
import pypinyin                          #中文轉拼音
import tools.test_id
import tools.google_news
import tools.tw_pm
import tools.ip_search
import tools.address
import tools.rmd_beautyIMG
import time
#======呼叫python內建函式======

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
#from cv2 import cv2
import numpy as np
#======python的函數庫==========

# encoding: utf-8
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('AZUiOu4qJ4oYrsNGNQzfjwLsO+y5uj5OEwBbZJvIXgdR89r8M2xbIOEtnFYr7ytb39N4QC3K3HO4F9UsmNzB/eugLfMwZ7T/0Aw1JaMXzkUyBCpxoVpnUIzyRMth6pGwZZVWX6J+vxmRYDc0nooLeQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('05fc344d02a1374e0937df72e3692284')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text + "?\n你爹")  #回應一樣的對話
    line_bot_api.reply_message(event.reply_token, message)
"""
def isset(v):
    try : 
        type (eval(v)) 
    except :
        return  0  
    else : 
        return  1  

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    msglist = msg.split()
    if '派大星' == msg:
        message = TextSendMessage(text="派大星")
        line_bot_api.reply_message(event.reply_token, message)
    elif '貼圖'==msg:
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
    elif event.message.text == "圖片": 
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://miro.medium.com/max/708/1*ifSob78knBe5rME04WHftg.png', preview_image_url='https://miro.medium.com/max/708/1*ifSob78knBe5rME04WHftg.png'))
    elif event.message.text == "抽帥哥":
        tmp_url =  'https://lh3.googleusercontent.com/KR2zXmNNjK4YKAL4un1qZoRU6APHRjRKih6JCatHrnAKyQKMuruQQd5beDmaeeYh7PFqKRctoylbUNUPqKOI'
        #tmp_url = 'https://drive.google.com/file/d/1GtP1fU9RQZbccci3S-ZunsP7jGnIkHy-/view'
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=tmp_url, preview_image_url=tmp_url))
    elif event.message.text == "抽女生": 
        img_url = tools.rmd_beautyIMG.rmd_beautyIMG('[正妹]')
        print(img_url)
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    elif event.message.text == "抽男生": 
        img_url = tools.rmd_beautyIMG.rmd_beautyIMG('[帥哥]')
        print(img_url)
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    elif event.message.text == "吃什麼":
        L=['水餃、鍋貼','火鍋','燒烤','牛排','美式料理','義式料理(披薩、義大利麵)','夜市小吃','港式飲茶','生魚片、壽司','拉麵','滷肉飯']
        num=random.randint(0,len(L))
        message = TextSendMessage(text=L[num])
        line_bot_api.reply_message(event.reply_token, message)
    elif event.message.text == "剪刀石頭布":
        L=[chr(0x100030),chr(0x100032),chr(0x100031)]   #L=['剪刀','石頭','布']
        num=random.randint(0,len(L))
        message = TextSendMessage(text=L[num])
        line_bot_api.reply_message(event.reply_token, message)
    elif lazy_pinyin(msg[0:3]) == ['xi','ba','la']:     #當輸入"喜巴拉"(音相同即可)
        L=[chr(0x2680),chr(0x2681),chr(0x2682),chr(0x2683),chr(0x2684),chr(0x2685)]
        message = TextSendMessage(text='{}{}{}'.format(random.choice(L),random.choice(L),random.choice(L)))
        line_bot_api.reply_message(event.reply_token, message)
    elif msglist[0].lower() == '-en':
        from googletrans import Translator
        translator = Translator()
        trans_EN = translator.translate(msg[4:]).text
        message = TextSendMessage(text=trans_EN)
        line_bot_api.reply_message(event.reply_token, message)
    elif msglist[0].lower() == '-ja':
        from googletrans import Translator
        translator = Translator()
        trans_JA = translator.translate(msg[4:], dest='ja').text
        message = TextSendMessage(text=trans_JA)
        line_bot_api.reply_message(event.reply_token, message)
    elif msg[0].lower() == '-':
        from googletrans import Translator
        translator = Translator()
        trans_CH = translator.translate(msg[1:], dest='zh-TW').text
        message = TextSendMessage(text=trans_CH)
        line_bot_api.reply_message(event.reply_token, message)
    elif msglist[0] == '.ip':
        n = tools.ip_search.ip_search(msglist[1])
        address_x = str(n['longitude'])
        address_y = str(n['latitude'])
        try :
            address = tools.address.address_TW(address_x,address_y)
        except :
            text = 'ip： '+n['ip']+'\n'+'國名： '+n['country_name']+'\n'+'城市名： '+n['city']+'\n'+'緯度： '+str(round(n['latitude'],7))+'\n'+'經度： '+str(round(n['longitude'],7))
        else :
            text = 'ip： '+n['ip']+'\n'+'國名： '+n['country_name']+'\n'+'城市名： '+n['city']+'\n'+'緯度： '+str(round(n['latitude'],7))+'\n'+'經度： '+str(round(n['longitude'],7))+'\n'+'地址： '+ address
        message = TextSendMessage(text=text)
        line_bot_api.reply_message(event.reply_token, message)
    elif msglist[0] == '.gn':
        news_total = tools.google_news.gn()
        message = TextSendMessage(text=news_total)
        line_bot_api.reply_message(event.reply_token, message)
    elif msglist[0] == '.gnj':
        news_total = tools.google_news.gnj()
        message = TextSendMessage(text=news_total)
        line_bot_api.reply_message(event.reply_token, message)
    elif msglist[0] == '.pm':
        pm = tools.tw_pm.tw_pm()
        message = TextSendMessage(text=pm)
        line_bot_api.reply_message(event.reply_token, message)  
    elif msglist[0] == '.help':
        message = TextSendMessage(text="功能說明:\
                                        \n*輸入「-」再輸入任意語言，即可翻譯成中文\
                                        \n*輸入「-en 」再輸入任意語言，即可翻譯成英文\
                                        \n*輸入「-ja 」再輸入任意語言，即可翻譯成日文\
                                        \n*輸入「.gn」即可觀看今日焦點新聞\
                                        \n*輸入「.gnj」即可觀看今日日本焦點新聞\
                                        \n*輸入「.pm」即可觀看全台今日PM2.5\
                                        \n*輸入「.ip」查詢網站及ip所在地址\
                                        \n*輸入「吃什麼」機器人幫你決定今天吃什麼\
                                        \n*輸入「剪刀石頭布」機器人幫你出拳\
                                        \n*輸入「喜巴拉」機器人幫你骰骰子\
                                        \n*輸入「抽女生」即可抽美女圖\
                                        \n*輸入「抽男生」即可抽帥哥圖\
                                            ")
        line_bot_api.reply_message(event.reply_token, message)

    #elif event.message.text == "影片":
        #line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url='https://www.youtube.com/watch?v=7q88m5MQRhE', preview_image_url='https://miro.medium.com/max/708/1*ifSob78knBe5rME04WHftg.png'))
    #elif event.message.text == "音訊":
        #line_bot_api.reply_message(event.reply_token,AudioSendMessage(original_content_url='音訊網址', duration=100000))



"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
"""
@handler.add(MessageEvent, message=(ImageMessage))
def handle_message(event):
    #如果LINE用戶端傳送過來的是圖片
    if isinstance(event.message, ImageMessage):
        print('收到圖片訊息')
        hull_list = []
        position_0_x = []
        position_0_y = []
        position_5_x = []
        position_5_y = []
        image_content = line_bot_api.get_message_content(event.message.id)
        with open('temp_img.jpg','rb') as f:
            img_binary = f.read()
            o = cv2.imdecode(np.frombuffer(img_binary,np.uint8),cv2.IMREAD_COLOR)#二進位資料轉成數組array，讓圖片可以用cv讀取得到並且進行處理
            gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
            ret,binary=cv2.threshold(gray,150,255,cv.THRESH_BINARY)
            contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
            #=========劃出凸矩形並且標註其輪廓編號
            n = len(contours)
            font=cv2.FONT_HERSHEY_SIMPLEX
            for i in range(n):
                hull = cv2.convexHull(contours[i])
                M = cv2.moments(hull)
                #print(i,M['m00'])
                if M['m00'] > 80 and M['m00']<450:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    print('cx的座標',cx,'cy的座標',cy)
                    if cx<300 and cx>100:
                        if cy>1850 and cy<2300:
                            print(cx,cy)
                            position_0_x.append(cx)
                            position_0_y.append(cy)
                            cv2.putText(o,'o',(cx,cy),font,1,(0,0,255),3)#p=每個像素幾公分     
                    if cx<800 and cx>600:
                        if cy>1850 and cy<2300:
                            print(cx,cy)
                            position_5_x.append(cx)
                            position_5_y.append(cy)
                            cv2.putText(o,'o',(cx,cy),font,1,(0,0,255),3)#p=每個像素幾公分
                    print(position_0_x,position_0_y)
                    print(position_5_x,position_5_y)
    #                cv2.putText(o,'o',(cx,cy),font,1,(0,0,255),3)#p=每個像素幾公分

                if M['m00'] > 100000 and M['m00']<500000:
                    print('面積',M['m00'])
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    #print('cx,cy',cx,cy)
                    cv2.polylines(o,[hull],True,(0,255,0),3)
                    #cv.drawContours(o, [box], 0, (255, 0, 0), 1)
                    #print('hull['+str(i)+']面積=',int(cv.contourArea(hull)))
                    #print('hull['+str(i)+']長度=',int(cv.arcLength(hull,True)))
                    n=len(hull)
                    for coordinate in hull:
                        #print(coordinate[0])
                        hull_list.append(tuple(coordinate[0]))
                        '''最佳擬合直線
                        rows,cols = gray.shape[:2]
                        [vx,vy,x,y]=cv.fitLine((contours[i]),cv.DIST_L2,0,0.01,0.01)
                        lefty=int(-x*vy/vx)+y
                        righty=int(((cols-x)*vy/vx)+y)
                        cv.line(o,(cols-1,righty),(0,lefty),(0,255,0),3)
                        '''
            #=========劃出凸矩形並且標註其輪廓編號==========
            y=[]      
            for point in hull_list:
                #print(point[0])
                #print(point[1])
                y.append(point[1])
            #print('min(y)',min(y))
            #print('max(y)',max(y))
            print(max(y)-min(y))
            p=5/(position_5_x[0]-position_0_x[0])
            #print(p)
            cm=round((max(y)-min(y))*p,2)
            print("穗長%scm"%(cm))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
