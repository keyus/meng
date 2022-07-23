import pyautogui as gui
import time


def sleep(num=2):
    time.sleep(num)


# 点击
def click(src, offsetX=5, offsetY=5, sleepTime=2):
    res = gui.locateOnScreen(src, confidence=0.9)
    if res:
        x = res.left + offsetX
        y = res.top + offsetY
        gui.click(x, y)
        sleep(sleepTime)
        return True
    return False

# 点击 end right bottom 坐标点  默认休息时间 2秒
def clickEnd(src, offsetX=5, offsetY=5, sleepTime=2):
    res = gui.locateOnScreen(src, confidence=0.9)
    if res:
        x = res.left + res.width - offsetX
        y = res.top + res.height - offsetY
        gui.click(x, y)
        sleep(sleepTime)
        return True
    return False

# 双击
def doubleClick(src, offsetX=5, offsetY=5, sleepTime=2):
    res = gui.locateOnScreen(src, confidence=0.9)
    if res:
        x = res.left + offsetX
        y = res.top + offsetY
        gui.doubleClick(x, y)
        sleep(sleepTime)
        return True
    return False

# 双击 end right bottom 坐标点  默认休息时间 2秒
def doubleClickEnd(src, offsetX=5, offsetY=5, sleepTime=2):
    res = gui.locateOnScreen(src, confidence=0.9)
    if res:
        x = res.left + res.width - offsetX
        y = res.top + res.height - offsetY
        gui.doubleClick(x, y)
        sleep(sleepTime)
        return True
    return False


# 点击所有坐标点
def clickAll(src, offsetX=5, offsetY=5, sleepTime=1,):
    res = gui.locateAllOnScreen(src, confidence=0.9)
    res = list(res)
    length = len(res)
    if length > 0:
        for loc in res:
            x = loc.left + offsetX
            y = loc.top + offsetY
            gui.click(x, y)
            sleep(sleepTime)
        return True

    return False


# 点击所有坐标点
def clickEndAll(src, offsetX=5, offsetY=5, sleepTime=1):
    res = gui.locateAllOnScreen(src, confidence=0.9)
    res = list(res)
    length = len(res)

    if length > 0:
        for loc in res:
            x = loc.left + loc.width - offsetX
            y = loc.top + loc.height - offsetY
            gui.click(x, y)
            sleep(sleepTime)
        return True

    return False

# 点击所有坐标点


def doubleClickEndAll(src, offsetX=5, offsetY=5, sleepTime=1):
    res = gui.locateAllOnScreen(src, confidence=0.9)
    res = list(res)
    length = len(res)
    if length > 0:
        for loc in res:
            x = loc.left + loc.width - offsetX
            y = loc.top + loc.height - offsetY
            gui.doubleClick(x, y)
            sleep(sleepTime)
        return True

    return False

# 点击世界地图，进入长安城
def clickMap():
    res = clickEnd('img/common/screen1/pool.png',180,0)
    if res == False:
            return False
    # 长安城
    res = clickEnd('img/common/screen1/map-changancheng-1.png')
    if res == False:
        return  False
    return True

# 点击世界地图，进入长安城  config 5
def clickMapAll():
    res = clickEndAll('img/common/screen5/pool.png',60,0)
    if res == False:
            return False
    # 长安城
    res = doubleClickEndAll('img/common/screen5/map-changan-1.png')
    if res == False:
        return  False
    return True

# 点击世界地图，进入东海湾  config 5
def clickMapDonghaiAll():
    res = clickEndAll('img/common/screen5/pool.png',60,0)
    if res == False:
            return False
    # 东海湾
    res = clickAll('img/common/screen5/map-donghai-1.png',20,15)
    if res == False:
        return  False
    return True



# 是否处于战斗中
def isZhandou():
    return gui.locateOnScreen('img/common/screen1/zhandou.png', confidence=0.9)

def has(src):
    return gui.locateOnScreen(src, confidence=0.9)