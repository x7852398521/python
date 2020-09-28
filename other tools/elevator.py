####電梯系統#######
import time

class elevator():
    def __init__(self):
        self.floor = 1
        self.targets = set()
    def save_target(self,*goto):      
        for n in goto:
            self.targets.add(n)
    def __iter__(self):
        self.up = 1
        self.down = -1
        self.move = None
        return self
    def __next__(self):
        if len(self.targets) == 0:
            print('電梯靜止中，目前位於{}樓'.format(self.floor))
            time.sleep(3)
            #raise StopIteration
        elif not self.move:
            self.move = 0
            t_floor = min(self.targets, key=lambda x:abs(x-self.floor))  #最接近樓層
            if t_floor == self.floor:
                print('電梯開門中，請小心')
                time.sleep(1)
                print('電梯已關門，請小心')
                time.sleep(1)
                self.targets.remove(self.floor)
                t_floor = min(self.targets, key=lambda x:abs(x-self.floor))
            if t_floor > self.floor:
                print('電梯上樓中...')
                time.sleep(2)
                self.move = self.up
                self.floor += 1
            elif t_floor < self.floor:
                print('電梯下樓中...')
                time.sleep(2)
                self.move = self.down
                self.floor -= 1
        elif self.move == -1:
            print('目前位於{}樓'.format(self.floor))
            if self.floor in self.targets:
                print('電梯開門中，請小心')
                time.sleep(1)
                print('電梯已關門，請小心')
                time.sleep(1)
                self.targets.remove(self.floor)
            if len(self.targets) == 0:
                print('電梯靜止中，目前位於{}樓'.format(self.floor))
                time.sleep(3)
                #raise StopIteration
            elif len([n for n in self.targets if (n-self.floor)<0]) > 0:
                t_floor = max([n for n in self.targets if (n-self.floor)<0])  #小於且最接近本層樓
                print('電梯下樓中...')
                time.sleep(2)
                self.move = self.down
                self.floor -= 1
            elif len([n for n in self.targets if (n-self.floor)>0]) > 0:
                t_floor = min([n for n in self.targets if (n-self.floor)>0]) #大於且最接近本層樓
                print('電梯上樓中...')
                time.sleep(2)
                self.move = self.up
                self.floor += 1
        elif self.move == 1:
            print('目前位於{}樓'.format(self.floor))
            time.sleep(3)
            if self.floor in self.targets:
                print('電梯開門中，請小心')
                time.sleep(1)
                print('電梯已關門，請小心')
                time.sleep(1)
                self.targets.remove(self.floor)
            if len(self.targets) == 0:
                print('電梯靜止中，目前位於{}樓'.format(self.floor))
                time.sleep(3)
                #raise StopIteration
            elif len([n for n in self.targets if (n-self.floor)>0]) > 0:
                t_floor = min([n for n in self.targets if (n-self.floor)>0])  #大於且最接近本層樓
                print('電梯上樓中...')
                time.sleep(2)
                self.move = self.up
                self.floor += 1
            elif len([n for n in self.targets if (n-self.floor)<0]) > 0:
                t_floor = max([n for n in self.targets if (n-self.floor)<0])  #小於且最接近本層樓
                print('電梯下樓中...')
                time.sleep(2)
                self.move = self.down
                self.floor -= 1
                
#電梯鈕請求(內外按鈕皆適用)
class floor_oi():
    def floor_1(self,oi):
        if oi == 'on':
            e.save_target(1)
    def floor_2(self,oi):
        if oi == 'on':
            e.save_target(2)
    def floor_3(self,oi):
        if oi == 'on':
            e.save_target(3)
    def floor_4(self,oi):
        if oi == 'on':
            e.save_target(4)

e = elevator()
f = floor_oi()
e.__iter__()
f.floor_4('on') #按下4樓電梯鈕
f.floor_3('on') #按下3樓電梯鈕
while len(e.targets) != 0:
    e.__next__()
f.floor_4('on')
f.floor_2('on')
f.floor_3('on')
while len(e.targets) != 0:
    e.__next__()
f.floor_2('on')
while len(e.targets) != 0:
    e.__next__() 
f.floor_4('on')
f.floor_2('on')
f.floor_1('on')
while len(e.targets) != 0:
    e.__next__()
 
#print(e.targets)   
    