#身分製造機

def id_card(country_code,gender):
    import random
    country_id={1:{'country':'臺北市','eng_num':'A','num':10},
                2:{'country':'臺中市','eng_num':'B','num':11},
                3:{'country':'基隆市','eng_num':'C','num':12},
                4:{'country':'臺南市','eng_num':'D','num':13},
                5:{'country':'高雄市','eng_num':'E','num':14},
                6:{'country':'新北市','eng_num':'F','num':15},
                7:{'country':'宜蘭縣','eng_num':'G','num':16},
                8:{'country':'桃園市','eng_num':'H','num':17},
                9:{'country':'嘉義市','eng_num':'I','num':34},
                10:{'country':'新竹縣','eng_num':'J','num':18},
                11:{'country':'苗栗縣','eng_num':'K','num':19},
                12:{'country':'南投縣','eng_num':'M','num':21},
                13:{'country':'彰化縣','eng_num':'N','num':22},
                14:{'country':'新竹市','eng_num':'O','num':35},
                15:{'country':'雲林縣','eng_num':'P','num':23},
                16:{'country':'嘉義縣','eng_num':'Q','num':24},
                17:{'country':'屏東縣','eng_num':'T','num':27},
                18:{'country':'花蓮縣','eng_num':'U','num':28},
                19:{'country':'臺東縣','eng_num':'V','num':29},
                20:{'country':'金門縣','eng_num':'W','num':32},
                21:{'country':'澎湖縣','eng_num':'X','num':30},
                22:{'country':'連江縣','eng_num':'Z','num':33}}

    if not country_code.isdigit():
        raise Exception('請輸入整數')
    if int(country_code)<0:
        raise Exception('數值應介於1~22')
    if int(country_code)>22:
        raise Exception('數值應介於1~22')
    if int(country_code)==0:
        code = random.randint(1,22)
        num = country_id[code]['num']
        for k in country_id.values():
            if k['num'] == num:
                eng_num = k['eng_num'] 
    else:
        num=country_id[int(country_code)]['num']
        eng_num=country_id[int(country_code)]['eng_num']
    
    if not gender.isdigit():
        raise Exception('請輸入整數')
    if int(gender)<0:
        raise Exception('數值應介於1~2')
    if int(gender)>2:
        raise Exception('數值應介於1~2')
    if int(gender)==0:
        gender=random.randint(1,2)
    else:
        gender=int(gender)
    
    L=[]
    value=0
    if num>=10:
        L=list(str(num))
        value=int(L[0])*1+int(L[1])*9+value
    else:
        L.append('0')
        L.append(str(num))
        value=int(L[0])*1+int(L[1])*9+value
        
    L.append(str(gender))
    value+=gender*8
    
    for i in range(7):
        random_num=random.randint(0,9)
        L.append(str(random_num))
        value+=random_num*(7-i)
        
    last_num=10-value%10
    L.append(str(last_num))
    
    print()
    print('身分證字號:',eng_num,end='')
    for j in L[2:11]:
        print(j,end='')   
    print()

    return L


    
    
    