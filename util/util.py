import pyautogui as gui
import util.screen as screen
from dataclasses import dataclass
import time
from pynput import keyboard


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


def click(src, offsetX=5, offsetY=5, sleepTime=1.2):
    box = gui.locateOnScreen(src, confidence=0.9)
    if box:
        gui.click(box.left + offsetX, box.top + offsetY)
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


def doubleClick(src, offsetX=5, offsetY=5, sleepTime=1.2):
    box = gui.locateOnScreen(src, confidence=0.9)
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


def clickAll(src, offsetX=5, offsetY=5, sleepTime=1.2):
    box = list(gui.locateAllOnScreen(src, confidence=0.9))
    lens = len(box)
    if lens > 0:
        for loc in box:
            gui.click(loc.left + offsetX, loc.top + offsetY)
            sleep(sleepTime)
        return lens
    return False


def clickCenterAll(src, sleepTime=0.6):
    box = list(gui.locateAllOnScreen(src, confidence=0.9))

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

# map ---------------------------------------------------------



# 长安城 npc map
def clickChangan():
    if clickEnd('img/common/screen1/pool.png', 180, 0):
        sleep(3)
        if clickEnd('img/common/screen1/map-changan-1.png'):
            print('进入长安城')
            return True
    return False

def clickChanganAll():
    if clickEndAll('img/common/screen5/pool.png', 60, 0):
        sleep(3)
        if doubleClickEndAll('img/common/screen5/map-changan-1.png'):
            return True
    return False


# 东海湾 npc map
def clickDonghaiAll():
    if clickEndAll('img/common/screen5/pool.png', 60, 0):
        sleep(3)
        if clickAll('img/common/screen5/map-donghai-1.png', 20, 15):
            return True
    return False

# 请选择
def clickSelectAll():
    lens = clickEndAll('img/common/screen5/select.png',-19,-35)
    if lens:
        return lens
    return False


# check ---------------------------------------------------------


# 是否处于战斗中
def isFighting():
    return gui.locateOnScreen('img/common/screen1/zhandou.png', confidence=0.9)


def has(src):
    return gui.locateOnScreen(src, confidence=0.9)


# 5开任务组，点击购买
def clickBuy():
    if has('img/common/screen5/yaodian.png'):
        print('检测到药店')
        if clickAll('img/common/screen5/yaodian.png',188,316):
            print('------点击了,药店购买')
    if has('img/common/screen5/baitan.png'):
        print('检测到摆摊')
        if clickAll('img/common/screen5/baitan.png',161,228):
            print('------点击了,商品')
        if clickEndAll('img/common/screen5/buy.png'):
            print('------点击了,购买')

    if has('img/common/screen5/shanghui.png'):
        print('检测到商会')
        if clickAll('img/common/screen5/shanghui.png',222,351):
            print('------点击了,商会购买')


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


