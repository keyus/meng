import util.screen as screen
import util.util as util
import time


# 师门
# 分辩率使用配置5 即在屏幕平铺5个游戏号窗口,支持同时压镖5个账号

class ShiMen():
    closeCount= 0
    def __init__(self):
        # screen.set(5)
        # time.sleep(2)
        print('师门：running....')
        self.loop()

    def loop(self):
        if util.stop : 
            print('按下空格键  任务结束')
            return 

        if self.closeCount >= 5:
            print('师门任务结束')
            return 
        if util.clickAll('img/task-shimen/go.png',34,10):
            print('去完成')
        
        if util.clickAll('img/task-shimen/bg.png'):
            print('点击了，背景')

        if util.clickEndAll('img/task-shimen/task-button1.png'):
            print('点击了，师门任务')

        if util.clickAll('img/task-shimen/task-button2.png',10,6):
            print('点击了，使用')

        # 购买任务组
        util.clickBuy()

        if util.clickAll('img/task-shimen/task-button3.png',30,45):
            print('点击了，请选择')
        if util.clickEndAll('img/task-shimen/task-button5.png'):
            print('点击了，上交')
        if util.clickEndAll('img/task-shimen/task-button6.png'):
            print('点击了，等等')

        if util.clickEndAll('img/common/screen5/task.png',0,-22):
            print('点击了，点击了任务栏文字')

        # close = util.clickAll('img/task-shimen/close.png')
        # if close:
        #     self.closeCount = self.closeCount + close
        #     print('已完成个数', self.closeCount)

        print('底部.....')
        self.loop()

util.start_listen()
ShiMen()
