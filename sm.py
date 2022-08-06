import util.util as util
import pyautogui as gui


# 师门
# 分辩率使用配置5 即在屏幕平铺5个游戏号窗口,支持同时压镖5个账号

class ShiMen():
    closeCount = 0

    def __init__(self):
        print('师门：running....')
        self.loop()

    def loop(self):

        if util.stop:
            print('按下空格键  任务结束')
            return

        tag = util.count('images/sm/sm-tag.png')
        if tag >= 5:
            if gui.locateOnScreen('images/sm/go.png') == None:
                print('师门完成')
                util.clickCenterAll('images/sm/close.png')
                print('点击关闭')
                return 
        
        if self.closeCount >= 5:
            print('师门任务结束')
            return

          # 请选择
        if util.clickSelect():
            return self.loop()

        if util.clickCenterAll('images/sm/go.png'):
            print('去完成')
            return self.loop()


        if util.clickAll('images/sm/sm-bg.png', -11, -17):
            print('点击了，背景')

        util.clickAnyway()

        if util.clickCenterAll('images/sm/sm-button.png'):
            print('点击了，师门任务')
            return self.loop()

        # 使用-上交
        util.clickUse()

        # 购买任务组
        util.clickBuy()

        if util.clickCenterAll('images/sm/shouxi.png'):
            print('点击了，首席')

        # 任务栏第一个任务
        util.clickTaskFirst()

        print('loop.....') 
        return self.loop()


util.start_listen()
ShiMen()
