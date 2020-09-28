#隨機抽正妹卡

import requests, bs4, random, re

def rmd_beautyIMG(wordinside):
    headers = { 'User-Agent':'Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',}
    proxies = {"http" : "60.251.40.84:1080"}
    
    
    url_ppt = 'https://www.ptt.cc'
    beauty = '/bbs/beauty/index.html'
    
    ptthtml = requests.get(url_ppt+beauty, cookies={'over18':'1'}, headers=headers, proxies=proxies)
    objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')
    
    div_page = objSoup.find('div', 'btn-group-paging')
    last_page = div_page.find_all('a')[1]['href']  #下一頁的網址
    
    pattern = r'(/bbs/Beauty/index)(\d+)(\.html)'
    index_page = re.search(pattern, last_page)
    
    on_off = 1         
    while on_off: #當有找到內本頁含有'[帥哥]或[正妹]'文字或是推文數超過10以上的文章
        page = random.randint(0,100) #隨機選頁
        page_url = index_page.group(1) + str(eval(index_page.group(2))-page) + index_page.group(3) #該頁數的網址
        ptthtml = requests.get(url_ppt + page_url, cookies={'over18':'1'}, headers=headers, proxies=proxies) #抓取該頁資料
        objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml') 
     
        hyp = []
        pttdivs = objSoup.find_all('div', 'r-ent') #尋找標籤為div屬性值為r-ent
        for i in range(len(pttdivs)):
            if pttdivs[i].find('a'):
                title_word = pttdivs[i].find('a').text
                push_num = pttdivs[i].find('div','nrec').text
                if wordinside in title_word and push_num:
                    if push_num == '爆':
                        push_num = '100'
                    elif push_num[0] == 'X':
                        push_num = '0'
                    if eval(push_num) > 9:
                        href = pttdivs[i].find('a')['href']  #文章超連結
                        hyp.append(url_ppt + href) #文章超連結串列
        if len(hyp)>0:
            on_off = 0

    radom_url = hyp[random.randint(0,len(hyp)-1)]
    beauty_html = requests.get(radom_url, cookies={'over18':'1'}, headers=headers, proxies=proxies)
    beauty_soup = bs4.BeautifulSoup(beauty_html.text, 'lxml')
    
    beauty_divs = beauty_soup.find('div', id='main-content')
    photos = []
    url_photos = beauty_divs.find_all('a')
    for photo in url_photos:
        href_photo = photo['href']
        if href_photo.startswith('https://i.imgur'):
            photos.append(href_photo)
    if len(photos)>1:
        random_photo = photos[random.randint(0,len(photos)-2)]
    else:
        random_photo = photos[random.randint(0,len(photos)-1)]
    return random_photo

if __name__ == '__main__':
    imgurl_girl = rmd_beautyIMG('[正妹]')
    imgurl_boy = rmd_beautyIMG('[帥哥]')
    print(imgurl_girl)
    print(imgurl_boy)





#尚未用到
def choice(a):
    #將0~a列成一個串列，隨機抽取串列內值，抽取完並刪除於串列
    #第一次使用:A,B=choice(數量)
    #後續使用:choice(A)
    if type(a) == int:
        L=[]
        for i in range(a+1):
            L.append(i)
        ch=random.choice(L)
        L.remove(ch)
    elif type(a) == list:
        L=a
        if len(L) == 0:
            print('串列內無值')
        else:
            ch=random.choice(L)
            L.remove(ch)
    return L,ch












