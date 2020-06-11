#101 整數輸出為固定格式
#輸入85 4 299 478後，輸出為以下
# |   85     4|
# |   85     4|
# |299   478  |
# |299   478  |
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
print('|{:>5} {:>5}|'.format(a,b))
print('|{:>5} {:>5}|'.format(a,b))
print('|{:<5} {:<5}|'.format(c,d))
print('|{:<5} {:<5}|'.format(c,d))

#102 浮點數輸出為固定格式
#輸入23.12 395.3 99.4617 564.329後，輸出為以下格式
# |  23.12  395.30|
# |  99.46  564.33|
# |23.12   395.30 |
# |99.46   564.33 |
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
print('|{:>7.2f} {:>7.2f}|'.format(a,b))
print('|{:>7.2f} {:>7.2f}|'.format(c,d))
print('|{:<7.2f} {:<7.2f}|'.format(a,b))
print('|{:<7.2f} {:<7.2f}|'.format(c,d))

#103 文字輸出為固定格式
#輸入my name is Neroal後，輸出為以下格式
# |        my       name|
# |        is     Neroal|
# |my         name      |
# |is         Neroal    |
a=input()
b=input()
c=input()
d=input()
print('|{:>10} {:>10}|'.format(a,b))
print('|{:>10} {:>10}|'.format(c,d))
print('|{:<10} {:<10}|'.format(a,b))
print('|{:<10} {:<10}|'.format(c,d))

#104 輸入半徑後，輸出半徑、周長、面積
#輸入15後，輸出以下內容
# Radius = 15.00
# Perimeter = 94.25
# Area = 706.86
import math
R=eval(input())
Per=2*R*(math.pi)
Area=R*R*(math.pi)
print('Radius','=','{:.2f}'.format(R))
print('Perimeter = {:.2f}'.format(Per))
print('Area = {:.2f}'.format(Area))

#105 輸入矩形寬、高，輸出寬、高、周長、面積
#輸入23.5 17後，輸出以下內容
# Height = 23.50
# Width = 17.00
# Perimeter = 81.00
# Area = 399.50
h=eval(input())
w=eval(input())
per=2*h+2*w
area=h*w
print('Height = {:.2f}'.format(h))
print('Width = {:.2f}'.format(w))
print('Perimeter = {:.2f}'.format(per))
print('Area = {:.2f}'.format(area))

#106 輸入時間分秒、距離，輸出速度
#輸入10 30 3後，輸出以下內容
# Speed = 10.7
x=eval(input())
y=eval(input())
z=eval(input())
print('Speed = {:.1f}'.format((z/1.6)/(x/60+y/3600)))

#107 輸入五整數，輸出五數字、總和、平勳
#輸入10 20 40 80 160後，輸出以下內容
# 10 20 40 80 160
# Sum = 310.0
# Average = 62.0
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
e=eval(input())
total=a+b+c+d+e
avg=(a+b+c+d+e)/5
print(a,b,c,d,e)
print('Sum = {:.1f}'.format(total))
print('Average = {:.1f}'.format(avg))

#108 輸入x1、y1、x2、y2，輸出座標及距離
#輸入2 1 5.5 8後，輸出以下內容
# (2.0,5.5) (1.0,8.0)
# Distance = 2.6926
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
dis=((x1-x2)**2+(y1-y2)**2)**0.5
print('( {} , {} )'.format(x1,y1))
print('( {} , {} )'.format(x2,y2))
print('Distance = {:.4f}'.format(dis))

#109 輸入邊長後，輸出五邊形面積
#輸入5後，輸出以下內容
# Area = 43.0119
import math
s=eval(input())
area=(5*s**2)/(4*math.tan(math.pi/5))
print('Area = {:.4f}'.format(area))

#110 輸入邊長及n邊形後，輸出n邊形面積
#輸入10 2.2後，輸出以下內容
# Area = 37.2400
import math
n=eval(input())
s=eval(input())
area=(n*s**2)/(4*math.tan(math.pi/n))
print('Area = {:.4f}'.format(area))

#201 輸入正整數，判斷是否為偶數
#輸入15 38後，輸出以下內容
# 15 is not an even number
# 38 is an even number
num=eval(input())
if num%2==0:
  print('{} is an even number'.format(num))
else:
  print('{} is not an even number'.format(num))
  
#202 輸入正整數，判斷是否為3或5的倍數
#輸入55 36 92 15後，輸出以下內容
# 55 is a multiple of 5.
# 36 is a multiple of 3.
# 92 is not a multiple of 3 or 5.
# 15 is a multiple of 3 and 5.
num=eval(input())
if num%3==0 and num%5==0:
  print('{} is a multiple of 3 and 5'.format(num))
elif num%3==0:
  print('{} is a multiple of 3'.format(num))
elif num%5==0:
  print('{} is a multiple of 5'.format(num))
