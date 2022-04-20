import random
import os
import time

#点按（x,y）点
def tap(point):
    os.system("adb shell input tap {} {}".format(point[0],point[1]))
    time.sleep(1)
# print("由（{}，{}）滑动到（{}，{}）".format(x1,y1,x2,y2))
def swipe(point2,point1=(390,850),time=4000):
    shell = "adb shell input swipe {} {} {} {} {}".format(point1[0],point1[1],point2[0],point2[1],time)
    os.system(shell)

key = {
    'battle':(1000,800),
    'solo':(1440,560),
    'matching':(840,510),
    'mo':(920,430),
    'yes':(1370,760),
    'input':(1200,830),
    'center':(390,850),
    'up':(530,700),
    'down':(250,1000),
    'left':(250,700),
    'right':(530,1000),
    'attack':(2090,920),
    'setting':(2220,40),
    'surrender':(1420,940),
    'continue':(1200,970),
    'back':(1050,970),
    'again':(1350,970)
}

def begin_game():
    tap(key['battle'])
    print('开始对战')
    time.sleep(2)
    tap(key['solo'])
    print('1对1')
    time.sleep(2)
    tap(key['matching'])
    print('匹配')
    time.sleep(2)
    tap(key['mo'])
    print('墨家机关道')
    time.sleep(8)
    tap(key['yes'])
    print("确定")
    time.sleep(15)
    tap(key['input'])
    print('确认')
    time.sleep(2)
    begin_time = time.time()
    return begin_time

def surrender():
    tap(key['setting'])
    print('打开设置')
    time.sleep(2)
    tap(key['surrender'])
    print('点击投降')
    time.sleep(20)
    tap(key['matching'])
    print('点击')
    time.sleep(5)
    tap(key['continue'])
    print('继续')
    time.sleep(3)
    tap(key['back'])
    print('返回大厅')
    time.sleep(3)
    



def go():
    a = random.randint(1, 8)
    tap(key['attack'])
    if a == 1:
        swipe(key['right'])
        print("right")
    elif a == 2:
        # 向左移动
        swipe(key['down'])
        print('down')
    elif a == 3:
        # 向右移动
        swipe(key['left'])
        print('left')
    else:
        # 向前移动
        swipe(key['up'])
        print('up')
    tap(key['attack'])

def play_game():
    begin_time = begin_game()
    for i in range(1,1000):
        now_time = time.time()
        print(now_time-begin_time)
        if now_time-begin_time > 160 :
            surrender()
            break
        else:
            go()

if __name__ =="__main__":
    for i in range(1,100):
        play_game()
