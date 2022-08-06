import pyautogui as gui
import util.screen as screen
from dataclasses import dataclass
import time
from pynput import keyboard
import sys  

sys.setrecursionlimit(1000000)

# 游戏窗口数量
use = screen.use

# 坐标点


@dataclass
class Point():
    x: int
    y: int

    def __init__(self, box, offsetX=0, offsetY=0):
        self.x = box.left + box.width + offsetX
        self.y = box.top + box.height + offsetY

def sleep(num=2):
    time.sleep(num)


def center(box):
    return gui.center(box)


def end(box, offsetX=0, offsetY=0):
    return Point(box, offsetX, offsetY)


def click(src, offsetX=5, offsetY=5, sleepTime=1,confidence= 0.9):
    box = gui.locateOnScreen(src, confidence=confidence)
    if box:
        gui.click(box.left + offsetX, box.top + offsetY)
        sleep(sleepTime)
        return 1
    return False

def clickCenter(src, sleepTime=1,confidence= 0.9):
    box = gui.locateOnScreen(src, confidence=confidence)
    if box:
        loc = gui.center(box)
        gui.click(loc.x, loc.y)
        sleep(sleepTime)
        return 1
    return False


def clickEnd(src, offsetX=5, offsetY=5, sleepTime=1.2):
    box = gui.locateOnScreen(src, confidence=0.9)
    if box:
        loc = end(box)
        gui.click(loc.x - offsetX, loc.y - offsetY)
        sleep(sleepTime)
        return 1
    return False


def doubleClick(src, offsetX=5, offsetY=5, sleepTime=1.2, confidence= 0.9):
    box = gui.locateOnScreen(src, confidence=confidence)
    if box:
        gui.doubleClick(box.left + offsetX,  box.top + offsetY)
        sleep(sleepTime)
        return 1
    return False


def doubleClickEnd(src, offsetX=5, offsetY=5, sleepTime=1.2):
    box = gui.locateOnScreen(src, confidence=0.9)
    if box:
        loc = end(box)
        gui.doubleClick(loc.x - offsetX,  loc.y - offsetY)
        sleep(sleepTime)
        return True
    return False


def clickAll(src, offsetX=5, offsetY=5, sleepTime=1, confidence = 0.9):
    box = list(gui.locateAllOnScreen(src, confidence= confidence))
    lens = len(box)
    if lens > 0:
        for loc in box:
            gui.click(loc.left + offsetX, loc.top + offsetY)
            sleep(sleepTime)
        return lens
    return False


def clickCenterAll(src, sleepTime=1,confidence=0.9):
    box = list(gui.locateAllOnScreen(src, confidence=confidence))
    lens = len(box)
    if lens > 0:
        for loc in box:
            loc = gui.center(loc)
            gui.click(loc.x, loc.y)
            sleep(sleepTime)
        return lens
    return False

def clickEndAll(src, offsetX=5, offsetY=5, sleepTime=1):
    box = list(gui.locateAllOnScreen(src, confidence=0.9))
    lens = len(box)
    if lens > 0:
        for loc in box:
            loc = end(loc)
            gui.click(loc.x - offsetX, loc.y - offsetY)
            sleep(sleepTime)
        return lens
    return False


def doubleClickEndAll(src, offsetX=5, offsetY=5, sleepTime=1):
    box = list(gui.locateAllOnScreen(src, confidence=0.9))
    lens = len(box)
    if lens > 0:
        for loc in box:
            loc = end(loc)
            gui.click(loc.x - offsetX, loc.y - offsetY)
            sleep(sleepTime)
        return lens
    return False

# locs: [[offsetX,offsetY]，[offsetX,offsetY]],  根据找到的坐标，进行点击
def clickAllFlow(src,offset):
    box = list(gui.locateAllOnScreen(src, confidence=0.9))
    lens = len(box)
    if lens > 0:
        for it in offset:
            for loc in box:
                gui.click(loc.left + it[0], loc.top + it[1])
                sleep(1)
        return lens
    return False

