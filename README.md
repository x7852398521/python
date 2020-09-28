# ReadME

## 591房屋交易租屋網資訊API

### 內政部不動產時價登錄網資料匯出程式(estate.py)
本程式共分為三項功能
1. 將以下五份【不動產買賣】資料表，分別建立dataframe物件，並將五個物件合併輸出成【df_all】
    * a_lvr_land_a.csv(臺北市不動產買賣資料)
    * b_lvr_land_a.csv(臺中市不動產買賣資料)
    * e_lvr_land_a.csv(高雄市不動產買賣資料)
    * f_lvr_land_a.csv(新北市不動產買賣資料)
    * h_lvr_land_a.csv(桃園市不動產買賣資料)
2. 以下列條件從【df_all】篩選出結果，並輸出【filter_a.csv】
    * 【主要用途】為【住家用】
    * 【建物型態】為【住宅大樓】
    * 【總樓層數】需【大於等十三層】
3. 以下列條件從【df_all】計算出結果，並輸出【filter_b.csv】
    * 計算 【總件數】
    * 計算 【總車位數】
    * 計算 【平均總價元】
    * 計算 【平均車位總價元】

### 使用方式
1. 安裝 pip install pandas
2. 安裝 pip install numpy
3. 執行estate.py
```bash
python estate.py
```

### 591房屋交易租屋網資訊API(c591.py、flask_c591.py)
利用爬網技術取得【591房屋交易租網】中，位於【臺北及新北】的所有【租屋物件資料】，並存取至MongoDB資料庫，以flask及Google Cloud Platform建立RESTful API供外部查詢。

其欄位包含【縣市】、【出租者】、【出租者身份】、【聯絡電話】、【型態】、【現況】、【性別要求】、【網址】

### 使用方式
* 開啟瀏覽器，網址列輸入 http://104.199.204.138/ 即可查詢所有租屋資料
* 網址列輸入 http://104.199.204.138/search/篩選條件 可查詢篩選後的租屋資料，範例如下
    * http://104.199.204.138/search/縣市=新北&性別要求=男 查詢男生可承租且位於新北市的租屋物件
    * http://104.199.204.138/search/聯絡電話=0912-708-643 以聯絡電話查詢租屋物件
    * http://104.199.204.138/search/出租者身份=n屋主 查詢所有非屋主自行刊登的租屋物件
    * http://104.199.204.138/search/縣市=台北&出租者性別=女&出租者姓氏=吳 查詢位於台北市屋主為女性且姓氏為吳的租屋物件
     
### 資料更新方式
* 開啟Google Cloud Platform，於終端機輸入sudo python c591.py即可


## line bot聊天機器人

* line bot 聊天機器人功能(line bot use python flask + heroku)
    * Google Trends 焦點新聞爬蟲（搭配短網址功能）
    * Google Translate API 翻譯功能
    * ptt表特版圖片爬蟲
    * ip查詢功能（搭配座標轉地址功能）
    * 行政院環境保護署pm2.5監測數據爬蟲
    * 隨機抽籤功能

## 其他工具

* 身分證製造機(id_card.py)

* 電梯模擬系統(elevator.py)

* ip查詢功能(get_host_ip.py)

* 短網址生成器(short_url.py)