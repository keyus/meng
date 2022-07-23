import pyautogui as gui
import time

# my screen 2160 1440          /3    720   700

config = {
    # max 5
    5: {
        'size': [720, 580],
        'loc': {
            0: [0, 0],
            1: [721, 0],
            2: [1441, 0],
            3: [0, 590],
            4: [721, 590],
        }
    },
    4: {
        'size': [1080, 700],
        'loc': {
            0: [0, 0],
            1: [1081, 0],
            2: [0, 701],
            3: [1081, 701],
            4: [0, 0],
        }
    },
    # mumu界面分辩率 1720 x 968  
    # 脚本监测窗口对应大小为 1720 x 1057
    # 适用队长任务  【捉鬼、副本】由队长带队，屏幕仅保留一个游戏窗口
    1: {
        'size': [1720, 1057],
        'loc': {
            0: [0, 0],
            1: [0, 0],
            2: [0, 0],
            3: [0, 0],
            4: [0, 0],
        }
    }
}


# 设置窗口位置,大小排版
def set(configKey = 1):
    useConfig = config[configKey]
    resize = useConfig['size']
    gameWinConfig = useConfig['loc']
    gameWin = gui.getWindowsWithTitle('梦幻西游')
    length = len(gameWin)
    if length < 1:
        return

    print(gameWin)
    for index, win in enumerate(gameWin):
        winWidth, winHeight = win.size
        loc = gameWinConfig[index]
        if winWidth == resize[0] and winHeight == resize[1]:
            print('窗口匹配成功：', resize[0], 'x',resize[1])
            break 
        win.resizeTo(resize[0], resize[1])
        win.moveTo(loc[0], loc[1])
        print('窗口不匹配，重设窗口END')

    time.sleep(2)