# map ---------------------------------------------------------



# 长安城 npc map
def clickChangan():
    if click('images/common/yin.png', -120, 22):
        sleep(3)
        if clickCenter('images/common/map-changan.png'):
            print('进入长安城')
            return True
    return False

def clickChanganAll():
    if clickAll('images/common/yin.png', -120, 22):
        sleep(3)
        if clickCenterAll('images/common/map-changan.png'):
            print('进入长安城...')
            return True
    return False


def clickNpc(name):
    if clickChanganAll() == False:
        return False
    if clickAll('images/common/yin.png',-50,15) == False:
        return False
    print('打开npc 地图')
    sleep(2)
        
    if name == 'ben':
        if clickAll('images/common/npc.png',193, 207):
            print('点击了，百晓仙子')
            return True
    if name == 'gui':
        if clickAll('images/common/npc.png',155, 227):
            print('点击了，钟馗')
            return True
    if name == 'biao':
        if clickAll('images/common/npc.png',90, 235):
            print('点击了，钟馗')
            return True
    if name == 'tu':
        if clickAll('images/common/npc.png',390, 210):
            print('点击了，店小二')
            return True
    return False

# check ---------------------------------------------------------

# 统计数量
def count(src, confidence = 0.9):
    box =  list(gui.locateAllOnScreen(src, confidence=confidence))
    print(box)
    return len(box)

# 是否处于战斗中
def isFire():
    return gui.locateOnScreen('images/common/fire.png', confidence=0.9)


def has(src, confidence=0.9):
    return gui.locateOnScreen(src, confidence=confidence)


# 请选择单个
def clickSelect():
    if click('images/common/select.png',65,55,1,0.7):
        print('点击了请选择')
        return True
    return False

# 请选择
def clickSelectAll():
    if clickAll('images/common/select.png',65,55,1,0.7):
        print('点击了请选择')
        return True
    return False

# 5开任务组，点击购买
def clickBuy():
    if has('images/common/buy-none.png'):
        print('检测到空商品')
        if clickCenterAll('images/common/buy-close.png'):
            print('------点击了,关闭')
    if has('images/common/yaodian.png'):
        print('检测到药店')
        if clickAll('images/common/yaodian.png',200,325):
            print('------点击了,药店购买')
    if has('images/common/baitan.png'):
        print('检测到摆摊')
        if clickAllFlow('images/common/baitan.png', [[200,170],[225,370]]):
            print('------点击了,购买')
    if has('images/common/baitan-gf.png'):
        print('检测到工坊摆摊')
        if clickAllFlow('images/common/baitan-gf.png', [[0,105],[235,365]]):
            print('------点击了,工坊购买')
      
    if has('images/common/shanghui.png'):
        print('检测到商会')
        if clickAll('images/common/shanghui.png',235,370):
            print('------点击了,商会购买')
    if has('images/common/bingqi.png'):
        print('检测到兵器铺')
        if clickAll('images/common/bingqi.png',215,325):
            print('------点击了,兵器铺购买')

# 使用-上交
def clickUse():
    if clickCenterAll('images/common/give.png'):
        print('点击了，上交')
    if clickCenterAll('images/common/use.png'):
        print('点击了，使用')

# 任务栏第一个任务
def clickTaskFirst():
    if clickEndAll('images/common/book.png',-35,-25):
        print('点击了，任务栏第一个任务')

# 任务栏第二个任务
def clickTaskTwo():
    if clickAll('images/common/book.png',42,110):
        print('点击了，任务栏第二个任务')

# 点击任意位置继续
def clickAnyway():
    if doubleClickEndAll('images/common/right.png',40,5):
        print('点击了，顶部任意位置继续')


# listen ---------------------------------------------------------



def on_press(key):
    # 如果按下了 <Esc> 键
    if key == keyboard.Key.space:
        global stop
        stop = True

        # 停止监听
        listener.stop()

def on_release(key):
    print('...',key)

stop = False
listener  = None

# 开始监听
def start_listen():
    global listener 
    listener  = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener .start()