else:
  print('{} is not a multiple of 3 or 5'.format(num))
  
#203 輸入年分，判斷是閏年還是平年(每四年一閏，每百年不閏，但每四百年也一閏)
#輸入2020 2045後，輸出以下內容
# 2020 is a leap year
# 2045 is not a leap year
num=eval(input())
if num%400==0 or num%100!=0 and num%4==0:
  print('{} is a leap year'.format(num))
else:
  print('{} is not a leap year'.format(num))
  
#204 輸入兩整數與運算子，輸出答案
#輸入15 20 *後，輸出300
a=input()
b=input()
z=input()
ans=eval(a+z+b)
print(ans)

#204
x=eval(input())
y=eval(input())
e=input()
if e=='+':
    z=x+y
elif e=='-':
    z=x-y
elif e=='*':
    z=x*y
elif e=='/':
    z=x/y
elif e=='//':
    z=x//y
elif e=='%':
    z=x%y
print(z)

#205 判斷字元是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）
#輸入@ c 5後，輸出以下內容
# @ is a symbol.
# c is an alphabet.
# 5 is a number.
a=input()
if a.isalpha():
    print('{} is an alphabet.'.format(a))
elif a.isdigit():
    print('{} is a number.'.format(a))
else:
    print('{} is a symbol.'.format(a))

#206 輸入分數，輸出對應的等級(A=80~100，B=70~79，C=60~69，F<=59)
#輸入69後，輸出C
num=eval(input())
if num<=59:
    print('F')
elif 60<=num<=69:
    print('C')
elif 70<=num<=79:
    print('B')
elif 80<=num<=100:
    print('A')

#207 輸入金額，顯示折扣完價格(38000以上7折，28000以上8折，18000以上9折，8000以上9.5折)
#輸入25000後，輸出22500
price=eval(input())
if 8000<=price<18000:
    print(price*0.95)
elif 18000<=price<28000:
    print(price*0.9)
elif 28000<=price<38000:
    print(price*0.8)
elif 38000<=price:
    print(price*0.7)

#208 輸入一個0~15的數值，轉成十六進位
#輸入13後，輸出5
num=eval(input())
if 0<=num<=15:
    a='{:x}'.format(num)

#209 輸入xy座標，輸出座標與(5,6)的距離
#輸入7 20、20 35，輸出Inside、Outside
x=eval(input())
y=eval(input())
dis=((x-5)**2+(y-6)**2)**0.5
if dis<=15:
    print('Inside')
else:
    print('Outside')

#210 輸入三角形三邊長，判斷是否可組成一個三角形(任意兩邊需大於第三邊)，可以則輸出邊長
#輸入5 6 13、2 2 2，輸出Invalid、6
a=eval(input())
b=eval(input())
c=eval(input())
if a+b>c and a+c>b and b+c>a:
    print(a+b+c)
else:
    print('Invaild')

#301 輸入兩正整數a、b，輸出a連加到b之總和
#輸入66 666，輸出219966
a=eval(input())
b=eval(input())
sum=0
for k in range(a,b+1):
    sum+=k
print(sum)

#302 輸入兩正整數a、b，輸出a連加到b間之偶數總和
#輸入14 1144，輸出327714
a=eval(input())
b=eval(input())
sum=0
for k in range(a,b+1):
    if k%2==0:
        sum+=k
print(sum)

#303 輸入正整數，以三角形的方式依序輸出
#輸入3，輸出以下內容
# 1
# 2 4
# 3 6 9
a=eval(input())
for i in range(a):
    for j in range(i+1):
        print('{:>4}'.format((i+1)*(j+1)),end=' ')
    print()

#304 輸入正整數a，輸出1到a之間所有5倍數數字總和
#輸入21，輸出50
a=eval(input())
sum=0
for k in range(1,a+1): 
    if k%5==0:
        sum+=k
print(sum)

#305 輸出反轉順序的值
#輸入123456，輸出654321
num=input()
print(num[::-1])

#305
num=input()
for k in range(len(num)):
    print(num[-k-1],end='')

#306 輸入一個正整數n，輸出n!的值
#輸入15，輸出1307674368000
a=eval(input())
sum=1
for k in range(1,a+1):
    sum*=k
print(sum)

#307 輸入一個正整數n，輸出n*n乘法表
#輸入3，輸出以下內容
# 1 * 1 = 1 2 * 1 = 2 3 * 1 = 3
# 1 * 2 = 2 2 * 2 = 4 3 * 2 = 6
# 1 * 3 = 3 2 * 3 = 6 3 * 3 = 9
num=eval(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print('{:<2}{:<2}{:<2}{:<2}{:<4}'.format(j,'*',i,'=',j*i),end='')
    print()

#308 輸入測試資料的筆數，每筆皆為一個正整數，將此正整數的每位數全部加總起來。
#輸入2 13579 2468，輸出以下內容
# Sum of all digits of 13579 is 25
# Sum of all digits of 2468 is 20
times=eval(input())
for k in range(times):
    sum=0
    num=input()
    for i in range(len(num)):
        sum+=eval(num[i])
    print('Sum of all digits of {} is {}'.format(num,sum))
    
#309 輸入金額、年收益率，以及經過的月份數，輸出每月的存款總額
#輸入50000 1.3 5，輸出以下內容
# Month Amount
# 1 50054.17
# 2 50108.39
# 3 50162.68
# 4 50217.02
# 5 50271.42
money=eval(input())
income=eval(input())
month=eval(input())
print('Month','Amount')
for k in range(month):
    money=money*(1+income/1200)
    print('{}'.format(k+1),'{:.2f}'.format(money))
    
#310 輸入正整數，輸出(1/(1**0.5+(1+1)**0.5))至(1/(n**0.5+(n+1)**0.5))總和
#輸入8，輸出1.8284 
n=eval(input())
sum=0
if n>1:
    for k in range(1,n):
        sum+=1/(k**0.5+(k+1)**0.5)
print('{:.4f}'.format(sum))

#401 輸入十個數字，輸出最小值
L=[]
for k in range(10):
    L.append(eval(input()))
print(min(L))

#402 輸入數字，輸入的動作直到輸入值為9999才結束，輸出最小值。
num=eval(input())
L=[]
while num!=9999:
    L.append(num)
    num=eval(input())
else:
    print(min(L))
    
#403 輸入兩個正整數a、b，輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）以及倍數之個數、總和
#輸入5 55，輸出以下內容
# 8   9   12  16  18  20  24  27  28  32  
# 36  40  44  45  48  52  54  
# 17
# 513
a=eval(input())
b=eval(input())
n=0
sum=0
for k in range(a,b+1):
    if k%4==0 or k%9==0:
        print('{:<4}'.format(k),end='')
        n+=1
        sum+=k
        if n%10==0:
            print()
print()
print(n)
print(sum)

#404 輸入一個正整數，將此正整數以反轉的順序輸出，並判斷如輸入0，則輸出為0
#輸入1234 0，輸出4321 0
num=input()
print(num[::-1])

#405 輸入數值，輸入的動作直到輸入值為9999才結束，輸出對應的等級(A=90~100，B=80~89，C=70~79，D=60~69，E=0~59)
#輸入100 50 60 9999，輸出A E D
score=eval(input())
while score!=-9999:
    if 90<=score<=100:
        print('A')
    elif 80<=score<=89:
        print('B')
    elif 70<=score<=79:
        print('C')
    elif 60<=score<=69:
        print('D')
    elif 0<=score<=59:
        print('E')
    score=eval(input())
    
#406 輸入身高、體重，直到輸入值為-9999才結束，輸出BMI、重度(under weight、normal、over weight、fat)
#輸入180 79 -9999，輸出BMI:24.38 State:normal
m=0
kg=0
while True:
    m=eval(input())/100
    if m==-9999/100:
        break
    kg=eval(input())
    if kg==-9999:
        break
    bmi=kg/m**2
    print('BMI: {:.2f}'.format(bmi))
    if bmi<18.5:
        print('State: under weight')
    elif 18.5<=bmi<25:
        print('State: under normal')
    elif 25<=bmi<30:
        print('State: over weight')
    elif 30<=bmi:
        print('State: fat')
        
#407 輸入年分，直到輸入值為-9999才結束，判斷是否為閏年或平年
#輸入2012 2006 -9999，輸出以下內容
#2012 is a leap year.
#2006 is not a leap year.
year=eval(input())
while year!=-9999:
    if year%400==0 or (year%100!=0 and year%4==0):
        print('{} is a leap year.'.format(year))
    else:
        print('{} is not a leap year.'.format(year))
    year=eval(input())

#408 輸入十個整數，輸出偶數和奇數的個數
#輸入1 2 3 4 5 6 7 8 9 10，輸出以下內容
# Even numbers: 5
# Odd numbers: 5
even=0
odd=0
for k in range(10):
    num=eval(input())
    if num%2==0:
        even+=1
    else:
        odd+=1
print('Even numbers: {}'.format(even))
print('Odd numbers: {}'.format(odd))

#409 輸入選票(No.1: Nami、No.2:Chopper)，每次投完輸出每位候選人的得票數，
#最後印出最高票者為當選人；如最終計算有相同的最高票數者或無法選出最高票者，顯示No one wonthe election.
no1_total=0
no2_total=0
no_vote=0
for k in range(5):
    vote=eval(input())
    if vote==1:
        no1_total+=1        
    elif vote==2:
        no2_total+=1
    else:
        no_vote+=1
    print('Total votes of No.1: Nami = {}'.format(no1_total))
    print('Total votes of No.2: Chopper = {}'.format(no2_total))
    print('Total null votes = {}'.format(no_vote))
if no1_total>no2_total:
    print('No.1 Nami won the election')
elif no1_total<no2_total:
    print('No.2 Chopper won the election')
else:
    print('No one won the election.')
    
#410 輸入n，輸出對應的等腰三角形
#輸入6，輸出以下內容
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
n=eval(input())
for k in range(n):
    print(' '*(n-k-1)+'*'*(k*2+1))
    
#501 呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、學號（StudentID）和姓名（Name）並顯示這些訊息
#輸入data science b123456 Neroal，輸出以下內容
# Department: data science
# Student ID: b123456
# Name: Neroal
def compute(D,S,N):
    print('Department:',D)
    print('Student ID:',S)
    print('Name:',N)
D=input()
S=input()
N=input()
compute(D,S,N)

#502 輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積
#輸入56 11，輸出616
def compute(x,y):
    print(x*y)
x=eval(input()) 
y=eval(input()) 
compute(x,y)

#503 輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳從a連加到b的和
#輸入1 10，輸出55
def compute(a,b):
    sum=0
    for k in range(a,b+1):
        sum+=k
    print(sum)
a=eval(input()) 
b=eval(input()) 
compute(a,b)

#504 輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳a**b的值
#輸入2 3，輸出8
def compute(a,b):
    print(a**b)
a=eval(input()) 
b=eval(input()) 
compute(a,b)

#505 輸入三個參數傳遞給一個名為compute()的函式，該函式功能為：一列印出x個a字元，總共印出y列(每一個字元後方有一空格)
#輸入e 5 5，輸出以下內容
# e e e e e 
# e e e e e 
# e e e e e 
# e e e e e 
# e e e e e 
def compute(a,x,y):
    for i in range(y):
        for j in range(x):
            print(a,end=' ')
        print()   
a=input()
x=eval(input()) 
y=eval(input())
compute(a,x,y)

#506輸入的三個整數（代表一元二次方程式 ax2+bx+c=0的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，
#該函式回傳方程式的解，如無解則輸出【Your equation has noroot.】
#輸入2 -3 1，輸出1.0,0.5
def compute(a,b,c):
    if (b**2-4*a*c)>=0:
        x1=(-b+(b**2-4*a*c)**0.5)/(2*a)  ########2*a需括號
        x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        print('{:.1f},{:.1f}'.format(x1,x2))
    else:
        print('Your equation has noroot.')
a=eval(input())
b=eval(input())
c=eval(input())
compute(a,b,c)

#507 輸入一個整數x，並將x傳遞給名為compute()的函式，此函式將回傳x是否為質數（Prime number）的布林值，
#接著再將判斷結果輸出。如輸入值為質數顯示【Prime】，否則顯示【Not Prime】
#輸入3，輸出Prime
def compute(x):
    p=0
    for k in range(2,x):
        if x%k==0:
            p+=1
    return p
x=eval(input())
if x<2:
    print('Not Prime')
elif compute(x)>1:
    print('Not Prime')
else:
    print('Prime')
    
#508 輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數
#輸入15,20，輸出5
def compute(x,y):
    for k in range(2,min(x,y)+1):
        if x%k==0 and y%k==0:
            ans=k
    return ans
x,y=eval(input())
print(compute(x,y))

#509 輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數），計算這兩個分數的和為p/q，
#接著將p和q傳遞給名為compute()函式，最後輸出的結果必須以最簡分數表示
#輸入1,2 1,6，輸出1 / 2 + 1 / 6 = 2 / 3
def compute(p,q):
    for k in range(2,min(p,q)+1):
        if p%k==0 and q%k==0:
            gcd=k
    return gcd
x,y=eval(input())
m,n=eval(input())
p=x*n+m*y
q=y*n
print(x,'/',y,'+',m,'/',n,'=',int(p/compute(p,q)),'/',int(q/compute(p,q)))

#510 輸入一正整數num，輸出費氏數列(F0=0，F1=1，Fn=Fn-1+Fn-2)
#輸入10，輸出0 1 1 2 3 5 8 13 21 34
def compute(num):
    Fn1=0
    Fn2=1
    print(Fn1,Fn2,end=' ')
    for k in range(num-2):
        Fn=Fn1+Fn2
        Fn1=Fn2
        Fn2=Fn
        print(Fn,end=' ')
num=eval(input())
if num>=2:
    compute(num)
    
#601 輸入的12個正整數(範圍1~99)。顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果
#輸入1 2 3 4 5 6 7 8 9 10 11 12，輸出以下內容
#   1  2  3
#   4  5  6
#   7  8  9
#  10 11 12
# 36  
L=[]
sum1=0
for i in range(12):
    num=eval(input())
    L.append(num)
for j in range(12):
    if (j+1)%3==0:
        print('{:>3}'.format(L[j]))
    else:
        print('{:>3}'.format(L[j]),end='')
    if j%2==0:
        sum1+=L[j]
print(sum1)

#602 輸入52張牌中的5張，計算並輸出其總和
#輸入5 10 j a 2，輸出29
L=[]
for k in range(5):
    poker=input()
    if poker.isdigit():
        L.append(eval(poker))
    elif poker=='J':
        L.append(11)
    elif poker=='Q':
        L.append(12)
    elif poker=='K':
        L.append(13)
    elif poker=='A':
        L.append(1)
print(sum(L))

#603 輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字
#輸入5 10 15 7 3 20 25 100 6 19，輸出100 25 20
L=[]
for k in range(10):
    L.append(eval(input()))
L.sort()
print(L[-1],L[-2],L[-3])
##print(sorted(L)[-1],sorted(L)[-2],sorted(L)[-3])

#604 輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數
#輸入1 1 1 2 2 2 2 3 4 4，輸出2 4
L=[]
n=0
for k in range(10):
    L.append(eval(input()))
for i in range(10):
    m=L.count(L[i])
    if m>n:
        num=L[i]
        n=m
print(num)
print(n)

#605 輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果
#輸入100 95 98 70 66 59 78 92 85 81，輸出665 83.12
L=[]
sum1=0
for k in range(10):
    L.append(eval(input()))
L.sort()
for i in range(1,len(L)-1):
    sum1+=L[i]
print(sum1)
print('{:.2f}'.format(sum1/8))

#606 輸入兩個正整數rows、cols，分別表示二維串列lst 的「第一個維度大小」與「第二個維度大小」。
#串列元素[row][col]所儲存的數字，其規則為：row、col 的交點值 = 第二個維度的索引col – 第一個維度的索引row。
#輸入3 6，輸出以下內容
#    0   1   2   3   4   5
#   -1   0   1   2   3   4
#   -2  -1   0   1   2   3
L=[]
rows=eval(input())
cols=eval(input())
def compute(rows,cols):
    for i in range(rows):
        L.append([])
        for j in range(cols):
            L[i].append(j-i)
            print('{:4}'.format(L[i][j]),end='')
        print()
compute(rows,cols)

#607 輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
#輸入50 67 77 80 59 29 87 93 100 60 85 83 79 77 80，輸出以下內容
# Student1: Sum 333 Average 66.60
# Student2: Sum 369 Average 73.80
# Student3: Sum 404 Average 80.80
L=[[],[],[]]
print('The 1st student:')
for i in range(5):
    L[0].append(eval(input()))
print('The 2nd student:')
for j in range(5):
    L[1].append(eval(input()))
print('The 3rd student:')
for k in range(5):
    L[2].append(eval(input()))
print('Student 1')
print('#Sum {}'.format(sum(L[0])))
print('#Average {:.2f}'.format(sum(L[0])/5))
print('Student 2')
print('#Sum {}'.format(sum(L[1])))
print('#Average {:.2f}'.format(sum(L[1])/5))
print('Student 3')
print('#Sum {}'.format(sum(L[2])))
print('#Average {:.2f}'.format(sum(L[2])/5))

########################################################
#608 建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引
#輸入3 1 10 19 2 77 8 5 60，輸出以下內容
# Index of the largest number 77 is: (1, 2)
# Index of the smallest number 1 is: (0, 1)
L=[]
for k in range(9):
    L.append(eval(input()))
arr_max=L.index(max(L))
arr_min=L.index(min(L))
print('Index of the largest number {} is: ({}, {})'.format(max(L),arr_max//3,arr_max%3))
print('Index of the smallest number {} is: ({}, {})'.format(min(L),arr_min//3,arr_min%3))

########################################################
#609 建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果
#輸入1 2 3 4 6 7 8 9，輸出以下內容
# Matrix 1:
# **1 2 **
# **3 4 **
# Matrix 2:
# **6 7 **
# **8 9 **
# Sum of 2 matrices:
# **7 9 **
# **11 13 **
L1=[[],[]]
L2=[[],[]]
print('Enter matrix 1:')
for i in range(2):
    for j in range(2):
        num1=eval(input('[{}, {}]: '.format(i,j)))
        L1[i].append(num1)
print('Enter matrix 2:')
for p in range(2):
    for q in range(2):
        num2=eval(input('[{}, {}]: '.format(p,q)))
        L2[p].append(num2)
print()
print('Matrix 1:')
for m in range(2):
    print('**',end='')
    for n in range(2):
        print('{} '.format(L1[m][n]),end='')
    print('**')
    
print('Matrix 2:')
for u in range(2):
    print('**',end='')
    for v in range(2):
        print('{} '.format(L2[u][v]),end='')
    print('**')
    
print('Sum of 2 matrices:')
for a in range(2):
    print('**',end='')
    for b in range(2):
        print('{} '.format(L1[a][b]+L2[a][b]),end='')
    print('**')
    
########################################################  
#610輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。
#輸入22.5 23 19.5 26.3 24.77 23.6 17.9 18.45 18.33 20.75 21.36 22.96，輸出以下內容
# Average 21.62
# Height 26.30
# Lowest 17.90    
L=[]
for i in range(4):
    print('Week {}:'.format(i+1))
    for j in range(3):
        L.append(eval(input('Day {}:'.format(j+1))))
print('Average: {:.2f}'.format(sum(L)/12))
print('Highest: {}'.format(max(L)))
print('Lowest: {}'.format(min(L)))

#701 輸入數個整數並儲存至串列中，以輸入-9999為結束點（串列中不包含-9999），
#再將此串列轉換成數組，最後顯示該數組以及其長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）
#輸入-5 3 100 1 -10 -9999，輸出以下內容
# (-5, 3, 100, 1, -10)
# Length: 5
#Max: 100
#min: -10
L=[]
num=eval(input())
while num!=-9999:
    L.append(num)
    num=eval(input())
L=tuple(L)
print(L)
print('Length:',len(L))
print('Max:',max(L))
print('Min:',min(L))
print('Sum:',sum(L)) 

#702 輸入並建立兩組數組，各以-9999為結束點。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。
#輸入1 2 3 -9999 2 7 -9999，輸出以下內容
# Combined tuple before sorting: (1, 2, 3, 2, 7)
# Combined list after sorting: [1, 2, 2, 3, 7]
t1=()
t2=()
print('Create tuple1:')
a=eval(input())
while a!=-9999:
    t1+=(a,)
    a=eval(input())
    
print('Create tuple2:')
b=eval(input())
while b!=-9999:
    t2+=(b,)
    b=eval(input())
print('Combined tuple before sorting:',t1+t2)
print('Combined list after sorting:',sorted(list(t1+t2)))

#703 輸入一些字串至數組，以字串"end"為結束點。接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素
#輸入san candy sunny zed neroal end，輸出以下內容
# ('san', 'candy', 'sunny', 'zed', 'neroal')
# ('san', 'candy', 'sunny')
# ('sunny', 'zed', 'neroal')
t=()
st=input()
while st!='end':
    t+=(st,)
    st=input()
print(t)
print(t[0:3])
print(t[-3:])

#704 輸入數個整數並儲存至集合，以輸入-9999為結束點，最後顯示該集合的長度、最大值、最小值、總和
#輸入-5 10 66 -32 7 -9999，輸出以下內容
# Length: 5
# Max: 66
# Min: -32
# Sum: 46
U=set()
num=eval(input())
while num!=-9999:
    U.add(num)
    num=eval(input())
print('Length:',len(U))
print('Max:',max(U))
print('Min:',min(U))
print('Sum:',sum(U))
 
#705 依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中。
#接著回答：set2是否為set1的子集合（subset）？set3是否為set1的超集合（superset）？
#輸入(Input to set1:) 3 28 -2 7 39 (set2:) 2 77 0 (set3:) 3 28 12 99 39 7 -1 -2 65，輸出以下內容
# set2 is subset of set1: False
# set3 is subset of set1: True
set1=set()
set2=set()
set3=set()
print('Input to set1:')
for i in range(5):
    set1.add(eval(input()))
print('Input to set2:')
for j in range(3):
    set2.add(eval(input()))
print('Input to set3:')
for k in range(9):
    set3.add(eval(input()))
print('set2 is subset of set1:',set2.issubset(set1))  
print('set3 is superset of set1:',set3.issuperset(set1))  

#706 輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，程式判斷該句子是否為全字母句(是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子)
#輸入1 the quick brown fox jumps over the lazt dog，輸出True
times=eval(input())
pangram=set('abcdefghijklmnopqrstuvwxyz')
for k in range(times):
    st=set(input().lower())
    st.discard(' ')#################################################################
    print(st==pangram)
    
#707 輸入X組和Y組各自的科目至集合中，以字串"end"作為結束點。請依序分行顯示(1) X組和Y組的所有科目、
#(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。
#輸入(Enter group X subject:) math english end (Enter group Y subject:) math chinese graphic music end，輸出以下內容
# ['chinese', 'english', 'graphic', 'math', 'music']
# ['math']
# ['chinese', 'graphic', 'music']
# ['chinese', 'english', 'graphic', 'music']    
x=set()
y=set()
print("Enter group X's subjects:")
su=input()
while su!='end':
    x.add(su)
    su=input()
print("Enter group Y's subjects:")
su=input()
while su!='end':
    y.add(su)
    su=input()
print(sorted(x|y))#################################################################
print(sorted(x&y))#################################################################
print(sorted(y-x))#################################################################
print(sorted(x^y))#################################################################

#708 輸入兩個詞典，將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值
#輸入a ant c cat z zed end g gold b bed q quick end，輸出以下內容
# a: ant
# b: bed
# c: cat
# g: gold
# q: quick
# z: zed
dict1={}
dict2={}
print('Create dict1:')
while True:
    key=input('Key: ')
    if key=='end':
        break
    value=input('Value: ')
    if value=='end':
        break
    dict1[key]=value
print('Create dict2:')
while True:
    key=input('Key: ')
    if key=='end':
        break
    value=input('Value: ')
    if value=='end':
        break
    dict2[key]=value  
dict1.update(dict2)#################################################################
for i in sorted(dict1.keys()):############
    print(i,': ',dict1[i])############
    
#709 輸入一顏色詞典color_dict，再根據key值的字母由小到大排序並輸出
#輸入a ant e egg b bold q queue end，輸出以下內容
# a: ant
# b: bold
# e: egg
# q: queue
U={}
while True:
    key=input('Key: ')
    if key=='end':
        break
    value=input('Value: ')
    if value=='end':
        break
    U[key]=value
for i in sorted(U.keys()):
    print(i,': ',U[i])
    
#710 輸入資料，再輸入一鍵值並檢視此鍵值是否存在於該詞典中
#輸入a ant b banana c candy d dog end (search key:) b，輸出Ture
D={}
while True:
    key=input('Key:')
    if key=='end':
        break
    value=input('Value:')
    if value=='end':
        break
    D[key]=value
search=input('Search key:')
print(search in D.keys())####################################

#801 輸入一字串，顯示該字串每個字元的索引
#輸入neroal，輸出以下內容
# Index of 'n': 0
# Index of 'e': 1
# Index of 'r': 2
# Index of 'o': 3
# Index of 'a': 4
# Index of 'l': 5
string=input()
for i in range(len(string)):
    print("Index of '{}': {}".format(string[i],i))
    
#802 輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和
#輸入abcdefg，輸出以下內容
# ASCII code for 'a' is 97
# ASCII code for 'b' is 98
# ASCII code for 'c' is 99
# ASCII code for 'd' is 100
# ASCII code for 'e' is 101
# ASCII code for 'f' is 102
# ASCII code for 'g' is 103
# 700.0  
sum1=0.
string=input()
for i in string:
    print("ASCII code for '{}' is {}".format(i,ord(i)))
    sum1+=ord(i)
print(sum1)

#803 輸入一個句子（至少有五個詞，以空白隔開），並輸出該句子倒數三個詞。
#輸入many foreign student study in FJU，輸出study in FJU
string=input().split()
print(string[-3],string[-2],string[-1])

#804 輸入一字串，分別將該字串轉換成全部大寫以及每個字的第一個字母大寫。
#輸入learn python is funny，輸出以下內容
# LEARN PYTHON IS FUNNY
# Learn Python Is Funny
string=input()
print(string.upper())
print(string.title())###########################################

#805 輸入一個長度為6的字串，輸出固定格式
#輸入python，輸出以下內容
# |python    |
# |  python  |
# |    python|
s = input()
print('|{:<10}|'.format(s))
print('|{:^10}|'.format(s))
print('|{:>10}|'.format(s))

#806 輸入一字串和一字元，並將此字串及字元作為參數傳遞給名為compute()的函式，此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。
#輸入python n，輸出n occurs 1 time(s)
def compute(a,b):
    sum1=0
    for i in a:
        if i==b:
            sum1+=1
    return sum1
a=input()
b=input()
count=compute(a,b)
print(f'{b} occurs {count} time(s)')

#807 輸入一字串，該字串為五個數字，以空白隔開。請將此五個數字加總（Total）並計算平均（Average）
#輸入12 15 60 77 30，輸出以下內容
# Total = 194
# Average = 38.8
L=[]       
a=input().split()
for i in range(len(a)):
    L.append(eval(a[i]))
print(f'Total = {sum(L)}')
print(f'Average = {sum(L)/len(L)}')

#807
a=input()
total=eval(a.replace(' ',' + '))
avg=total/len(a.split())
print(f'Total = {total}')
print(f'Average = {avg}')

#################################################################################################
#808 輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。
#輸入123-45-67888 13a-78-5553，輸出以下內容
# Vaild SSN
# Invaild SSN
a=input().replace('-','')
if a.isdigit():
    print('Valid SSN')
else:
    print('Invalid SSN') 
    
#809 輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
#a. 必須至少八個字元。
#b. 只包含英文字母和數字。
#c. 至少要有一個大寫英文字母。
#d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】
#輸入39Gfkd587 39gfkd333，輸出以下內容 
# Vaild password
# Invaild password
c=0
pw=input()
for k in pw:
    if k.isupper():
        c+=1
if len(pw)>=8 and pw.isalnum() and c>0:
    print('Valid password')
else:
    print('Invalid password')
    
#810 輸入正整數k（1 <=k <= 100），代表有k筆測試資料。每一筆測試資料是一串數字，每個數字之間以一空白區隔
#請找出此串列數字中最大值和最小值之間的差。
#先輸入2，輸入13 15 -5 77 60，再輸入30 35 40，輸出82.00 10.00
n=0
while n<1 or n>100:
    n=eval(input())
for i in range(n):
    a=input().split()
    L=[]
    for j in range(len(a)):
        L.append(eval(a[j]))
    print('{:.2f}'.format(max(L)-min(L)))
    
#901 輸入的五筆資料寫入到write.txt
data=open('write.txt',mode='w',encoding='UTF-8')
for k in range(5):
    data.write(input())
    data.write('\n')  ##########################################################
data.close()

#內容有問題
#902 讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出
L=[]
data=open('read.txt',mode='r',encoding='UTF-8')
txt=data.read().split()
for i in range(len(txt)):
    L.append(eval(txt[i]))
data.close()
print(sum(L))

#903 輸入五個人的名字並加入到data.txt的尾端。之後再顯示此檔案的內容。
data=open('read.txt',mode='a+',encoding='UTF-8')
for k in range(5):
    data.write('\n')
    data.write(input())
print('Append completed!')
print('Content of "data.txt:"')
data.seek(0,0)  #指標移至資料的最前頭
print(data.read())
data.close()

#904 讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者
data=open('read.txt',mode='r',encoding='UTF-8')
txt=data.read()
txt_list=txt.split()
N=[]
H=[]
W=[]
for k in range(len(txt_list)):
    if (k+1)%3==0:
        W.append(eval(txt_list[k]))
    elif (k+1)%3==2:
        H.append(eval(txt_list[k]))
    else:
        N.append(txt_list[k])
print('Average high: {:.2f}'.format(sum(H)/len(H)))
print('Average weight: {:.2f}'.format(sum(W)/len(W)))
h_num=H.index(max(H))
w_num=W.index(max(W))
print('The tallest is {} with {:.2f}cm'.format(N[h_num],H[h_num]))
print('The heaviest is {} with {:.2f}kg'.format(N[w_num],W[w_num]))
data.close()

#905 輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔
datafile=input()
reptxt=input()
data1=open(datafile,mode='r',encoding='UTF-8')
old_txt=data1.read()
new_txt=old_txt.replace(reptxt,'')
data1.close()
data1=open(datafile,mode='w',encoding='UTF-8')
data1.write(new_txt)
data1.close()
print('=== Before the deletion')
print(old_txt)
print('=== After the deletion')
print(new_txt)

#906 輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之
data=input()
s1=input()
s2=input()
data1=open(data,mode='r',encoding='UTF-8')
old_txt=data1.read()
new_txt=old_txt.replace(s1,s2)
data1.close()
data1=open(data,mode='w',encoding='UTF-8')
data1.write(new_txt)
data1.close()
print('== Before the replacement')
print(old_txt)
print('== After the replacement')
print(new_txt)

#907 輸入檔名read.txt，顯示該檔案的行數、單字數（簡單起見，單字以空白隔開即可，忽略其它標點符號）以及字元數（不含空白）。
data=input()
data1=open(data,mode='r',encoding='UTF-8')
txt=data1.read()
lines=txt.split('\n')
words=txt.split()
char=txt.replace('\n','').replace(' ','')
print('{} line(s)'.format(len(lines)))
print('{} word(s)'.format(len(words)))
print('{} character(s)'.format(len(char)))
data1.close()

#################################################################################
#908 輸入檔名read.txt，以及檔案中某單字出現的次數。輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可)
data=input()
num=eval(input())
data1=open(data,mode='r',encoding='UTF-8')
#data_txt=data1.read().replace('\n','').replace(' ','')  #計算字元數
data_txt=data1.read().split()
data_set=sorted(set(data_txt))
for k in data_set:
    if data_txt.count(k)==num:
        print(k)
data1.close()

#909 輸入的五個人的資料寫入data.dat檔，每一個人的資料為姓名和電話號碼，以空白分隔。再將檔案加以讀取並顯示檔案內容
data=open('data.dat',mode='w',encoding='UTF-8')
for k in range(5):
    data.write(input())
    data.write('\n')
    data.write('\n')
data=open('data.dat',mode='r',encoding='UTF-8')
print('The content of "data.dat":')
print(data.read())
data.close()

#910 讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後是個人記錄。
#請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）
data=open('read.dat',mode='r',encoding='UTF-8')
txt=data.read().split()
male=0
female=0
for k in range(len(txt)):
    if (k+1)>=5:
        if (k+1)%4==3 and eval(txt[k])==0:
            female+=1
        elif (k+1)%4==3 and eval(txt[k])==1:
            male+=1
print('Number of males: {}'.format(male))
print('Number of females: {}'.format(female))
data.close()

        























    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
